from pydantic import BaseModel
from datetime import datetime

class ProductResultSchema(BaseModel):
    id: int
    name: str
    img: str
    url: str
    price: float
    created_at: datetime
    search_text: str
    source: str

    class Config:
        from_attribute = True

class TrackedProducts(BaseModel):
    id: int
    name: str
    created_at: datetime
    tracked: bool

    class Config:
        from_attribute = True