#Bessone Elisa      classe 5BROB
#creazione di una chat UDP
import random
from socket import SOCK_STREAM, socket, AF_INET
from struct import pack
import config
from common import modexp, encode_big, decode_big, dh
SERVER = ("127.0.0.1", 5000)


def mypow(a,b,n):
    return (a ** b) % n

def input_value():
    host = input("Inserisci l'indirizzo ip: ")
    port = int(input("Inserisci la porta: "))
    return host, port

def chatClient():
    #richiedo indirizzo ip, porta e nome utente
    #print("Client in esecuzione: inserire INDIRIZZO IP, il numero della PORTA e il NOME UTENTE")
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((SERVER))
        gab = dh(s)
        print(f"GAB calcolato --> {gab}")

if __name__ == '__main__':
    #host, port= input_value()

    chatClient()