import random
import config

"""def modexp(a,b,n):
    print(f"a {a}, b {b}, n {n}")
    acc = 1
    while b > 0:
        if b % 2 == 1:
            acc = (acc*a) % n
            print(f"1ACC: {acc}")
        a = (a * a) % n
        print(f"a {a}")
        b = b // 2
        print(f"b {b}")
        print(f"ACC: {acc}")
        
    print("fine ciclo")
    return acc"""

def modexp(b, exp, m):
    res = 1
    while exp > 1:
        if exp & 1:
            res = (res * b) % m
        b = b ** 2 % m
        exp >>= 1
    return (b * res) % m

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
