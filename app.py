# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 19:25:46 2021

@author: jmgar
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import config

## Instanciamos la clase Flask
app = Flask(__name__) #app es la aplicación servidor

app.config.from_object(config)
db = SQLAlchemy(app)



######### GET ##########
# @app.route('/coches', methods=['GET'])
# def coches():
#     from coche import get_todos_coches
    
#     coches = get_todos_coches()

#     return jsonify(coches), 200


# @app.route('/coches', methods=['GET'])
# def coches():
#     from coche import get_todos_coches_extendida
    
#     coches = get_todos_coches_extendida() 

#     return jsonify(coches), 200



# @app.route('/coches/<id>', methods=['GET'])
# def coches_id(id):
#     from coche import get_coches_id 
    
#     coche = get_coches_id(id)
    
#     if not coche:
#         return jsonify("Recurso NO encontrado"), 404
    
#     return jsonify(coche), 200
    
    
# @app.route('/coches', methods=['GET'])
# def coches():
#     from coche import get_filtro_coches, get_todos_coches

#     marca = request.args.get('marca')
#     modelo =  request.args.get('modelo')   
    
#     if not marca or not modelo:
#         return jsonify(get_todos_coches()), 200
#     else:    
#         return jsonify(get_filtro_coches(marca, modelo)), 200




# @app.route('/coches/', methods=['GET'])
# def filtro_coches():
#     from coche import get_filtro_coches
    
#     marca = request.args.get('marca')
#     modelo =  request.args.get('modelo')   
    
#     return jsonify(get_filtro_coches(marca, modelo))



# Funcion para filtrar, en funcion de GET o POST
# Descomentar para probar 
# def filtro_coches():
#     from coche import get_filtro_coches
    
#     if request.is_json:
#         data = request.get_json()
#         marca = data['marca']
#         modelo =  data['modelo']
        
#     else:
        
#         marca = request.args.get('marca')
#         modelo =  request.args.get('modelo') 
        
#     return jsonify(get_filtro_coches(marca, modelo))



####### DELETE #####
# @app.route('/coches/<car_id>', methods=['DELETE'])
# def elimina_coches(car_id):
#     from coche import delete_coches       
    
#     return jsonify(delete_coches(car_id))


# @app.route('/coches', methods=['DELETE'])
# def elimina_coches_filtro():
#     from coche import delete_filtro_coches

#     marca = request.args.get('marca')
#     modelo =  request.args.get('modelo')   
    
#     return jsonify(delete_filtro_coches(marca, modelo))


#################### ADD ############################
@app.route('/coches', methods=['POST'])
# def anade_coche():
#     from coche import add_coche  
    
#     data = request.get_json()
#     marca = data['marca']
#     modelo =  data['modelo']
#     cilindrada = data['cilindrada']
#     kms = data['kms']
#     matricula = data['matricula']
    
#     return jsonify(add_coche(marca, modelo, cilindrada, kms, matricula))


##################### UPDATE ###################
# @app.route('/coches/<car_id>', methods=['PUT'])
# def actualiza_coche(car_id):
#     from coche import update_coche  
    
#     data = request.get_json()
#     marca = data['marca']
#     modelo =  data['modelo']
#     cilindrada = data['cilindrada']
#     kms = data['kms']
#     matricula = data['matricula']
    
#     return jsonify(update_coche(int(car_id), marca, modelo, cilindrada, kms, matricula))

    

# TODOS LOS MÉTODOS HTTP
# @app.route('/coches', methods=['GET', 'POST'])
# def coches():
#     from coche import get_filtro_coches, get_todos_coches, add_coche
    
#     marca = request.args.get('marca')
#     modelo =  request.args.get('modelo')
    
#     if request.method == "GET":
#         if not marca or not modelo:
#             return jsonify(get_todos_coches())
#         else:    
#             return jsonify(get_filtro_coches(marca, modelo))
    
#     elif request.method == "POST":
        
#         data = request.get_json()
#         marca = data['marca']
#         modelo =  data['modelo']
#         cilindrada = data['cilindrada']
#         kms = data['kms']
#         matricula = data['matricula']
    
#         return jsonify(add_coche(marca, modelo, cilindrada, kms, matricula))
    


# @app.route('/coches/<car_id>', methods=['PUT', 'DELETE'])
# def coches_id(car_id):
#     from coche import update_coche, delete_coches
    
#     if request.method == "PUT":
        
#         data = request.get_json()
#         marca = data['marca']
#         modelo =  data['modelo']
#         cilindrada = data['cilindrada']
#         kms = data['kms']
#         matricula = data['matricula']
    
#         return jsonify(update_coche(int(car_id), marca, modelo, cilindrada, kms, matricula))
    
#     elif request.method == "DELETE":
        
#         return jsonify(delete_coches(car_id))
        
        
        

if __name__ == '__main__':
    #Inicializamos el servidor
    app.run(debug=True, port=5002) 
    
    

    
    