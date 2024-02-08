# Girilen metnin çift indekslerini büyük harf yapma
# örnek----------
# before: my name is ismail. i am from turkiye
# after:  My nAmE İs iSmAiL. i aM FrOm tUrkiYe

def alternating(string):
    new_string = " "
    for i in range(len(string)):
        if i % 2 == 0:
            new_string += string[i].upper()
        else:
            new_string += string[i].lower()

    print(new_string)


alternating("my name is ismail i learning python")
alternating("ismail")





