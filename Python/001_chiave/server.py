#Bessone Elisa      classe 5BROB

import random
from socket import AF_INET, SOCK_STREAM, socket
import config
BUFFER_SIZE = 1024
HOST = '0.0.0.0'  
PORT = 5000
from common import modexp, encode_big, decode_big, dh

SERVER = ("0.0.0.0", 5000)

def chatServer():
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind((SERVER))
        s.listen()
        connessione, _ = s.accept()       
        gab = dh(connessione)
        print(f"GAB calcolato --> {gab}")


            
if __name__ == "__main__":
    chatServer()
    
