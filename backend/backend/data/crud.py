from sqlalchemy.orm import Session
from .database import ProductResult, TrackedProducts
from ..schemas.database_schema import TrackedProducts, ProductResultSchema

def add_all_results( db: Session, results: list[ProductResultSchema]) -> None:
    product_result = [ProductResult(**result.__dict__) for result in results]
    db.add_all(product_result)
    db.commit()

def unique_search_texts(db: Session):
    return db.query(ProductResult.search_text).distinct().all()