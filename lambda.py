# 1-masala
c = lambda x, y: x + y
print(c(2, 4))


# 2-masala
kv = lambda x:x**2
print(kv(8))



# 3-masala
c = lambda x: "Juft" if x % 2 ==0 else "toq"
print(c(574))



# 4-masala
l = lambda x:len(x)
print(l("salom"))



# 5-masala
a = lambda x: f"Salom, {x}"
print(a("Azizillo"))



# 6-masala
data = [3, 5, 31, 7, 25, 9, 11, 32, 54, 76, 98]

sort_data = lambda x: sorted(x)
print(sort_data(data))




# 7-masala
students = {
    "Ali": 85,
    "Vali": 92,
    "Sami": 78,
    "Diyor": 90,
    "Gulnora": 88
}  

sorte = dict(sorted(students.items(), key= lambda x:x[1]))
print(sorte)




# 8-masala
ismlar = ["Azizillo", "Sardor", "Diyorbek", "Gulnora", "Sami"]
sorted_ismlar = sorted(ismlar,key = lambda x:len(x))
print(sorted_ismlar)




# 9-masala
nuqtalar = [(3, 5), (1, 2), (4, 6), (2, 3)]
sorted_nuqtalar = sorted(nuqtalar, key = lambda x:x[1])
print(sorted_nuqtalar)






# 10-masala
mahsulotlar = [("Olma", 3), ("Banan", 2), ("Apelsin", 4), ("Anor", 1)]
sorted_mahsulotlar = sorted(mahsulotlar, key = lambda x:x[1])
print(sorted_mahsulotlar)





# 11-masala
talabalar = {"Azizillo": [86, 78, 56], "Sardor": [92, 88, 95], "Diyorbek": [78, 85, 80]}
sorted_by_avg = sorted(talabalar, key = lambda x: sum(talabalar[x])/len(talabalar[x]))
print(sorted_by_avg)






# 12-masala
sonlar = [34, 235, 32, 45, 96, 395, 346, 23, 56]
sorted_sonlar = sorted(sonlar, key = lambda x: str(x)[-1])
print(sorted_sonlar)





# 13-masala(
fayllar = {"python.py": 23, "java.java": 45, "c++.cpp": 12, "javascript.js": 30}
sorted_fayllar = sorted(fayllar.items(), key = lambda x:x[1])
print(sorted_fayllar)




# 14-masala


























