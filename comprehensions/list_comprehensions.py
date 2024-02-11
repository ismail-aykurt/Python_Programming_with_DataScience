# Python'daki comprehension'lar, listeler, sözlükler (dictionary) ve kümeler (set) gibi veri yapılarını oluşturmak
# veya dönüştürmek için kullanılan kısa ve okunabilir bir dil yapısıdır. Bu yapılar, genellikle tek satırda ifade
# edilir ve bir döngü ve bir koşul ifadesi içerebilir.

salaries = [1000, 2000, 3000, 4000]


def new_salary(x):
    return x * 20 / 100 + x


for salary in salaries:
    print(new_salary(salary))

null_list = []
for salary in salaries:
    null_list.append(new_salary(salary))

# Yukarıda her bir durum için ayrı ayrı loopslaer oluşturduk ve içine kodlarımızı yazdık ancak bu işlemlerin aynısını
# tek satırda da gerçekleştirebiliriz. Hem kod okunurşuğu artar hemde daha sistemli bir şekilde yürümüş olur.

[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]

# Mesela bir döngü ile maaşları iki ile çarpıp ekrana yazdıralım

list_comp = [salary * 2 for salary in salaries]

# şimdi de maaşları 3000 den küçük olanlara bir işlem yaptıralım

list_comp1 = [salary * 2 for salary in salaries if salary < 3000]
# Şimdi buradaa dikkat edilmesi gereken şey eğer biz bir conditions kullanacaksak ve bu sadece if ten olursa if en
# sağa yazılır

# Peki şimdi de maaşı 3000 den küçükse ne yapmalıyız işte burda da else kullanırız ancak dikkat dediğim gibi eğer else
# de kullanılırsa bu sefer if en sağda değil aşağıda oldugu gibi sola yazılır

list_comp2 = [int(salary * 0) if salary < 3000 else int(salary) for salary in salaries]

list_comp3 = [int(new_salary(salary * 2)) if salary < 3000 else int(new_salary(salary * 0.2)) for salary in salaries]

# -----------------------------------------------------------------------------------------------------------------
# Mesela burada da elimzde bir tane liste olsun burda istediğim öğrencileri bir listeye istemediklerimi de bir listeye
# alayım

students = ["İsmail", "Ahmet", "Mustafa", "Hilmi", "Elemsu"]
students_no = ["Ahmet", "Mustafa"]

list_comp4 = [student.lower() if student in students_no else student.upper() for student in students]
# Mesela burda da bir döngü oluştur daha sonra içine conditionsşarı gir de karşılaştır da ekle de bir sürü kod satırı
# gerek yok burda comprehensionsları kullanarrak tek satırda tüm işlemleri halledebiliriz.

list_comp5 = [student.lower() if student not in students_no else student.upper() for student in students]

