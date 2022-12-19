#Bessone Elisa      classe 5BROB

#input valori 
def input_valori():
    p = int(input("Inserisci p> "))
    q = int(input("Inserisci q> "))
    e = int(input("Inserisci e> "))
    m = int(input("Inserisci m> "))
    return p, q, e, m

#genero n, la chiave pubblica
def generoN(p, q):
    return (p*q)

def calcolophi(p,q):
    return ((p-1)*(q-1))

def equazioneDiofantea(e, phi, n):            #(e, phi, n):
    div, mod= divmod(e,phi)
    if mod == 0:
        return ([0, n/phi])
    else:
        sol = equazioneDiofantea(phi,mod,n)
        u = sol[0]
        v=sol[1]
        return ([v,u-div * v])
    """if a <= 0 or b <= 0:
        raise Exception("Arguments must be positive")

    # In the algorithm a > b, otherwise just swap the coefficients
    if a < b:
        d, alpha, beta = equazioneDiofantea(b, a)
        return d, beta, alpha

    prec = (a, 1, 0)
    curr = (b, 0, 1)

    while curr[0] > 0:
        pprec = prec
        prec = curr
        div = pprec[0] // prec[0]
        # https://ilprofalberto.github.io/sistemicrypto/#/8
        curr = (pprec[0] % prec[0], pprec[1] - div * prec[1], pprec[2] - div * prec[2])

    return prec"""

def cifro_decifro(m, d, n):
    acc = 1
    print(f"D: {d}")
    while d > 0:
        if d % 2 == 1:
            acc = (acc*m) % n
        m = (m * m) % n
        d = d // 2  
    return acc
    #return (m**d)%n     #metodo con utilizzo di potenza



def main():
    p, q, e, m = input_valori()
    n = generoN(p, q)
    phi = calcolophi(p, q)
    print(f"phi: {phi}")
    
    m_cifrato = cifro_decifro(m, e, n)
    print(f"Messaggio cifrato>> {m_cifrato}")    

    d = equazioneDiofantea(e, phi, n)
    print(f"Equazione diofantea{d}")

    if d[0] < 0:
        d[0] = d[0] + phi



    m_decifrato = cifro_decifro(m_cifrato, d[0], n)
    print(f"Messaggio decifrato>> {m_decifrato}")

    


if __name__ == "__main__":
    main()
