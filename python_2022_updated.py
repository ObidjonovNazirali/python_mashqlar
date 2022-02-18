# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 18:48:56 2022

@author: grem
"""
# quidagi kod hello world jumlasini konsolga chiqaradi
# print("salom dunyo, yoki hello world")
# print(23+24) #bu matematik amal hisoblanadi shuning uchun buni ehtiyotkorlik bila qarash kerak
# print('men "dell" markali computer sotib oldim, vachaaaach')
# print(" men \"dell\" markali computer sotib oldim va judayam xursandman")
# print(""" bugun sening kuning,
#       kuning bugun sening, do'stim sancho""")
# print('salom qalesilar  \ishlar yaxshimi')

# print(15/4)
# print(15//4)

# print(15/3)
# print(2**4)
# print(3**3)
# 
# ism="abdulloh"
# dost="nodir"
# print(dost)
# ism="abror"
# yosh="34"
# print("mening do'stimning ismi", ism, "va u", yosh, "yoshda")
# a=3
# b=4
# c=(a*b)**3
# print(c)
# radius = 5
# pi = 3.14159
# aylana_yuzi = pi * radius**2
# print("Radiusi" , radius, "ga teng aylananing yuzi=", aylana_yuzi)

# ism="ahad"
# familya="qayum"
# print(ism+" "+familya)

# ism='nazir'
# familya='obidjonov'
# print(f"mening  ismim {ism}, va mening familyam esa {familya}")

# print('hello world')
# print('hello \t world')
# print("hello \n world")

# ism="james"
# familiya="bond"
# ism_familiya=f"{ism} {familiya}"
# print(ism_familiya.upper())
# ism_sharif= ism_familiya.upper()
# print(ism_sharif.lower())
# print(ism_sharif.title())
# print(ism_sharif.capitalize())

# meva='    olma  '
# # print(meva)
# # print(meva.lstrip())
# # print(meva.rstrip())
# # print(meva.strip())
# print(f"men {meva.lstrip()} ni yaxshi koraman")

# #INPUT
# shahar=input("qaysi shahardansiz?")
# print("qalesilar "+ shahar + "liklar")

# ism=input("ismingiz nima?")
# print("assalom alaykum  "+ ism.title())

# a=23
# b=45
# temp=45.6
# print(type(a))
# aholi_soni=7_456_456_234
# print("yer sharidagi aholi soni",aholi_soni,"ga teng")

# d,f,g=2,3,4
# k=d*f
# print(k)

# radius=20
# PI=3.14159
# diametr=radius*2
# print("aylananing uzunligi = ", PI*diametr)

# ism='jobir'
# yosh=34
# xabar= ism + " "+ str(yosh) +" yoshda"
# print(xabar)

# t_yil=int(input('tug\'ilgan yilingiz qachon?'))
# yosh=2022-t_yil
# print("demak, siz "+ str(yosh)+" yoshda ekansiz")

# son=input("istalgan son kiriting \n>>>")
# son_kv=int(son)**2
# son_kb=int(son)**3
# print(f"{son} sonining kvadrati {son_kv} ga teng")
# print(f"{son} sonining kubi {son_kb}ga teng")
# print(son, " sonining kvadrati ", int(son)**2, "ga teng")

# yosh=input("yoshingiz nechida? \n >>>")
# t_yil=2022-int(yosh)
# print(f"siz {t_yil} yiilda tug\'ilgansiz.")

# a=int(input("birinchi sonni kiriting: \n >>>"))
# b=int(input("ikkinchi sonni kiriting: \n >>>"))
# print(f"birinchi va ikkinchi sonlarning yig'indisi {a+b} ga teng")
# print(f"birinchi va ikkinchi sonlarning ko'paytmasi {a*b} ga teng")


# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
# sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
# ismlar = [] # bo'sh ro'yxat

# mevalar=['nok', 'olma', 'anor','tarvuz', 'apelsin']
# # print(mevalar)
# # print("birinchi meva bu - ", mevalar[0])
# # print("ikkinchi meva bu- ", mevalar[1])
# # print(mevalar.insert(2,"qovoq"))
# # print(mevalar)
# # mevalar.append('shaftoli')
# # print(mevalar)
# # mevalar.pop()
# # print(mevalar)
# # del mevalar[3]
# print(mevalar)
# print(mevalar.lower())
# print(mevalar.title())

# narhlar = [12000, 18000, 10900, 22000]
# # narhlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
# # narhlar[2] = 11000 # 3-qiymatni 11000 ga o'zgartiramiz
# # narhlar[3] = narhlar[3]+2000 # 4-qiymatga 2000 qo'shamiz
# # print(narhlar)
# # narhlar[3]=23333
# # narhlar[2]=narhlar[0]+4555
# # print(narhlar)
# narhlar.remove(12000)
# print(narhlar)

# ismlar=['abror','muhammad','nodir','mirzali']
# print(f"salom {ismlar[0]},ishlar yaxshimi?")
# print("assalom alaykum "+ismlar[1]+" bugun choyxona bormi?")
# print('salom ',ismlar[3], 'nimalar qiltasin')

# cars=['nexia','damas','malibu', 'tiko','tucker']
# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# print(cars)

# mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
# print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
# print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)

# print(sorted(mehmonlar, reverse=True))

# sonlar = list(range(0,10)) # 
# print(sonlar)

# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# my_cars = cars[0:6:2] # 0-indeskdan boshlab 3 ta element ajratib olamiz
# print(my_cars)

# davlatlar=['korea','china','usa','russia','uzbek','german']
# print(davlatlar)
# print(len(davlatlar))
# print(sorted(davlatlar))
# print(sorted(davlatlar,reverse=True))
# print(davlatlar)
# davlatlar.reverse()
# print(davlatlar)
# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)

# sonlar=list(range(120,1201,2))
# print(sum(sonlar))
# print(max(sonlar)-min(sonlar))
# print(len(sonlar))
# print(sonlar[:20], sonlar[-21:], sonlar[450:470])

# taomlar=['osh','shurva','mastava','manti', 'kabob']
# print(taomlar)
# nonushta=taomlar[:]
# print(nonushta)
# nonushta.remove('shurva')
# nonushta.pop(-1)
# print(nonushta)
# nonushta.insert(2,'shashlik')
# nonushta.append('non')
# print(nonushta)
# print(taomlar)
# nonushta=tuple(nonushta)
# nonushta[0]='osh va non'

# mehmonlar=['ali','vali','hasan','husan','nodir']
# # for mehmon in mehmonlar:
# #     print(mehmon)
# for mehmon in mehmonlar:
#     print(f"hurmatl {mehmon} siz 23 fevral kuni nahorgi oshga taklif etamiz")
#     print("hurmat bilan, falonchiyevlar oilasi")

# sonlar=list(range(1,11))
# for son in sonlar:
#     print(f"{son}ning kvadrati {son**2}ga teng")
    

# sonlar=list(range(11))
# son_kvadrati=[]
# for son in sonlar:
#     son_kvadrati.append(son**2)
# print(sonlar)
# print(son_kvadrati)

# dostlar=[]
# print("5ta eng yaqin do'stingiz ismini kiriting")
# for n in range(5):
#     dostlar.append(input(f"{n+1}-do'stingiz ismini kiriting  "))
# print(dostlar)




# ismlar=['nodir','nazir','jasur','islom','bilol']
# for ism in ismlar:
#     print(f'{ism} qalesan, yuripsami?')
# print(f"Kod {len(ismlar)} marta takrorlandi")

# t_sonlar=list(range(11,100,2))
# t_sonlarkubi=[]
# for son in t_sonlar:
#     t_sonlarkubi.append(son**3)
# print(t_sonlar)
# print(t_sonlarkubi)


# kinolar=[]
# print("5ta eng sevimli kinolaringiz qaysi?")
# for k in range(5):
#     kinolar.append(input(f"{k+1}-kino:"))
# print(kinolar)


# odamlar=[]
# son=input('bugun necha kishi bilan uchrashdingiz?')
# for k in range(int(son)):
#     odamlar.append(input(f"{k+1}-kishini ismini kiriting "))
# print("siz bugun uvhrashgan odamlar yo\'yhati: ",odamlar )

# ism=input('ismingiz nima? \n>>>')
# if ism.lower()!="ali":
#     print(f"uzur {ism.title()}, biz Alini kutayotgan edik")
# else:
#     print("salom Ali")











# javob=float(input("12*6 nechida teng?\n >>> "))
# if javob != 72:
#     print("javob xato")
# else:
#     print("siz to'g'ri topdingiz")

# yosh=int(input("yoshingiz nechida? \n>>> "))
# if yosh>=18:
#     print("kirorilar")
# else:
#     print("sizi yoshiz kichgina ekan, kirolmaysiz, uzur")


# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car == 'gm': print("GM")
#     else: print(car.title())

# for car in cars:
#     if car != 'gm': print(car.title())
#     else: print("GM")

# login=input("loginni kiriting \n>>> ")
# if login.lower() == 'admin':
#     print("Hush kelibsiz, ADMIN, Foydalanuvchilar ro'yhatini korasizmi?")
# else: print(f"Hush kelibsiz,{login.title()}")

# a=int(input("birinchi sonni kiriting: \n>>> "))
# b=int(input("ikkinchi sonni kiriting: \n>>> "))
# if a==b: print("ikkala son teng ekan")
# elif a>b: print("A B dan kata ekan")
# else: print("B Adan katta ekan")



# son=int(input("istalgan sonni  kiriting:\n >>>"))
# if son>0: print("son musbat ekan")
# elif son<0: print("son manfiy ekan")
# else: print("eee kallavaram bu son nolku!!!!")

# raqam=int(input("istalgan sonni kiriting:\n >>>"))
# if raqam>0: print(raqam**0.5)
# else: print("musbat son kiriting")

# son=int(input("iltimos, juft son kiritng:\n>>>"))
# if son%2 == 0: print("rahmat")
# else: print("bu juft son emas, adashdiz shekili")

# yosh=int(input("iltimos yoshingizni kiriting: \n>>>"))

# if yosh<4 or yosh>=60: 
#     narx=0
#     print("sizga krish bepul")
# elif yosh<18:
#   narx=10000
# else: 
#   narx=20000
# print(f"sizga chipta narxi {narx} sum")


# a=int(input("birinchi sonni kiriting:"))
# b=int(input("ikkinchi sonni kiriting:"))
# if a>b: print(f"{a} {b} dan katta")
# elif a<b:print(f"{a} {b}dan kichkina")
# else: print('a va b teng')

# mahsulotlar=["osh",'shorva','mastava',"shashlik","norin",'manti','somsa',"olma", "tarvuz","salad"]
# savat=[]
# for n in range(5):
#     savat.append(input(f"{n+1} - ni taomni tanlang"))

# for taom in savat:
#     if taom in mahsulotlar:
#         print("bu taom bizda bor")
#     else: print("kechirasiz bu taom bizda yoq")

# print(savat)



# mahsulotlar=["osh",'shorva','mastava',"shashlik","norin",'manti','somsa',"olma", "tarvuz","salad"]
# savat=[]

# for n in range(5):
#     savat.append(input(f"{n+1}- taomni tanlang"))
# for taom in savat:
#     if taom in mahsulotlar:
#         print("bu taom bizda bor, buyurtm qabul qilindi")
#     else: 
#         savat.remove(taom)
#         print("bu taom bizda yoq")
    

# mahsulotlar=['tarvuz',"tuz","cola","olma","fanta","saryog","ruchka","piyola",
#              "shashlik","non",'choy']


# savat=[]
# for n in range(5):
#     savat.append(input(f"{n+1}-taomni kiriting"))
# mavjud_emas=[]
# mavjud=[]

# for taom in savat:
#     if taom in mahsulotlar:
#        mavjud.append(taom) 
#     else: mavjud_emas.append(taom)

# if mavjud_emas:
#     print("bizda quyidagi taomlar yo'q: ")
#     for taom in mavjud_emas:
#         print(taom)
# else: print("bizda hamma mahsulotlar bor")

# foydalanuvchilar=['1111','abror97','nazir97','nodir97','salom97']
# login=input("ynagi login kiriting: \n>>>")
# if login in foydalanuvchilar:
#     print("uzur aka, bunday login band ekan, boshqa tanlay qoling")
# else: print("eee hush kelibsiz, login qulluq bolsin")








# son=int(input('butun son kiriting: \n>>>'))
# sonlar=[]
# for n in range(2,11):
#     if son%n==0: 
#         print(f"{son}soni {n} ga qoldiqsiz bolinadi")

# otam={'t_yil':1972, "ismi":"Safarali", 'manzil':'Andijon'}
# print(f' Otamning ismi {otam["ismi"]},\n va {otam["t_yil"]} -yil {otam["manzil"]}da tugilgan')


# taom={'nodir':'osh', 'abror':"salad",'mirzali':'olma',"avaz":"somsa","nazir":"cola"}
# print(f"Nodirning sevimi taomi {taom['nodir']}")
# print(f"Abrorning sevimli taomi {taom['abror']}")
# print(f"Mirzalining sevimli taomi {taom['mirzali']}")

# python_dic={'integer':'butun son','float':'o\'nli son', 'string':'matn','if':'agar'}
# # print(python_dic['integer'])
# # print(python_dic['float'])
# soz=input('birorta soz kiriting: ')
# if soz in python_dic[key]:
#     print(python_dic[value])


# kalit = input("Kalit so'z kiriting:").lower()
# tarjima = python_dic.get(kalit)
# if tarjima==None:
#     print("Bunday so'z mavjud emas")
# else:
#     print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")

# talaba_0={'ism':'nazirali','familya':'obidjonov',
#           'yosh':'25', 
#           'fan':'iqtisod'}

# print(talaba_0)
# print(talaba_0.keys())
# print(talaba_0.values())

# for key, value in talaba_0.items():
#     print(f" kalitlar: {key}")
#     print(f"qiymatlar: {value}")
    

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }
# for k,q in telefonlar.items():
#     print(f"{k}ning telefoni {q}")


# mahsulotlar = { # Do'kondagi mahsulotlar
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }
# # print(mahsulotlar.keys())

# print("do'kondagi mahsulotlar quyidagilar:")
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())
# print("narxlar esa quyidagicha")
# for narx in mahsulotlar.values():
#     print(narx)


# bozorlik = ['anor','uzum','non','baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot} narxi {mahsulotlar[mahsulot]}")

# for buyum in bozorlik:
#     if  buyum not in mahsulotlar:
#         print(f"iltimos, do'koningizga {buyum} ni olib keling ")
        
# print("do'konimizdagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar.keys()):
#     print(mahsulot.title())


# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }

# print(telefonlar.values())

# print("Foydalanuvhcilar quyidagi telefonlarni ishlatishadi: ")
# for tel in telefonlar.values():
#     print(tel.title())

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'hamida':'galaxy s9',
#     'maryam':'huawei p30',
#     'tohir':'iphone x',
#     'umar':'iphone x'    
#     }
# print("foydalanuvhcilar quyidagi telefonlarni ishlatishadi: ")
# for tel in sorted(telefonlar.values()):
#     print(tel.title())
# print("buyer bosh bolishi kerak edi")
# for tel in set(telefonlar.values()):
#     print(tel.title())


# lugat={'apple':'olma', 'car':'moshina','phone':'telefon','juice':'sharbat',
#        'pen':'ruchka','notebook':'daftar', 'mouse':'sichqon','table':'stol',
#        'sun':'quyosh','moon':'oy'}
# for k, l in lugat.items():
#     print(f"{k}- {l}")

# davlatlar={'uzbekistan':'tashkent','qazaqstan':'astana','korea':'seoul',
#            'china':'bejiing','usa':'washington','germany':'berlin','russia':'moscow',
#            'turkey':'anqara'}
# # for k in sorted(davlatlar.keys()):
# #     print(k.title())
# # print('             ')
# # for l in sorted(davlatlar.values()):
# #     print(l.title())

# davlat=input("istalgan davlat nomini kriting: \n>>>")
# if davlat in davlatlar:
#     print(davlatlar[davlat])
# else: print('uzr aka, bizda bunday davlat nomi yoq edida omalekin')




# taomnoma={'osh':1000,'shorva':1100,'mastava':1200,'norin':1300,'qazi':2000,
#           'non':2100,'lagmon':3400,'shashlik':2300}
# print("restoranimizga xush kelibsiz")
# buyurtma =[]
# for n in range(3):
#       buyurtma.append(input(f"{n+1}- taomni tanlang: \n>>>").lower())

# for taom in buyurtma: 
#     if taom in taomnoma:
#        print(f"{taom} narxi {taomnoma[taom]} so'm")
#     else: print(f"bizda  {taom} yoq ekan, uzur omale")
                     

                                      
# menu = {
#         'osh':20000,
#         "lag'mon":22000,
#         'non':4000,
#         'choy':5000,
#         'shashlik':12000,
#         'somsa':6000,
#         'tabaka':15000
#         }

# print('3 ta taom buyurtma bering.')
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1}-taom:").lower())

# for buyurtma in buyurtmalar:
#     if buyurtma in menu:
#         print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
#     else:
#         print(f"Kechirasiz, bizda {buyurtma} yo'q.")

# ali=['familiya':'valiyev',
#            'tyil':1995,
#            'malumot':'oliy',
#            'tillar':['python','c++']]

# nodir= {'ismt':'Nodirbek Xotamtoyev','tyil':1997,'tjoy':'nayman', 'boy':180}

# donyor= {'ismt':'Donyor Ahmedov','tyil':1998,'tjoy':'noray','boy':179}

# abror= {'ismt':'Abror Kamolov','tyil':1996,'tjoy':'noray','boy':175}

# avaz= {'ismt':'Avazek Yunusov','tyil':1999,'tjoy':'oqkoprik','boy':175}

# # mirzali= {'ismt':'Mirzali Obidjonov','tyil':1995,'tjoy':'oqbosh','boy':170}

# dostlar=[nodir, donyor, abror, avaz]
# for dost in dostlar:
#     ism = dost['ismt']
#     tyil=dost['tyil']
#     tjoy=dost['tjoy']
#     boy=dost['boy']
    
# print(f"{ism.title()} {tyil}-yil {tjoy}da tug\'ilgan. bo\'yi {boy}santimetr")

# print(dostlar)



# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro'
#            }

# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent'
#            }

# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona"
#            }

# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot"
#            }

# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     tyil = shaxs['tyil']
#     vyil = shaxs['vyil']
#     tjoy = shaxs['tjoy']
#     print(f"{ism} {tyil}-yilda {tjoy}da tavallud topgan. "
#           f"{vyil-tyil} yil umr ko'rgan.")


# kinolar={'nodir':['jumong','jangbogo','spiderman'],
#          'abror':['shumbola','suyunchi','yoryor'],
#          'avaz':['tangem','abdulhamid','esmeralda']}

# for k,l in kinolar.items():
#     print(f"\n {k.title()} bu kinolarni yaxshi koradi: ")
#     for kino in l:
#         print(kino)


# ism=input('ismingiz nima? ')
# yosh=input(f"salom {ism.title()}, yoshingiz nechida?")
# height=float(input(f" {ism.title()}, yoshingizni bilib oldik, endi boyingizni kiriting: \n>>>"))

# 


# son=1
# while son<=5:
#     print(son, end=' ')
#     son=son+1
# print('dastur tugadi')


# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print("dastur tugadi")


# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)




# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True: # abadiy tsikl
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break # tsiklni to'xtatish
#     else:
#         print(float(qiymat)**2)


# sonlar=list(range(1,11))
# for son in sonlar:
#     if son ==5:
#         break
#     else: print(f"{son}ning kvadrati = {son**2}")



# sonlar=list(range(1,11))
# for son in sonlar:
#     if son ==5:
#         continue
#     else: print(f"{son}ning kvadrati = {son**2}")

# son =0
# while son<10:
#     son+=1
#     if son%2 !=0:
#         continue
#     else: print(son)

# print("yaqin dostlaringiz ro'yhatini tuzamiz")
# ismlar=[]
# n=1
# while True:
#     savol=f"{n}-yaqin do'stingizni ismini kiriting: "
#     ism=input(savol)
#     ismlar.append(ism)
#     n+=1
#     takrorlash=input("yana ism kiritasizmi? ha/yo'q ")
#     if takrorlash != 'ha':
#         print("rahmat, sog' bo'ling")
#         break
    
# print("do'stlaringiz ro'yhati :")
# for ism in ismlar:
#     print(ism)
      
    
    
    
# print("do'stlaringiz ismi va yoshini kiriting: ")   
# dostlar={}  
# ishora =True
# while ishora:
#     dost=input("Dostingizni ismini kiriting: ")
#     yosh=int(input(F"{dost.title()}ning yoshini kiriting: "))
#     dostlar[dost]=yosh
#     takrorlash= input("yana malumot kiritasizmi? ha/yo'q ")
#     if takrorlash != 'ha':
#         ishora=False
# for dost, yosh in dostlar.items():
#     if dost.lower()=='abror':
#         print(f"{dost.title()} bechora bolapaqir hali yoshda, endigina {yosh}ga kirdi")
#     else: print(f"{dost.title()}ning yoshi {yosh}da")
    
    
    
# talabalar = ['hasan', 'husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = baho  
    

               # #Amaliyot
# print("Buyurtma berishingiz mumkin ")
# buyurtmalar=[]
# n=1
# while True:
#     taom=input(f"{n}- ovqatni tanlang: ")
#     buyurtmalar.append(taom)
#     n+=1
#     savol=input("yana ovqat tanlaysizmi?  ha/yoq ")
#     if savol != 'ha':
#           break
# print(buyurtmalar)
  
# print('ebozor uchun mahsulot va narxini kiritamiz: ')   
# ebozor={}
# ishora=True
# n=1
# while ishora:
#     mahsulot=input(f"{n}-mahsulot nomini kiriting : ")
#     narx=input(f"{mahsulot} narxini kiriting: ")
#     ebozor[mahsulot]=int(narx)
#     n+=1
#     if n==5:
#         break    
# print(ebozor) 
# print(buyurtmalar)
# for taom in buyurtmalar:
#     if taom in ebozor:
#         print(ebozor[taom])
#     else: print("kechirasiz, bu taom bizda yoq ekan ")

    ##AMALIYOT
# def tyiltop(ism, yosh):
#     """ bu funksiya, tugulgan yilni hisoblaydi"""
#     print(f"{ism.title()} {2022-int(yosh)}da tugilgan ")
# tyiltop("nodir", 23)
# tyiltop("donyor",24)   
# tyiltop("abror", 34)    
    
    
# def kvkubtop(son):
#     """bu funksiya sonning kvadrati va kubini hisoblaydi"""
#     print(f"{son} sonining kvadrati {son**2} ga teng")
#     print(f"{son} sonining kubi esa {son**3}g teng")
# kvkubtop(34)  
# kvkubtop(45)
    

# def juft_toq (son):
#     """bu funksiya sonning juft yoki toq ekanligini tekshiradi"""
#     if son%2==0:
#         print(f"{son} soni juft sondir. ")
#     else: print(f"{son} soni toq son ekan")
# juft_toq(56)
   
    
# def kattani_chiqar(son1,son2):
#     if son1>son2: print(f"{son1} soni {son2} sonidan katta")
#     elif son1<son2: print(f"{son2} soni {son1} sonidan katta")
#     else: print(f" {son1} va {son2} sonlari tengdir")
# kattani_chiqar(23,12)
# kattani_chiqar(12,12)    
# kattani_chiqar(23,25)    


# def daraja_top(x,y=3):
#     print(f"{x} sonining {y}-darajasi {x**y} ga teg")
# daraja_top(23)
# daraja_top(12,4)
  
# sonlar=[] 
# def qoldiqtop(x):
#     for y in range(2,11):
#         if x%y==0:
#             print(y)
#         else: print(f"{x} soni {y}ga qoldiqsiz bolinmas ekan")
# qoldiqtop(34)
     
    
    
    
    
# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto 
    
     
# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting",end='')
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
    
#     #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#     #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
#     # Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no': 
#         break
    
    
    
    ### AMALIYOT
# def shaxs_haqida( ismi,familiyasi,t_yili, t_joyi, email='',t_raqami=''):
#     shaxs={"ismi":ismi,
#            "familiyasi":familiyasi,
#            "t_yili":t_yili,
#            "yoshi":2022-t_yili,
#            "t_joyi":t_joyi,
#            "email":email,
#            "t_raqami":t_raqami}
#     return shaxs 
    
# shaxs1=shaxs_haqida('nodir', 'xotamtoyev', 1997, 'nayman', 'nodir@gmail.com',
#                     200398129)  
# shaxs2=shaxs_haqida('abror','kamolov',1998,'nayman','abror@gmail.com',
#                    2223456)
# print(shaxs1)
# print(shaxs2)
    
    
    
# def mijoz_info(ism, familiya, tyil, tjoy, email='',tel=None):
#     """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     mijoz = {'ism':ism,
#              'familiya':familiya,
#              'tyil':tyil,
#              'yoshi':2020-tyil,
#              'tjoy':tjoy,
#              'email':email,
#              'telefon':tel}
#     return mijoz

# print("Mijoz haqida ma'lumotlarni kiriting.")
# mijozlar =[]
# while True:
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")
#     tyil = int(input("Tug'ilgan yili: "))
#     tjoy = input("Tug'ilgan joyi: ")
#     email = input("Email: ")
#     telefon = input("Telefon raqami: ")
#     mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
#     javob = input("Davom etasizmi? (ha/yo'q)")
#     if javob!='ha':
#         break

# print("Mijozlar:")
# for mijoz in mijozlar:
#     print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()}," 
#           f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}")
    
    
    
# def katta_top(x,y,z):
#   if x>y and y>z:
#       return x
#   elif x<y>z:
#       return y
#   else: return z
  
# print(katta_top(1,2,3))

    
    
# def aylana_info(x):
#     aylana={"radiusi":x,
#                  "diametri":x*2,
#                  "uzunligi":x*2*3.14,
#                  "yuzi":(x**2)*3.14}
#     return aylana
# aylana1=aylana_info(4)
# print(aylana1)
    

# def tub_son(min,max):
#     t_sonlar=[]
#     while True:
#        for son in range(min,max):
#           if son%1=0 and son%son==0 or son==1:
#               continue
#           else:t_sonlar.append(son)
#           return t_sonlar
         
# tub_son(1,34)  
# print(t_sonlar)  
    
    
# def fibonacci(n):
#     sonlar=[]
#     for son in range(n):
#         if son==0:
#             continue
#         elif son==1:
#             sonlar.append(1)
#         else: sonlar.append((son-1)+(son-2))
#     return sonlar

# sonlar1=fibonacci(15) 
# print(sonlar1)

   
# def katta_harf(matnlar):
#     matnlar1=[]
#     for matn in matnlar:
#         matnlar1.append(matn.title())
#     return matnlar1
# ismlar=['nodir','abror','mirzali','avaz','azamat']  
# matnlar1=katta_harf(ismlar[:])
# print(matnlar1)     

    


    
    
    
    
    
    
# def bahola(ismlar):
#     baholar = {}
#     for ism in ismlar:
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(baholar)    
    


# def multiply(*sonlar):
#     kopaytma=1
#     for n in sonlar:
#         kopaytma*=n
#     return kopaytma

# print(multiply(2,3,4,5))
        
    
# def talaba_info(ism, familiya,**boshqa):
   
#     return boshqa
# talaba1=talaba_info("nodir","xotamtoyev", tyili=1997, tjoyi="nayman", holati="uylanmagan")
# talaba2=talaba_info('abror','kamolov', tyili=1998, tjoyi='noray')

import random as r

my_pets = ['alfred', 'tabitha', 'william', 'arla']

uppered_pets = list(map(str.upper, my_pets))

print(uppered_pets)
  