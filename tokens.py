# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 08:27:20 2021

@author: user
"""

from flask import Flask
import os
from flask import request
from jose import jwt  


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World Tokens!"


@app.route("/crear-token")
def crear():
        nombre=request.args.get("nombre")
        idp=request.args.get("id")
        id_rol=request.args.get("id_rol")
        
                 
        try:
            secret_key=os.environ.get("JWT_SECRET_TOKEN")
            token = jwt.encode({'nombre': nombre, 'id':idp, 'rol': id_rol}, secret_key, algorithm='HS256')
            
            print("enviado")
            
            return token
        except Exception as e:
            print(e.message)
            return ""


@app.route("/validar-token")
def validar():
        token=request.args.get("token")  
        rol = request.args.get("rol")     
        print(rol)

        try:
            secret_key=os.environ.get("JWT_SECRET_TOKEN")
            token = jwt.decode(token, secret_key, algorithms=['HS256'])
            if(rol in token["rol"]): 
                print("ok")
                return "ok"
            else:
                print("ko")
                return "ko"
        except Exception as e:
            return ""

if __name__== '__main__':
    app.run(host="localhost", port=5001)