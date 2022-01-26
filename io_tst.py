import string 
import random 
""" WRITE YOUR OWN CORRECT CODE TO TEST THE OUTPUT """

def to_str(num: int):
    return f"{num}\n"

def random_case_string(s: str):
    res = ''
    for letter in s:
        choice = random.randint(1, 3)
        if choice == 1:
            res += letter.lower()
        elif choice == 2:
            res += letter.lower()
        else:
            res += random.choice(string.ascii_uppercase)
    return res 

def generate_random_string(length: int):
    s = ''.join(random.choices(string.ascii_uppercase + string.digits, k = length))  
    random_cased = random_case_string(s)
    return s, random_cased

def main_code():
    """ RETURN THE I/O THAT IS COMPATIBLE WITH YOUR TEST """
    n = random.randint(1, 100000)
    hero, followed = generate_random_string(n)
    counter = 0
    
    for i, letter in enumerate(hero):
        if letter != followed[i]:
            counter += 1
    
    i = f"{n}\n{hero}\n{followed}"
    o = f"{counter}"

    return i, o
