import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()



class Users(Base):
    __tablename__ = 'Users'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False)
    password = Column(String(50), nullable=False)
    active = Column(Boolean, nullable=False)

  
class Pais(Base):
    __tablename__ = 'Pais'
   
    id = Column(Integer, primary_key=True)
    nombre = Column(String(150), nullable=False) 

class Perfil(Base):
    __tablename__ = 'Perfil'
   
    id = Column(Integer, primary_key=True) 
    user_Id = Column(Integer, ForeignKey('Users.id'))
    Users = relationship(Users)    
    profesion = Column(String(150), nullable=False)
    fecha_nacimiento = Column(String(50), nullable=False)
    pais_id = Column(Integer, ForeignKey('Pais.id'))
    Pais = relationship(Pais)   
    comentario_personal =Column(String(250), nullable=False)
    foto=Column(String(250), nullable=False)
      

class Publicaciones(Base):
    __tablename__ = 'Publicaciones'
   
    id = Column(Integer, primary_key=True)
    user_Id = Column(Integer, ForeignKey('Users.id'))
    Users = relationship(Users)    
    nombrePublicacion = Column(String(250), nullable=False) 
    hashtags = Column(String(250), nullable=False) 
    imagen=Column(String(250), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')