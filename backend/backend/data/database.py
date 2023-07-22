from sqlalchemy import (Boolean, Column,
                        ForeignKey, Integer,
                        String, Float, DateTime)
from sqlalchemy.orm import relationship
from datetime import datetime

from ..main import base, connection



class ProductResult(base):
    __tablename__ = 'product_result'
    id = Column(Integer, primary_key=True)
    name = Column(String(1000))
    img = Column(String(1000))
    url = Column(String(1000))
    price = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    search_text = Column(String(255))
    source = Column(String(255))

    def __init__(self, name: str, img: str, url: str, 
                 price: float, search_text: str, 
                 source: str):
        self.name = name
        self.url = url
        self.img = img
        self.price = price
        self.search_text = search_text
        self.source = source


class TrackedProducts(base):
    __tablename__ = 'tracked_products'
    id = Column(Integer, primary_key=True)
    name = Column(String(1000))
    created_at = Column(DateTime, default=datetime.utcnow)
    tracked = Column(Boolean, default=True)

    def __init__(self, name:str, created_at:str, 
                 tracked: bool):
        self.name = name
        self.created_at = created_at
        self.tracked = tracked



base.metadata.create_all(bind=connection.get_engine)