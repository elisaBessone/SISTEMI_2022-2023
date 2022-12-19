def mcd_esteso(a, b):
    #d = a*x +b*y
    if a < b:
        d, x, y = mcd_esteso(b, d)
        return d, y, x
    
    d = b
    dp = a
    x = 0
    y = 1
    xp = 1
    yp = 0

    while d > 0:
        dpp, xpp, ypp = dp,xp, yp
        dp, xp, yp = d, x, y
        d = dpp % dp      #mod
        di = dpp // dp     #div
        x, y = xpp - di * xp, ypp - di * yp  
    
    return dp, xp, yp

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



if __name__ == "__main__":
    p = 11
    q = 5

    n = p*q
    phi = (p-1)*(q-1)
    e = 3

    gcd, d, k = mcd_esteso(e, phi)

    if d < 0:
        d = d + phi
        k = k - e
    
    print(gcd, d, k)

    m = 2
    c = cifro_decifro(m, e, n)
    m = cifro_decifro(c, d, n)

    print(c, m)