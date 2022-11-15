#Bessone Elisa      classe 5BROB

#input valori 
def input_valori():
    p = int(input("Inserisci p: "))
    q = int(input("Inserisci q: "))
    e = int(input("Inserisci e: "))
    m = int(input("Inserisci m: "))
    return p, q, e, m

#genero n, la chiave pubblica
def generoN(p, q):
    return (p*q)

def calcoloYn(p,q):
    return ((p-1)*(q-1))

def equazioneDiofantea(a, b, c):
    div, mod= divmod(a,b)
    if mod == 0:
        return ([0, c/b])
    else:
        sol = equazioneDiofantea(b,mod,c)
        u = sol[0]
        v=sol[1]
        return ([v,u-div * v])

def cifro_decifro(m, d, n):
    acc = 1
    print(f"D: {d}")
    while d > 0:
        if d % 2 == 1:
            acc = (acc*m) % n
        m = (m * m) % n
        d = d // 2  
    return acc



def main():
    p, q, e, m = input_valori()
    n = generoN(p, q)
    yN = calcoloYn(p, q)
    print(f"yN: {yN}")
    
    d = equazioneDiofantea(e, yN, 1)
    print(f"Equazione diofantea{d}")

    if d[0] < 0:
        d[0] = d[0] + yN

    m_cifrato = cifro_decifro(m, d[0], n)
    print(f"Messaggio cifrato: {m_cifrato}")

    m_decifrato = cifro_decifro(m_cifrato, d[0], n)
    print(f"Messaggio decifrato: {m_decifrato}")

    


if __name__ == "__main__":
    main()
