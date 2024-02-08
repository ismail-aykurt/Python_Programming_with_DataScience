#listeler değiştriebilir sıralı ve kapsayıcıdırlar

notes=[1,2,3,3,21,45]
type(notes)
not_nam=[12,2,3, True, "a", [1,2,3]]

not_nam[1]
not_nam[4]
not_nam[5][1]

notes[0]=99

dir(notes)
len(notes)
len(not_nam)
notes.append(5)
notes
len(notes)
len(not_nam)
notes.remove(5)

notes.pop(4)
'''burada pop istenilen herhangi bir indexteki elemanı silerken remove ise istenen elemanı siler
ancak mesela biz beşi sildeceğiz 20. indexte bunu remove ile sil dersek ve 20. indeksten önce bir beş değeri varsa 
ide sadece ilk gelen beşi siler diğerlerini ellemez'''

liste2=[2,3,5,2,3,5]
liste2.remove(5)
liste2.remove(2)
#burada yanlız istenen değerin hepsini siliyor !!!!!!!!!!!!!!!!
liste2.insert(1,45)

liste3=["ismail", "memet", "ismail"]
liste3.remove("ismail")
liste4=[1,2,3,5,2]
liste4.remove(2)
