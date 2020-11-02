#!/usr/bin/env python3                                                          
from flask import Flask, jsonify, request                                       
import json                                                                      
import threading                                                                
                                                                                
import time                                                                     
                                                                                
app = Flask(__name__)                                                           
                                                                                
NO_SQL_DB = {}                                                                  


# @app.route('/storage/<key>', methods=['GET', 'PUT', 'DELETE'])
# def handler(my_file):
#     with open(log_file,'a') as f:
#         f.write(f"{request.method} /storage/ {my_file}\n")

@app.route('/storage/<key>', methods=['GET'])                                   
def get_value(key):                                                             
    if key in NO_SQL_DB:                                                        
        return json.loads(NO_SQL_DB[key])                                       
    else:                                                                       
        return '', 404    
    
@app.route('/storage/<key>', methods=['PUT'])        
def add_value(key):                                                             
    if not request.is_json:                                                     
        return '', 400                                                          
    content=request.get_json()                                                  
    NO_SQL_DB[key] = json.dumps(content)                                        
    return '', 201                                                              
                                                                                
@app.route('/storage/<key>', methods=['DELETE'])                                
def delete_value(key):                                                          
    if key in NO_SQL_DB:                                                        
        del NO_SQL_DB[key]                                                      
    return '', 204                                                              
                                                                                                                                                       
                                                                                
if __name__ == '__main__':                                                      
    app.run(host='0.0.0.0',port=8080)