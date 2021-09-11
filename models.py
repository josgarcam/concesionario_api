# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 19:50:21 2021

@author: jmgar
"""
from sqlalchemy  import Column, Integer, String, Date
from app import db

class Coches(db.Model):
    __tablename__ = 'coches'

    coc_id = Column(Integer, primary_key=True)
    coc_marca = Column(String)
    coc_modelo = Column(String)
    coc_cilindrada = Column(Integer)
    coc_kms = Column(Integer)
    coc_matricula = Column(String)
    
    
class Matriculas(db.Model):
    __tablename__ = 'matriculas'

    mat_id = Column(Integer)
    mat_numero = Column(String, primary_key=True)
    mat_fecha_mat = Column(Date)
    mat_bastidor = Column(Integer)
    
    
    
    
    
    
    