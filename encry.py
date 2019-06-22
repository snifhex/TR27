#for python3 

def encrypt(txt, key):
    alphabets = "abcdefghijklmnopqrstuvwxyz"    
    punctuation = '! .-'
    alphabets = alphabets*key
    txt = txt.lower()
    alpha = [ord(alpha) for alpha in list(alphabets)]
    txt = ''.join([chr(alpha[alpha.index(ord(a))+key]) if a not in punctuation else a 
        for a in list(txt)])
    print(txt)
    

encrypt('hello This is sachin',2)
