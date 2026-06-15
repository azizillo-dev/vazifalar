# 1
new = {x: x**2 for x in range(1,11)}
print(new)



# 2
names = ["Ali", "Vali", "Hasan", "Husan"]
new = {x : len(x) for x in names}
print(new)


# 3
new = {x : x**3 for x in range(1,6)}
print(new)



# 4
letters = ['a', 'b', 'c', 'd']
new = {x: ord(x) for x in letters}
for key, value in new.items():
    print(f"'{key}': {value}")




# 5
new = {x : str(x) for x in range(1, 6)}
for key, value in new.items():
    print(f"'{key}': {value}")




# 6
new = {x : x**2 for x in range(1, 21) if x % 2 == 0}
for key, value in new.items():
    print(f"'{key}': {value}")



# 7
prices = [100000, 250000, 50000, 300000]
new = { x: x * 1.2 if x > 200000 else x for x in prices}
for key, value in new.items():
    print(f"'{key}': {value}")




# 8
names = ["ali", "vali", "hasan"]
new = {x : x.title() for x in names}
for key, value in new.items():
    print(f"'{key}': {value}")



# 9
numbers = [-5, 7, -1, 12, 0, 20]
new = {x : x**2 for x in numbers if x > 0}
for key, value in new.items():
    print(f"'{key}': {value}")




# 10
word = "assalomu"
new = {}
for x in word:
    if x not in new:
        new[x] = 1
    else:
        new[x] += 1
print(new)


new = {x : word.count(x) for x in word}
for key, value in new.items():
    print(f"'{key}': {value}")



# 11
names = ["Ali", "Vali", "Hasan"]
scores = [90, 85, 70]

new = {names[i] : scores[i] for i in range(0, len(names))}
for key, value in new.items():
    print(f"'{key}': {value}")




12
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]
new = {x[0] : x[1] for x in matrix}
for key, value in new.items():
    print(f"'{key}': {value}")





# 13
new = { x: {"square": x**2, "cube": x**3} for x in range(1, 6)}
for key, value in new.items():
    print(f"'{key}': {value}")




# 14
scores = {
    "Ali": 95,
    "Vali": 72,
    "Hasan": 58
}
new = {name: ( "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F") 
    for name, score in scores.items()}
for key, value in new.items():
    print(f"'{key}': {value}")



# 15
new = {(a, b) : a * b for a in range(1, 11) for b in range(1, 11)}
for key, value in new.items():
    print(f"'{key}': {value}")





