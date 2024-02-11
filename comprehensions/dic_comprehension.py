# Burada da bir sözlük tanımmlaması yaptık diyelim bunu her seferinde uzun uzun yazmak yerine list comprehensionsta
# oldugu gibi birden fazla satırlık kodun yaptığı bir işlemi tek satırda halledebiliririz

dictionary = {"book": "kitap",
              "computer": "bilgisayar",
              "data": "veri",
              "Artificial Intelligence": "Yapay Zeka"}
dictionary.values()
dictionary.keys()
dictionary.items()

dic1 = {k: v.capitalize() for k, v in dictionary.items()}
dic2 = {k.upper(): v.capitalize() for k, v in dictionary.items()}
dic3 = {k.upper(): v.lower() for k, v in dictionary.items()}



