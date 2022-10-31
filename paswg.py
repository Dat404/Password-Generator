import random


def simple_generate(*args):
    smb = '0123456789'
    res = [random.choice(smb) for i in range(0,3)]
    return ''.join(res)

def password(leng = 8):
    smb = 'abcdefghijklmnopqrstuvwxyz0123456789!()$%?'
    if leng > 64:
        leng = 64
    return ''.join(random.sample(smb + smb.upper(), leng))

def password_secure(pasw): ...



n = mega_password(64)
print(n)


    