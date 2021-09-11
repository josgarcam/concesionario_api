# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 18:13:45 2021

@author: jmgar
"""

from models import Coches, Matriculas
from app import db


#Obtiene los coches de la bbdd que cumplen con el criterio de filtrado
def get_filtro_coches(marca, modelo):
     
    coches= Coches.query.filter_by(coc_marca=marca, coc_modelo=modelo) 
    
    data = {}
    i = 0
    
    for coche in coches:
        data[i] = { 'id': coche.coc_id,
                    'marca': coche.coc_marca,
                   'modelo':coche.coc_modelo,
                   'cilindrada': coche.coc_cilindrada,
                   'kms': coche.coc_kms,
                   'matricula': coche.coc_matricula}
        i += 1
    
    return (data)



#Obtiene los detalle de un coche, filtrando por id
def get_coches_id(id):
     
    coches= Coches.query.filter_by(coc_id=id) 
    
    data = {}
    i = 0
    
    for coche in coches:
        data[i] = { 'id': coche.coc_id,
                    'marca': coche.coc_marca,
                   'modelo':coche.coc_modelo,
                   'cilindrada': coche.coc_cilindrada,
                   'kms': coche.coc_kms,
                   'matricula': coche.coc_matricula}
        i += 1
    
    return (data)


# Obtiene todos los coches de la bbdd, sin criterios de filtrado
def get_todos_coches():
     
    coches= Coches.query.all() 
    
    data = {}
    i = 0
    
    for coche in coches:
        data[i] = { 'id': coche.coc_id,
                    'marca': coche.coc_marca,
                   'modelo':coche.coc_modelo,
                   'cilindrada': coche.coc_cilindrada,
                   'kms': coche.coc_kms,
                   'matricula': coche.coc_matricula}
        i += 1
    
    return (data)


#Obtiene los coches, junto con la info de las matriculas 
def get_todos_coches_extendida():
     
    coches = db.session.query(Coches, Matriculas).join(Coches, Matriculas.mat_numero == Coches.coc_matricula).all()
    data = {}
    i = 0
    
    for coche in coches:
        data[i] ={  'id': coche.Coches.coc_id,
                    'marca': coche.Coches.coc_marca,
                   'modelo':coche.Coches.coc_modelo,
                   'cilindrada': coche.Coches.coc_cilindrada,
                   'kms': coche.Coches.coc_kms,
                   'matricula': coche.Coches.coc_matricula,
                   'Nº bastidor': coche.Matriculas.mat_bastidor,
                   'Fecha matriculacion': coche.Matriculas.mat_fecha_mat}
        
        i += 1
    
    return (data)


############# DELETE ##########
def delete_coches(coc_id):
     
    coche = Coches.query.filter_by(coc_id=int(coc_id)).one()
    db.session.delete(coche)
    db.session.commit()
    
    return { 'id': coche.coc_id,
        'marca': coche.coc_marca,
         'modelo':coche.coc_modelo,
         'matricula': coche.coc_matricula}


def delete_filtro_coches(marca, modelo):
     
    coche= Coches.query.filter_by(coc_marca=marca, coc_modelo=modelo).one()
    
    db.session.delete(coche)
    db.session.commit()
    
    return { 'id': coche.coc_id,
        'marca': coche.coc_marca,
          'modelo':coche.coc_modelo,
          'matricula': coche.coc_matricula}

############# ADD ##########
def add_coche(marca, modelo, cilindrada, kms, matricula):
       
    coche = Coches()
    
    coche.coc_marca = marca
    coche.coc_modelo = modelo
    coche.coc_cilindrada = cilindrada
    coche.coc_kms = kms
    coche.coc_matricula= matricula
    
    db.session.add(coche)
    db.session.commit()
    
    return { 'id': coche.coc_id,
        'marca': coche.coc_marca,
         'modelo':coche.coc_modelo,
         'matricula': coche.coc_matricula} 

############# UPDATE ##########
def update_coche(id, marca, modelo, cilindrada, kms, matricula):
    
    coche = Coches.query.get_or_404(id)
    
    coche.coc_marca = marca
    coche.coc_modelo = modelo
    coche.coc_cilindrada = cilindrada
    coche.coc_kms = kms
    coche.coc_matricula= matricula
    
    db.session.add(coche)
    db.session.commit()
    
    return { 'id': coche.coc_id,
        'marca': coche.coc_marca,
         'modelo':coche.coc_modelo,
         'matricula': coche.coc_matricula} 







