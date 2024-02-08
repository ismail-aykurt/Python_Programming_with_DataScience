# Girilen metnin çift indekslerini büyük harf yapma
# örnek----------
# before: my name is ismail. i am from turkiye
# after:  My nAmE İs iSmAiL. i aM FrOm tUrkiYe

def alternating_with_enumerate(string):
    new_string = " "
    for index, strings in enumerate(string):
        if index % 2 == 0:
            new_string += strings.upper()
        else:
            new_string += strings.lower()

    print(new_string)


alternating_with_enumerate("hi my name is ismail i am learning python")
