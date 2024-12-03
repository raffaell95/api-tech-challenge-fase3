from typing import List
from fastapi import APIRouter, status, Depends
from fastapi import Depends, status, APIRouter, HTTPException
from sqlalchemy.orm import Session
from infra.config.database import get_db
from infra.repositories import RepositoryUData
import aiohttp
import zipfile
import os
from io import BytesIO
from schemas.schemas import UDataSchema


router = APIRouter()

ZIP_URL = "https://files.grouplens.org/datasets/movielens/ml-100k.zip"
DEST_DIR = "ml-100k"  # Diretório onde o conteúdo será extraído

@router.on_event("startup")
async def startup():
    # Criar diretório se não existir
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)

@router.post('/baixar/arquivo/movielens', status_code=status.HTTP_201_CREATED)
async def baixar_arquivo():
    try:
        # Baixando o arquivo zip
        async with aiohttp.ClientSession() as session:
            async with session.get(ZIP_URL) as response:
                if response.status != 200:
                    return {"erro": "Falha ao baixar o arquivo", "status": response.status}

                # Lendo o conteúdo do arquivo zip diretamente da resposta
                zip_content = await response.read()
                
                # Descompactando o arquivo zip
                with zipfile.ZipFile(BytesIO(zip_content)) as zf:
                    zf.extractall(DEST_DIR)

                return {"status": "sucesso", "mensagem": "Arquivo descompactado com sucesso!", "diretorio": DEST_DIR}

    except Exception as e:
        return {"erro": str(e)}


@router.post('/salvar/udata', status_code=status.HTTP_201_CREATED)
async def salvar_udata(session: Session =  Depends(get_db)):

    file_path = '/home/raffa/Documentos/api-tech-challenge-fase3/ml-100k/ml-100k/u.data'
    
    # Verifique se o arquivo existe antes de tentar abrir
    if not os.path.exists(file_path):
        return {"error": "Arquivo não encontrado"}

    try:
        # Abra o arquivo e leia as linhas
        with open(file_path, 'r') as file:
            lines = file.readlines()

        data: List[UDataSchema] = []
        for i, line in enumerate(lines):

            if i >= 10:
                break  # Sai do loop após processar 10 linhas

            parts = line.strip().split('\t')
            
            if len(parts) == 4:
                user_id, item_id, rating, timestamp = parts
                data.append(UDataSchema(user_id=user_id, item_id=item_id, rating=rating, timestamp=timestamp))


        repository = RepositoryUData(session).save(data)

        # Retornar os dados processados
        return {"data": repository}

    except Exception as e:
        return {"error": f"Ocorreu um erro ao ler o arquivo: {str(e)}"}
    

@router.get('/listar/udata', status_code=status.HTTP_200_OK)
async def listar_udata(session: Session =  Depends(get_db)):
    udata = RepositoryUData(session).list()
    return udata
