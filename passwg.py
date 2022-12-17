import random


def simple_generate():
    return ''.join(random.sample('0123456789', 3))

def get_password(leng = 8):
    var_ = 'abcdefghijklmnopqrstuvwxyz0123456789!()$%?'
    if leng > 64:
        leng = 64
    return ''.join(random.sample(var_+var_.upper(), leng))

def password_secure(pasw): ...


if __name__ == '__main__':
    print(f'simple_generate = {simple_generate()} \nget_password = {get_password(999)}')
