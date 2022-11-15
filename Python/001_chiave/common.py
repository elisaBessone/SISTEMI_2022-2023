import random
import config

def modexp(a,b,n):
    acc = 1
    while b > 0:
        if b % 2 == 1:
            acc = (acc*a) % n
        a = (a * a) % n
        b = b // 2
        
    return acc

#number -> string -> bytes
def encode_big(num):
    return str(num).encode('utf8')

#bytes -> string -> number
def decode_big(s):
    return int(s[0].decode('utf8'))

def dh(sock):
    #GENERO NUMERO A random.
    a = random.randint(1,config.P-2)
    print(f"N RANDOM {a}")

    #INVIO NUMERO GA
    ga = modexp(config.G, a, config.P)
    sock.sendall(encode_big(ga))     #encode_big --> encode della stringa
    print(f"GA INVIATO {ga}")
    
    #RICEVO NUMERO GB
    gb = decode_big(sock.recvfrom(4096))   #--> decode della stringa    #from_bytes(1, 'big')
    print(f"GB RICEVUTO {gb}")
    
    #CALCOLO NUMERO GAB 
    gab = modexp(gb, a, config.P)
    print(f"GAB CALCOLATO {gab}")


    return gab
