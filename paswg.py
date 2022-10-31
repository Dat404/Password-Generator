import random


def simple_generate(*args):
    smb = '0123456789'
    res = [random.choice(smb) for i in range(0,3)]
    return ''.join(res)

def get_password(leng = 8):
    smb = 'abcdefghijklmnopqrstuvwxyz0123456789!()$%?'
    if leng > 64:
        leng = 64
    return ''.join(random.sample(smb + smb.upper(), leng))

def password_secure(pasw): ...


if __name__ == '__main__':
    fst = simple_generate()
    snd = get_password(999)
    print(f'simple_generate = {fst} \nget_password = {snd}')