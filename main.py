import random

storage = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
zapros = int(input("Введите длину пароль"))
parol = ""
for i in range(zapros):
    parol += random.choice(storage)
print(parol)