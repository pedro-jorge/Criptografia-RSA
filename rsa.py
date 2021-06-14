from random import randrange

codigos_para_simbolos = {111: '0', 112: '1', 113: '2', 114: '3', 115: '4',
116: '5', 117: '6', 118: '7', 119: '8', 121: '9', 122: '=', 123: '+',
124: '-', 125: '/', 126: '*', 127: 'a', 128: 'b', 129: 'c', 131: 'd',
132: 'e', 133: 'f', 134: 'g', 135: 'h', 136: 'i', 137: 'j', 138: 'k',
139: 'l', 141: 'm', 142: 'n', 143: 'o', 144: 'p', 145: 'q', 146: 'r',
147: 's', 148: 't', 149: 'u', 151: 'v', 152: 'w', 153: 'x', 154: 'y',
155: 'z', 156: 'á', 157: 'à', 158: 'â', 159: 'ã', 161: 'é', 162: 'ê',
163: 'í', 164: 'ó', 165: 'ô', 166: 'õ', 167: 'ú', 168: 'ç', 169: 'A',
171: 'B', 172: 'C', 173: 'D', 174: 'E', 175: 'F', 176: 'G', 177: 'H',
178: 'I', 179: 'J', 181: 'K', 182: 'L', 183: 'M', 184: 'N', 185: 'O',
186: 'P', 187: 'Q', 188: 'R', 189: 'S', 191: 'T', 192: 'U', 193: 'V',
194: 'W', 195: 'X', 196: 'Y', 197: 'Z', 198: 'Á', 199: 'À', 211: 'Â',
212: 'Ã', 213: 'É', 214: 'Ê', 215: 'Í', 216: 'Ó', 217: 'Ô', 218: 'Õ',
219: 'Ú', 221: 'Ç', 222: ',', 223: '.', 224: '!', 225: '?', 226: ';',
227: ':', 228: '_', 229: '(', 231: ')', 232: '"', 233: '#', 234: '$',
235: '%', 236: '@', 237: ' ', 238: '\n'}

simbolos_para_codigos = {'0': 111, '1': 112, '2': 113, '3': 114, '4': 115,
'5': 116, '6': 117, '7': 118, '8': 119, '9': 121, '=': 122, '+': 123,
'-': 124, '/': 125, '*': 126, 'a': 127, 'b': 128, 'c': 129, 'd': 131,
'e': 132, 'f': 133, 'g': 134, 'h': 135, 'i': 136, 'j': 137, 'k': 138,
'l': 139, 'm': 141, 'n': 142, 'o': 143, 'p': 144, 'q': 145, 'r': 146,
's': 147, 't': 148, 'u': 149, 'v': 151, 'w': 152, 'x': 153, 'y': 154,
'z': 155, 'á': 156, 'à': 157, 'â': 158, 'ã': 159, 'é': 161, 'ê': 162,
'í': 163, 'ó': 164, 'ô': 165, 'õ': 166, 'ú': 167, 'ç': 168, 'A': 169,
'B': 171, 'C': 172, 'D': 173, 'E': 174, 'F': 175, 'G': 176, 'H': 177,
'I': 178, 'J': 179, 'K': 181, 'L': 182, 'M': 183, 'N': 184, 'O': 185,
'P': 186, 'Q': 187, 'R': 188, 'S': 189, 'T': 191, 'U': 192, 'V': 193,
'W': 194, 'X': 195, 'Y': 196, 'Z': 197, 'Á': 198, 'À': 199, 'Â': 211,
'Ã': 212, 'É': 213, 'Ê': 214, 'Í': 215, 'Ó': 216, 'Ô': 217, 'Õ': 218,
'Ú': 219, 'Ç': 221, ',': 222, '.': 223, '!': 224, '?': 225, ';': 226,
':': 227, '_': 228, '(': 229, ')': 231, '"': 232, '#': 233, '$': 234,
'%': 235, '@': 236, ' ': 237, '\n': 238}

def do_miller_rabin_test(b, n):
    k, q = 0, n-1
    while q % 2 == 0:
        k+=1
        q//=2
    
    r = pow(b,q,n)

    if r==1 or r==n-1:
        return True
    
    i = 0

    while True:
        r = pow(r,2,n)
        i+=1

        if r==1 or i==k:
            return False

        if r==n-1:
            return True
    

def do_euclid_extended(a, b):
    x_, y_ = 1, 0
    x, y = 0, 1
    D, d = a, b

    while d != 0:
        q, r = divmod(D, d)
        
        x_, x = x, (x_ - q*x)
        y_, y = y, (y_ - q*y)
        D, d = d, r
    
    return D, x_, y_

def generate_prime_number(n):
    min = pow(10, n)+1
    max = pow(10, n+2)-1
    isProbablyPrime = False 

    while True:
        p = randrange(min, max, 2)

        for _ in range(10):
            b = randrange(2, p-2)
            isProbablyPrime = do_miller_rabin_test(b, p)

            if not isProbablyPrime:
                break 

        if isProbablyPrime:
            return p

def generate_keys(k):
    p, q = generate_prime_number(k), generate_prime_number(k)
    n = p*q
    phi = (p-1)*(q-1)
    e, d = 3, 0

    inverse_p, inverse_q = 0, 0 # inverso de p mod q, inverso de q mod p
    d_mod_p, d_mod_q = 0, 0

    while True:
        gcd, d, _ = do_euclid_extended(e, phi)

        if gcd == 1:
            break
            
        e+=2
    
    _, inverse_p, _ = do_euclid_extended(p, q) # calculando inverso de p mod q
    _, inverse_q , _ = do_euclid_extended(q, p) # calculando inverso de q mod p
    
    d%=phi
    d_mod_p = d%(p-1) # nao sei se é isso
    d_mod_q = d%(q-1) # nao sei se é isso


    keys = {
        'n': n,
        'p': p,
        'q': q,
        'phi': phi,
        'e': e,
        'd': d,
        'd_mod_p': d_mod_p,
        'd_mod_q': d_mod_q,
        'inverse_p_mod_q': inverse_p,
        'inverse_q_mod_p': inverse_q
    }



    return keys

def encrypt(texto, n, e):
    texto_em_numeros = ''
    tamanho_bloco = int(len(str(n)))-1

    for letra in texto:
        texto_em_numeros += str(simbolos_para_codigos[letra])

    mensagem_em_blocos = [texto_em_numeros[i:i+tamanho_bloco] for i in range(0, len(texto_em_numeros), tamanho_bloco)]
    blocos_encriptados = []

    for bloco in mensagem_em_blocos:
        blocos_encriptados.append(pow(int(bloco), e, n))
    
    return blocos_encriptados

def decrypt(blocos, n, d, keys={}):
    mensagem_em_blocos = []
    texto_em_numeros = ''
    texto = ''

    if keys != {}:
        d_mod_p = keys['d_mod_p']
        d_mod_q = keys['d_mod_q']
        p_ = keys['inverse_p_mod_q']
        q_ = keys['inverse_q_mod_p']
        p = keys['p']
        q = keys['q']
        n = keys['n']

    if keys == {}: # se nao foi especificado chaves adicionais além de n e d, entramos aqui
        for bloco in blocos:
            mensagem_em_blocos.append(pow(bloco, d, n))

    else: # utilizando o teorema chines dos restos
        for bloco in blocos:
            m1 = pow(bloco, d_mod_p, p)
            m2 = pow(bloco, d_mod_q, q)
            h = (q_ * (m1-m2)) % p
            m = m2 + h * q
            mensagem_em_blocos.append(m)

    for bloco in mensagem_em_blocos:
        texto_em_numeros += str(bloco)
    
    for i in range(0, len(texto_em_numeros), 3):
        texto += codigos_para_simbolos[int(texto_em_numeros[i:i+3])]
    
    return texto

k = 50 # primes size
keys = generate_keys(k)
n, e, d = keys["n"], keys["e"], keys["d"]

msg_enc = encrypt('Thanks for coming here :)', n, e)
msg_des = decrypt(msg_enc, n, d, keys)

print(msg_enc)
print(msg_des)