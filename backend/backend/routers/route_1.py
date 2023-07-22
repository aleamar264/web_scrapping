from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from ..schemas.database_schema import ProductResultSchema
from ..data.database import ProductResult, TrackedProducts
from ..data.crud import add_all_results, unique_search_texts
from sqlalchemy.orm import Session
from ..main import get_db


router = APIRouter()

@router.post('/results', status_code=200)
async def submit_results(body: list[ProductResultSchema], db: Session = Depends(get_db)):
    add_all_results(db, body)
    response = {'message': 'Received data successfully'}
    return JSONResponse(response, 200, media_type="application/json")

@router.get('/unique_search_text', status_code=200)
async def get_unique_search_texts(db: Session = Depends(get_db)):
    search = unique_search_texts(db)
    search = [text[0] for text in search]
    return JSONResponse(search, 200, media_type="application/json")