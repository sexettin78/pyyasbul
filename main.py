import  datetime
bu_yil=datetime.datetime.now()
suan = int(bu_yil.year)
dogumyili=int(input("Hangi yılda doğdunuz? "))
yas=suan-dogumyili
print("Siz şuan "+str(yas)+" yaşındasınız")
