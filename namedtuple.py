from collections import namedtuple


# # 1
# Student = namedtuple("User", ["name", "age", "group"])

# ism = input("Ism: ")
# yosh = int(input("Yosh : "))
# guruh = input("Guruh : ")

# user1 = Student(ism, yosh, guruh)
# print(user1._asdict())



# # 2
# Book = namedtuple("Book", ["title", "author", "year"])
# b = Book("O'tkan kunlar", "Abdulla Qodiriy", 1920)
# print(b.author)




# # 3
# Point = namedtuple("Point", ['x' , 'y'])
# A = Point(2, 4)
# print(A.x)
# print(A.y)




# # 4
# Car = namedtuple("Car", ["brand", "model", "year"])
# c1 = Car("Chevrolet", "Cobalt", 2025)
# print(c1.brand, c1.model, c1.year)



# # 5
# Student = namedtuple("Student", ["name", "age", "score"])
# students = [
#     Student("Azizillo", 19, 80),
#     Student("Ali", 20, 95),
#     Student("Vali", 21, 88),
#     Student("Sardor", 18, 76),
#     Student("Jasur", 22, 91)
# ]

# maks = max(students, key = lambda x: x.score)
# print(maks._asdict())





# # 6
# Product = namedtuple('Product', ['name', 'price', 'quantity'])

# mahsulotlar_royxati = [
#     Product("Noutbuk", 800, 3),
#     Product("Telefon", 400, 5),
#     Product("Sichqoncha", 15, 10),
#     Product("Klaviatura", 25, 4),
#     Product("Monitor", 150, 2)
# ]
# new = list(map(lambda x: (x.name, x.price * x.quantity), mahsulotlar_royxati))
# print(new)



# # 7
# Employee = namedtuple("Employee", ["name", "salary"])

# e1 = Employee("Azizilll", 2000)
# e2 = e1._replace(salary = e1.salary * 1.2)
# print(e2)




# 8
# City = namedtuple('City', ['name', 'population'])

# shaharlar_royxati = [
#     City("Toshkent", 3000000),
#     City("Samarqand", 550000),
#     City("Buxoro", 280000),
#     City("Andijon", 450000),
#     City("Namangan", 65000),
#     City("Farg'ona", 300000),
#     City("Nukus", 330000),
#     City("Qarshi", 27000),
#     City("Urganch", 200000),
#     City("Termiz", 19000)
# ]

# new = list(filter(lambda x: x.population > 100000, shaharlar_royxati))
# for i in new:
#     print(i)




# # 9
# Student = namedtuple('Student', ['name', 'faculty', 'gpa'])

# talabalar_royxati = [
#     Student("Asadbek", "IT", 3.8),
#     Student("Zilola", "Economics", 3.6),
#     Student("Bekzod", "Medicine", 3.4),
#     Student("Madina", "IT", 3.9),
#     Student("Diyor", "Economics", 3.2),
#     Student("Jasur", "Medicine", 3.7),
#     Student("Shahnoza", "IT", 3.5),
#     Student("Olimjon", "Economics", 3.9),
#     Student("Guli", "Medicine", 3.1),
#     Student("Sardor", "IT", 3.2),
#     Student("Farrux", "Economics", 3.5),
#     Student("Dina", "Medicine", 3.8),
#     Student("Aziz", "IT", 3.7),
#     Student("Lola", "Economics", 3.4),
#     Student("Rustam", "Medicine", 3.3),
#     Student("Malika", "IT", 4.0),
#     Student("Siroj", "Economics", 3.8),
#     Student("Laylo", "Medicine", 3.6),
#     Student("Otabek", "IT", 3.1),
#     Student("Yulduz", "Economics", 3.7)
# ]




# # 10
# from collections import namedtuple

# Order = namedtuple('Order', ['order_id', 'customer', 'amount'])

# buyurtmalar_royxati = [
#     Order(1, "Azizillo", 1200000),
#     Order(2, "Ali", 450000),
#     Order(3, "Vali", 1500000),
#     Order(4, "Sardor", 300000),
#     Order(5, "Jasur", 2500000),
#     Order(6, "Zilola", 850000),
#     Order(7, "Madina", 1100000),
#     Order(8, "Diyor", 950000),
#     Order(9, "Shahnoza", 150000),
#     Order(10, "Olimjon", 3500000),
#     Order(11, "Azizillo", 600000),
#     Order(12, "Ali", 1250000),
#     Order(13, "Guli", 700000),
#     Order(14, "Sardor", 1800000),
#     Order(15, "Jasur", 90000),
#     Order(16, "Farrux", 2100000),
#     Order(17, "Dina", 400000),
#     Order(18, "Lola", 1350000),
#     Order(19, "Rustam", 800000),
#     Order(20, "Malika", 3100000),
#     Order(21, "Azizillo", 950000),
#     Order(22, "Siroj", 1700000),
#     Order(23, "Laylo", 2300000),
#     Order(24, "Otabek", 500000),
#     Order(25, "Yulduz", 1050000),
#     Order(26, "Ali", 300000),
#     Order(27, "Vali", 120000),
#     Order(28, "Sardor", 4100000),
#     Order(29, "Jasur", 650000),
#     Order(30, "Zilola", 1400000),
#     Order(31, "Madina", 200000),
#     Order(32, "Diyor", 1900000),
#     Order(33, "Shahnoza", 850000),
#     Order(34, "Olimjon", 1200000),
#     Order(35, "Guli", 2600000),
#     Order(36, "Farrux", 750000),
#     Order(37, "Dina", 1150000),
#     Order(38, "Lola", 450000),
#     Order(39, "Rustam", 2200000),
#     Order(40, "Malika", 600000),
#     Order(41, "Siroj", 1300000),
#     Order(42, "Laylo", 900000),
#     Order(43, "Otabek", 3400000),
#     Order(44, "Yulduz", 150000),
#     Order(45, "Azizillo", 1850000),
#     Order(46, "Ali", 550000),
#     Order(47, "Vali", 2400000),
#     Order(48, "Sardor", 700000),
#     Order(49, "Jasur", 1650000),
#     Order(50, "Zilola", 3200000)
# ]


# max_order = max(buyurtmalar_royxati, key = lambda x: x.amount)
# min_order = min(buyurtmalar_royxati, key = lambda x: x.amount)
# than_1m = list(filter(lambda x: x.amount > 1000000, buyurtmalar_royxati))


# print(max_order)
# print(min_order)
# print(f"1 mln so'mdan yuqori bo'lgan buyurtmalar soni : {len(than_1m)}")









# 11 Bonus masala
Student = namedtuple('Student', ['id', 'name', 'age', 'score'])


talabalar_royxati = [
    Student(1, "Azizillo", 19, 85),
    Student(2, "Ali", 20, 95),
    Student(3, "Vali", 21, 78),
    Student(4, "Sardor", 18, 64),
    Student(5, "Jasur", 22, 91),
    Student(6, "Zilola", 19, 88),
    Student(7, "Madina", 20, 72),
    Student(8, "Diyor", 21, 55),
    Student(9, "Shahnoza", 19, 98),
    Student(10, "Olimjon", 23, 82),
    Student(11, "Guli", 18, 90),
    Student(12, "Farrux", 22, 67),
    Student(13, "Dina", 20, 74),
    Student(14, "Lola", 21, 89),
    Student(15, "Rustam", 19, 61),
    Student(16, "Malika", 20, 93),
    Student(17, "Siroj", 22, 76),
    Student(18, "Laylo", 18, 83),
    Student(19, "Otabek", 21, 50),
    Student(20, "Yulduz", 19, 87),
    Student(21, "Asadbek", 20, 79),
    Student(22, "Sevara", 21, 92),
    Student(23, "Dilshod", 22, 68),
    Student(24, "Kamola", 18, 81),
    Student(25, "Bobur", 23, 73),
    Student(26, "Nodira", 19, 96),
    Student(27, "Temur", 20, 58),
    Student(28, "Nargiza", 21, 84),
    Student(29, "Umida", 18, 70),
    Student(30, "Shaxzod", 22, 94),
    Student(31, "Zuhra", 20, 63),
    Student(32, "Anvar", 19, 77),
    Student(33, "Eldor", 21, 86),
    Student(34, "Iroda", 22, 52),
    Student(35, "Sunnat", 18, 99),
    Student(36, "Roxat", 20, 65),
    Student(37, "Akmal", 21, 71),
    Student(38, "Nilufar", 19, 80),
    Student(39, "Sardor", 22, 88),
    Student(40, "Aziza", 20, 75),
    Student(41, "Javohir", 18, 92),
    Student(42, "Zarina", 21, 60),
    Student(43, "Murod", 23, 84),
    Student(44, "Gozal", 19, 79),
    Student(45, "Mirzo", 22, 97),
    Student(46, "Rano", 20, 54),
    Student(47, "Xurshid", 18, 82),
    Student(48, "Sitora", 21, 66),
    Student(49, "Abror", 19, 73),
    Student(50, "Komil", 22, 89)
]


sorted_talabalar = sorted(talabalar_royxati, key = lambda x : x.score, reverse = True)


# 1-shart
for i in sorted_talabalar:
    print(i)

# 2-shart
print(sorted_talabalar[:10])

# 3-shart
yig = 0
for i in talabalar_royxati:
    yig += i.score
ortacha = int(format(yig/len(talabalar_royxati), ".0f"))
print(f"O'rtacha ball : {ortacha}")

# 4-shart
than_ortacha = list(filter(lambda x: int(x.score) > ortacha, talabalar_royxati))
for i in than_ortacha:
    print(i)





