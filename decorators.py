# # 1


# def my_decorator(func):
#     def wrapper():
#         print("=== START ===")
#         func()
#         print("=== END ===")
#     return wrapper

# @my_decorator
# def salom():
#     print("Salom")
# salom()



# # 2
# def show_args(func):
#     def wrapper(*args):
#         return f"Args: {args}"
#     return wrapper

# @show_args
# def add(a, b):
#     return a + b
# print(add(3, 5))





# # 3
# def get_double(func):
#     def wrapper(*args):
#         result = func(*args)
#         return result * 2
#     return wrapper
    
# @get_double
# def son():
#     return 15
# print(son())





# # 4
# data = [-5, 3, -2, 10, 7] 
# def musbat(func):
#     def wrapper(lst):
#         new = [i for i in lst if i > 0]
#         return func(new) 
#     return wrapper

# @musbat
# def hisobla(musbatlar):
#     return musbatlar

# print(hisobla(data))




# ishlamadi

# # 5
# def counter(func):
#     count = 0
#     def wrapper(*args):
#         count += 1
#         print(f"Funksiya {count} marta chaqirildi")
#         return func(*args)
#     return wrapper

# @counter
# def salomlash(ism):
#     return f"Salom, {ism}!"

# salomlash("Ali")
# salomlash("Vali")
# salomlash("Olim")




# # 6
# data = [1, 2, 3, 4, 5, 6]
# def juft(func):
#     def wrapper(lst):
#         new = [i for i in lst if i % 2 == 0]
#         return func(new)
#     return wrapper

# @juft
# def juftlar(data):
#     return data
# print(juftlar(data))





# # 7
# import time

# data = [-5, 3, 11, 15, -20, 7]

# def timer(func):
#     def wrapper(*args):
#         start = time.time()
#         result = func(*args)
#         end = time.time()
#         print(f"{end - start:.6f} sekund")
#         return result
#     return wrapper

# @timer
# def qosh(data):
#     return sum(data)

# qosh(data)




# # 8
# data = [5, 2, 8, 1]

# def sorter(func):
#     def wrapper(data):
#         new = sorted(data)
#         return func(new)
#     return wrapper

# @sorter
# def lst(data):
#     return data

# print(lst(data))



# # 9

# data = [-5, 3, 11, 15, -20, 7]
# def musbat(func):
#     def wrapper(data):
#         new = [i for i in data if i > 0]
#         return func(new)
#     return wrapper

# def than_10(func):
#     def wrapper(data):
#         new = [i for i in data if i > 10]
#         return func(new)
#     return wrapper


# @musbat
# @than_10
# def lst(data):
#     return data
# print(lst(data))





# # 10
# data = [-5, 3, 11, 15, -20, 7, 24, 56, 21, -4, -43, -22, 44]
# def musbat(func):
#     def wrapper(data):
#         new = [i for i in data if i > 0]
#         return func(new)
#     return wrapper

# def than_10(func):
#     def wrapper(data):
#         new = [i for i in data if i > 10]
#         return func(new)
#     return wrapper

# def juft(func):
#     def wrapper(data):
#         new = [i for i in data if i % 2 == 0]
#         return func(new)
#     return wrapper


# @musbat
# @than_10
# @juft
# def lst(data):
#     return data
# print(lst(data))





# # 11
# import time
# def speed_(func):
#     def wrapper(*args):
#         start = time.time()
#         result = func(*args)
#         end = time.time()
#         tt = end - start
#         if tt > 1.0:
#             print("Sekin ishlayotgan funksiya!")
#         return result
#     return wrapper

# @speed_
# def funksiya():
#     time.sleep(1.2) 
#     return "Tugadi"
# funksiya()



# # 12
# def upper(func):
#     def wrapper(*args, **kwargs):
#         new = func(*args, **kwargs)
#         if isinstance(new, str):
#             return new.upper()
#         return new
#     return wrapper

# @upper
# def salom():
#     return "assalomu alekum"
# print(salom())




# # 13


# data = [2, 34, 43,- 2, 21, 2, 34, 54,12, -32]

# def musbat(func):
#     def wrapper(data):
#         new = [i for i in data if i > 0]
#         return func(new)
#     return wrapper

# def juft(func):
#     def wrapper(data):
#         new = [i for i in data if i % 2 == 0]
#         return func(new)
#     return wrapper

# def kvadrat(func):
#     def wrapper(data):
#         new = [i**2 for i in data]
#         return func(new)
#     return wrapper


# @musbat
# @juft
# @kvadrat
# def daata(data):
#     return data
# print(daata(data))





# # 14
# import time
# def logger(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         timee = format(end - start, ".3f")

#         print(f"Funksiya: {func.__name__}")
#         print(f"Args: {args}")
#         print(f"Natija: {result}")
#         print(f"Vaqt: {timee} sekund")
#         return result
#     return wrapper

# @logger
# def qoshish(a, b):
#     return a + b
# qoshish(3, 4)





# 15





























