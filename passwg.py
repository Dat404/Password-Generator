import random


#version - 0.2
global VAR
VAR = "abcdefghijklmnopqrstuvwxyz0123456789!()$%?"

def simple_generate():
    return "".join(random.sample("0123456789", 3))

def get_password(leng = 8) -> str:
    if leng > 64: leng = 64
    while True:
        password = ''.join(random.sample(VAR + VAR.upper(), leng))

        if "not" in password_secure(password): pass
        else:
            return password
            break

def password_secure(pasw):
    if len(pasw) < 8: return f"[0] {pasw} not save! reason: not enough lenght"
    if len((set(pasw)).intersection(set(VAR))) < 3: return f"[1] {pasw} not save! reason: not enough nums"
    if len((set(pasw)).intersection(set(VAR[:-16]))) < 5: return f"[2] {pasw} not save! reason: not enough letters"

    return pasw



if __name__ == "__main__":
    print(f"simple_generate = {simple_generate()} \nget_password = {get_password(999)} \npassword_secure1 = {get_password(8)}")
