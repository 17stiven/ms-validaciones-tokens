from flask import Flask
import os

from flask import request
from jose import jwt



app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/crear-token")
def crear():
    
        nombre=request.args.get("nombre")
        idp=request.args.get("id")
        id_rol=request.args.get("id_rol")
       
        
       
        try:
            secret_key=os.environ.get("JWT_SECRET_KEY")
            token = jwt.encode({'nombre': nombre, 'id':idp, 'rol': id_rol}, secret_key, algorithm='HS256')
            
            print("enviado")
            
            return {"response":"ok", "token":token}
        except Exception as e:
            print(e.message)
            return {"response":"ko", "token":""}
   
        
        
        
@app.route("/validar-token")
def validar():
 
        token=request.args.get("token")
     
        
        
      
        try:
            secret_key=os.environ.get("JWT_SECRET_KEY")
            jwt.decode(token, secret_key, algorithms=['HS256'])
            
            return "ok"
        except Exception as e:
            print(e.message)
            return "ko"
   
    


if __name__== '__main__':
    app.run(host='localhost', port=5001)
