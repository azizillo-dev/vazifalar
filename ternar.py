# 1-masala
n = int(input("n = "))
print("juft" if n % 2 == 0 else "toq")

# 2-masala
n = int(input("n = "))
print("musbat" if n > 0 else "manfiy" if n < 0 else "nol")

# 3-masala
yosh = int(input("yosh = "))
print("voyaga yetmagan" if yosh < 18 else "voyaga yetgan")

# 4-masala
a = int(input("a = "))
b = int(input("b = "))
print(a if a > b else b) 

# 5-masala
username = input("username = ")
print("admin" if username == "admin" else "foydalanuvchi")

#6-masala
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

print(a if a > b and a > c else b if b > a and b > c else c)


#7-masala
grade = int(input("grade = "))
print("passsed" if grade >= 60 else "failed")

#8-masala
price = int(input("price = "))
discount = 1.1 if price > 100000 else 1
print(price * discount)



# 9-masala
yil = int(input("yil = "))
print("kabisa" if yil % 4 == 0 else "kabisa emas")


# 10-masala
password = input("password = ")
print("strong" if len(password) >= 8 else "weak")


# 11-masala
a = int(input("a = "))
b = int(input("b = "))

min_num = a if a <= b else b
max_num = b if a <= b else a

print(f"Kichigi  {min_num}")
print(f"Kattasi  {max_num}")


# 12-masala
baho = int(input("baho = "))
print("A" if baho >= 90 else "B" if baho < 90 and baho >= 80 else "C" if baho < 80 and baho >= 70 else "D" if baho < 70 and baho >= 60 else "F")


# 13-masala
n = int(input("n = "))
print("musbat" if n > 0 else "manfiy" if n < 0 else "nol")


# 14-masala
a = int(input("a = "))
b = int(input("b = "))

print((a if a > b else b) if (a % 2 == 0 and b % 2 == 0) else "Juft son topilmadi")


# 15-masala
price = int(input("price = "))
discount = 1.2 if price > 500000 else price > 200000 and price <= 500000 if 1.1 else 1
print(price * discount)


















































