from functools import reduce
# 1-masala
data = [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

new = list(map(lambda x: x *2, data))
print(new)



# 2-masala
data = [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
new = list(map(lambda x: x**2,data))
print(new)



# 3-masala
data = [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
new = list(map(lambda x: x+10,data))
print(new)


# 4-masala
data = [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
new = list(map(lambda x: str(x), data))
print(new)



# 5-masala
ismlar = ["ali", "vali", "hasan", "husan"]
new = list(map(lambda x:x.title(), ismlar))
print(new)



# 6-masala
data = [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
new = list(filter(lambda x:x % 2 ==0, data))
print(new)



# 7-masala
data = [2, 4, -5, -6, 7, -8, 9, -10, -11, -12, 13, 14, -15]
new = list(filter(lambda x: x > 0, data))
print(new)




# 8-masala
data = [34, 43, 56, 78, 90, 12, 23, 45, 67, 89]
new = list(filter(lambda x: x > 50, data))
print(new)




# 9-masala
data = ['olma', 'anor', 'uzum', 'behi', 'shaftoli', "o'rik", "gilos", "nok", "anjir", "tarvuz", "qovun", "limon", "apelsin"]
new = list(filter(lambda x:len(x) > 5, data))
print(new)




# 10-masala
data = [4, 9, 23, 56, 78, 90, 12, 23, 45, 67, 89]
new = list(filter(lambda x: x % 3 ==0, data))
print(new)


# 11-masala
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new = list(map(lambda x:x**3,data))
print(new)





# 12-masala
data = [23,32,45,67,89,12,34,56,78,90]
new = list(map(lambda x:int(str(x)[-1]),data))
print(new)




# 13-masala
data = ["Azizillo", "Ziyodillo", "Shaxzod", "Qodirali", "Umar"]
new = [(i, len(i)) for i in data]
print(new)



# 14-masala
data = [3, 22, 32,26, 45, 67, 89, 12, 34, 56, 78, 90]
new = list(map(lambda x: "Juft" if x % 2 == 0 else "Toq", data))
print(new)



# 15-masala
data = ["olma", "anor", "uzum", "behi", "shaftoli", "o'rik", "gilos", "nok", "anjir", "tarvuz", "qovun", "limon", "apelsin"]
new = list(map(lambda x:x.title(), data))
print(new)




16-masala



# 17-masala  
data = [234, 345, 456, 567, 678, 789, 890, 901, 123, 321, 432, 543, 654, 765, 876, 987]
new = list(filter(lambda x: sum(map(int, str(x))) > 10, data))
print(new)



# 18-masala
data = ["kiyik", "olma", "ikki", "qirol"]
new = list(filter(lambda x: x ==x[::-1],data))
print(new)



# 19-masala
data = [121, 321, 324, 232, 545, 421, 1221, 12344321, 23455]
new = list(filter(lambda x: int(str(x) ==str(x)[::-1]),data))
print(new)




# 20-masala
data = ["azizillo", "ziyodillo", "shaxzod", "qodirali", "umar", "olim", "umida"]
unlilar = "aeiouAEIOU"
new = list(filter(lambda x: x[0] in unlilar, data))
print(new)



# 21-masala
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new = reduce(lambda x, y: x+y, data)
print(new)













