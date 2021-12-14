import math
print("CHIFFREMENT/DECHIFFREMENT")

entree = input("FICHIER D'ENTREE: ")
sortie = input("FICHIER DE SORTIE: ")

n = 0
while not n:
    try:
        n = int(input("N = "))
    except ValueError:
        print("Ceci n'est pas un nombre entier.")

x = n
while math.gcd(x, n) != 1:
    try:
        x = int(input("E ou D = "))
    except ValueError:
        print("Ceci n'est pas un nombre entier.")

def pmod(a, p, n): #a ** p % n
    ret = 1
    while p != 0:
        if (p & 1) == 1:
            ret = (ret * a) % n
            p = p - 1
        a = (a * a) % n
        p = p // 2
    return ret

def encrypt(m):
    return pmod(m, x, n)

def encrypt_bigint(data):
    out = 0
    i = 0
    while data:
        out *= n
        m = data % n
        out += encrypt(m)
        data //= n
        i += 1
    return out
with open(entree, "rb") as f_entree:
    with open(sortie, "wb") as f_sortie:
        print("Chargement du fichier d'entree...")
        inbytes = f_entree.read()
        indata = int.from_bytes(inbytes, "little")
        length = len(inbytes)
        print("Chiffrement/dechiffrement...")
        outdata = encrypt_bigint(indata)
        print("Ecriture...")
        overflow_error = True
        while overflow_error:
            try:
                outbytes = outdata.to_bytes(length, "little")
                overflow_error = False
            except OverflowError:
                length += 1
        f_sortie.write(outbytes)
        print(outbytes)
        print("Fin de l'operation.")
