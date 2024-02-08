def number_check(number):
    if number > 10:
        print("Greater than 10 ")

    elif number < 10:
        print("less then 10")

    else:
        print("equal then 10")



number_check(10)
number_check(11)
number_check(0)

# LOOPS -----------DÖNGÜLER#
#for loop
#Burada döngüler sayesinde iterasyon yaparak her elemanbu-ı tek tek çağırmak
#yerine tek bir döngü ile tüm elemanlarda iterasyınyapabiliriz

student = ["İsmail", "Ahmet", "Mustafa", "Melih", "Bahrain"]

def student_names():
    for i in student:
        print(i)

def add_students():
    print("Lütfen eklemek istediğiniz isim veya isismleri giriniz. Sonlandırmak için (q) harfine basınız")
    deger=True
    while(deger):
        name = input("isim giriniz:")
        student.append(name.upper())
        if name == "q":
            student.remove("q")
            deger = False

student_names()
add_students()


salarys = [1000, 2000, 3000, 6000, 7500]

def new_salary(salary, rate):
    return salary * rate/100 + salary

for salary in salarys:
    print(int(new_salary(salary , 10)))


salarys2 = [10100, 20100, 30010, 60100, 71500]

for salary in salarys2:
    print(int(new_salary(salary , 15)))
#Burada da  hazır olark yazılna fonksiyon ile istediğimiz herhangi bir listedeki değerleri
# çok kolay bir şekilde değiştirebiliriz.



for salary in salarys:
    if salary <= 3000:
        print(int(new_salary(salary, 10)))
    else:
        print(int(new_salary(salary, 15)))














