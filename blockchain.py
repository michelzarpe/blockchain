# -*- coding: utf-8 -*-
"""
Created on Mon May  3 20:21:37 2021
@author: michel
"""



import datetime 
import hashlib 
import json
from flask import Flask, jsonify

#primeira parte -> criar um blockchain
class Blockchain:
    def __init__(self):
        self.chain = []
        self.createBlock(proof = 1, previous_hash='0')
    
    def createBlock(self,proof, previous_hash):
        #criando um dicionario 
        block = {'index':len(self.chain)+1,
                 'timestamp':str(datetime.datetime.now()),
                 'proof':proof,
                 'previous_hash':previous_hash}
        self.chain.append(block)
        return block
    
    #retornando o bloco anterior
    def getPreviousBlock(self):
        return self.chain[-1]
    
    #processo de mineração, achar novo nonce
    def proofOfWork(self,previous_proof):
        newProof = 1
        checkProof = False #check se a prova é correta
        while checkProof is False:
            hashOperation = hashlib.sha256(str(newProof**2-previous_proof**2).encode()).hexdigest()
            if hashOperation[:4] == '0000':
                checkProof = True
            else:
                newProof+=1
        return newProof
    
    #gera e retorna o sha256
    def hash(self,block):
        encodedBlock = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encodedBlock).hexdigest()
    
  




            
    