#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 20:54:44 2022

@author: diego
"""

# Módulo 1 Crear una Cadena de Bloques

# Para Instalar:
# Flask==0.12.2: pip install Flask==0.12.2
# Cliente HTTP Postman: https://www.getpostma.com/

# Importar las librerías
import datetime
import hashlib
import json
from flask import Flask, jsonfy

# Parte 1 - Crear la Cadena de Bloques
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
        
    def create_block(self, proof, previous_hash):
        block  = {
                'index': len(self.chain)+1,
                'timestamp': str(datetime.datetime.now()),
                'proof': proof,
                'previous_hash': previous_hash
            }
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]
    
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof= True
            else:
                new_proof += 1
        return new_proof
    
    def hash(self, block):
        encode_block  = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encode_block).hexdigest()
# Parte 2 - Minado de un BLoque de la Cadena















