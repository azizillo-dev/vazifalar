# # 1
# def read_lines(file_):
#     with open(file_, "r", encoding="utf-8") as file:
#         for line in file:
#             yield line

# generator = read_lines("text.txt")
# print(next(generator))
# print(next(generator))
# print(next(generator))

# for satr in generator:
#     print(satr)


# # 2
# def read_lines(file_):
#     with open(file_, "r", encoding="utf-8") as file:
#         numbers = file.read().split() 
#         for i in numbers:
#             if int(i) % 2 == 0:
#                 yield int(i) 

# generator = read_lines("numbers.txt")
# for num in generator:
#     print(num)




# # 3
# def kvadrat(file_):
#     with open(file_, "r", encoding="utf-8") as data:
#         number = data.read().split()
#         for i in number:
#             yield int(i)**2
# generator = kvadrat("nums.txt")
# for i in generator:
#     print(i)


# # 4
# def func(file_):
#     with open(file_, "r", encoding="utf-8") as file:
#         data = file.read().split()
#         for i in data:
#             if len(i) > 5:
#                 yield i

# generator = func("text.txt")
# for i in generator:
#     print(i)




# # 5
# import time
# def words(file_):
#     with open(file_, "r", encoding="utf-8") as file:
#         words = file.read().split()
#         for i in words:
#             yield i
# generator = words("words.txt")
# for i in generator:
#     time.sleep(2)
#     print(i)



# 6, 7, 8, 9  mashqlar bitta class da
import psycopg2
import time

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname = "iterator",
            user = "postgres",
            password = "CEO517984",
            port = 5432,
            host = "localhost"
        )
        self.cur = self.conn.cursor()


    # 6-mashq
    def show_users(self):
        self.cur.execute("""
            SELECT users.name FROM users
        """)
        data = self.cur.fetchall()
        for i in data:
            yield i


    # 7 - mashq
    def max_price(self):
        self.cur.execute("""
            SELECT * FROM products
            WHERE price > 10000
        """)
        data = self.cur.fetchall()
        for i in data:
            yield i


    # 8-mashq
    def get_email(self):
        self.cur.execute("""
            SELECT users.email FROM users
        """)
        data = self.cur.fetchall()
        for i in data:
            yield i



    # 9-mashq
    def longer(self):
        self.cur.execute("""
            SELECT * FROM users
            ORDER BY LENGTH(name) DESC
            LIMIT 1
        """)
        data = self.cur.fetchone()
        yield data

    
data = Database()

# 6-mashq
# generator6 = data.show_users()
# for i in generator:
#     time.sleep(2)
#     print(i)



# 7-mashq
# generator7 = data.max_price()
# for i in generator1:
#     time.sleep(1)
#     print(i)


# # 8-mashq
# generator8 = data.get_email()
# for i in generator8:
#     time.sleep(1)
#     print(i)


# # 9-mashq
# generator9 = data.longer()
# print(next(generator9))




# 10

















































