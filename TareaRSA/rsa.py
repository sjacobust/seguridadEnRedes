def naive_modular_inverse(a, m):
    for b in range(0, m):
        if (b * a) % m == 1:
            #print("Modular Inverse of {} % {} is {}".format(a, m, b))
            return b


def extended_euclidean_algorithm(a, b):
    if a == 0 : 
        return b, 0, 1
            
    gcd, x1, y1 = extended_euclidean_algorithm(b%a, a)

    x = y1 - (b//a) * x1
    y = x1
    return gcd, x, y

def encrypt_rsa_alg(p, q, e, m):
    # C = (M ^ e) mod N
    # 1 = e(x) mod phi(N) --> x = d
    # phi(N) = (p-1)(q-1)
    N = p*q
    print("N = (p)(q) = ({})({}) = {}".format(p, q, N))
    phi_N = (p-1)*(q-1)
    print("phi(N) = (p - 1)(q - 1) = ({} - 1)({} - 1) = {}".format(p, q, phi_N))
    d = naive_modular_inverse(e, phi_N)
    print("1 = e(x) mod phi(N) = {}(x) mod {} = {}({}) mod {}".format(e, phi_N, e, d, phi_N))
    c = m**e % N
    print('C = M^e mod N = {}^{} mod {} = {}'.format(m, e, N, c))
    print("N = {}, d = {}, C = {}".format(N, d, c))
    return c, d, N

def decrypt_rsa_alg(p, q, d, c):
    N = p*q
    phi_N = (p-1)*(q-1)
    e = naive_modular_inverse(d, phi_N)
    m = c**d % N
    print("N = {}, e = {}, M = {}".format(N, e, m))
    return c


def rsa_start():
    print("N = (p)(q)")
    print("phi(N) = (p - 1)(q - 1)")
    print("1 = e(x) mod phi(N)")
    print("C = M^e mod N")
    p = int(input("P = "))
    q = int(input("Q = "))
    e = int(input("E = "))
    m = int(input("M = "))
    encrypt_rsa_alg(p, q, e, m)

rsa_start()

