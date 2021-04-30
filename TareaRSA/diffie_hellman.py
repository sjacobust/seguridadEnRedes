

def diffie_hellman(a, q, xa, xb):
    ya = a ** xa % q
    print("Ya = {} ^ {} mod {}".format(a, xa, q))
    yb = a ** xb % q
    print("Yb = {} ^ {} mod {}".format(a, xb, q))
    common_secret_a = yb ** xa % q
    print("Common Secret = {} ^ {} mod {}".format(ya, xa, q))
    common_secret_b = ya ** xb % q
    print("Common Secret = {} ^ {} mod {}".format(yb, xa, q))
    if common_secret_a == common_secret_b:
        print("a = {}, q = {}, xa = {}, xb = {}, ya = {}, yb = {}, common_secret = {}".format(a,q,xa,xb,ya,yb,common_secret_a))
        return common_secret_b
    return False

def calculator_dh():
    print("Ya = A^Xa mod Q")
    print("Yb = A^Xb mod Q")
    a = int(input("A = "))
    q = int(input("Q = "))
    xa = int(input("Xa = "))
    xb = int(input("Xb = "))
    diffie_hellman(a, q, xa, xb)

#diffie_hellman(10,23,512,192)
calculator_dh()