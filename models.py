from db import Base
from sqlalchemy import Column,Integer,String,DateTime,Text,Float,ForeignKey 
from datetime import datetime

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    email=Column(String,index=True)
    password=Column(String)
    api_key=Column(String,index=True)
    user_name=Column(String,index=True)

class Address(Base):
    __tablename__="addresses"
    id=Column(Integer,primary_key=True,index=True)
    street=Column(String)
    city=Column(String)
    state=Column(String)
    zip_code=Column(String)
    user_id=Column(Integer,ForeignKey("users.id"))

class Order(Base):
    __tablename__="orders"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"))
    address_id=Column(Integer,ForeignKey("addresses.id"))
    order_date=Column(DateTime,default=datetime.now)
    total_amount=Column(Float)