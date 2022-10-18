def potenza(x, n):
    if n<0:
        raise Exception("Errore")
    res = 0
    if n == 0:
        res = 1
    elif n % 2 == 0:
        res = potenza(x, n//2)
        res = res*res
    else:
        res = potenza(x, (n-1)//2)
        res = res*res*x
    
    return res