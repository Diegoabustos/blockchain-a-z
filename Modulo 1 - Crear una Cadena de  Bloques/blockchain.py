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

# Parte 2 - Minado de un BLoque de la Cadena