# 1

def string48():
    satr = input("satrni kirit: ")
    start = satr[0]

    yangi = start

    for i in satr[1:]:
        if i == start:
            yangi +=  "."
        else:
            yangi += i
    return yangi
print(string48())





# 2
#  o'xshamadi
def string49():
    satr = input("satr : ")
    oxirgi = satr[-1]
    teskari = satr[::-1]
    yangi = oxirgi
    for harf in teskari[:-2]:
        if harf == oxirgi:
            yangi += "."
        yangi += harf
    return yangi
print(string49())


# 3
def string50():
    satr = input("Satr kiriting: ")
    sozlar = satr.split()
    teskari = sozlar[::-1]
    natija = " ".join(teskari)
    
    return natija
print("Natija:", string50())






# 4
def string51():
    satr = input("satr : ")
    sozlar = satr.split()
    new = sorted(sozlar, key = lambda x : x[0])
    natija = " ".join(new)
    return natija
print("natija: ", string51())



# 5
def string52():
    satr = input("satr : ")
    new = [i.title() for i in satr.split()]
    natija = " ".join(new)
    return natija
print("natija: ", string52())





# 6
def string53():
    satr = input("Satr : ")
    tinish_belgilari = ".,?!:;-_()\"'[]{}<>"
    soni = 0
    for belgi in satr:
        if belgi in tinish_belgilari:
            soni += 1  
            
    return soni
print("soni:", string53())




# 7

def string54():
    satr = input("satr : ")
    katta_harflar = "AZXCVBNMSDFGHJKLQWERTYUIOP"
    soni = 0
    for i in satr:
        if i in katta_harflar:
            soni += 1
    return soni
print("natija : ", string54())





# 8
def string55():
    satr = input("satr : ")
    sozlar = satr.split()

    natija = max(sozlar, key = lambda x : len(x))
    return natija
print("natija ", string55())



# 9
def string56():
    satr = input("satr : ")
    sozlar = satr.split()
    eng_qisqa = sozlar[0]
    for soz in sozlar:
        if len(soz) <= len(eng_qisqa):
            eng_qisqa = soz 
    return eng_qisqa
print("natija:", string56())



# 10
def string57():
    satr = input("satr : ")
    sozlar = satr.split()
    natija = " ".join(sozlar)
    return natija
print("natija: ", string56())




# 11
def string58():
    nom = input("Manzil : ")
    slash = nom.rfind("\\")
    nuqta = nom.find(".")
    file_name = nom[slash+1:nuqta]
    return file_name
print(string58())











