

from aiogram import Bot, Dispatcher, executor, types


bot = Bot(token="5989178724:AAEiOYwmkGayLSMVjpD0aUDy6YGE32EZWvY")
dp = Dispatcher (bot=bot)


@dp.message_handler(commands=['start'])
async def commands(message: types.Message):
    await message.answer("Assalomu aleykum nima yordam bera olaman")

@dp.message_handler(lambda message: message.text.lower() == "1-bilet")
async def send_code(message: types.Message):
    code = '''1-savol
    ism = input("Ismingiz: ")
yosh = input("Yoshingiz: ")
print(f"Assalomu aleykum {ism}! yoshingiz {yosh}.")


2-savol
son = int(input("Iltimos, biror son kiriting: "))
if son % 2 == 0:
    print("Son juft")
else:
    print("Son toq")


3-savol

n = int(input("Iltimos, biror son kiriting (n): "))
for i in range(1, n + 1):
    print(f"{i} ning kvadrati: {i ** 2}")
    
    
4-savol
n = int(input("Iltimos, nechta son kiritmoqchisiz? (n): "))
raqamlar = []
for i in range(n):
    raqam = int(input(f"{i + 1}-sonni kiriting: "))
    raqamlar.append(raqam)
yigindi = sum(raqamlar)
print(f"Kiritilgan sonlarning yig'indisi: {yigindi}")


5-savol
def ajrat_juft_toq(raqamlar):
    juft_sonlar = []
    toq_sonlar = []
    for son in raqamlar:
        if son % 2 == 0:
            juft_sonlar.append(son)
        else:
            toq_sonlar.append(son)

    return juft_sonlar, toq_sonlar
raqamlar = list(map(int, input("Ro'yxatdagi sonlarni kiriting (bo'sh joy bilan ajratilgan): ").split()))
juft_sonlar, toq_sonlar = ajrat_juft_toq(raqamlar)
print(f"Juft sonlar: {juft_sonlar}")
print(f"Toq sonlar: {toq_sonlar}")

'''
    await message.answer(f"Mana, kod:\n\n{code}")


@dp.message_handler(lambda message: message.text.lower() =="2-bilet")
async def send_code(message: types.Message):
    code = ''' 1-savol
son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))
yigindi = son1 + son2
print(f"Ikki sonning yig'indisi: {yigindi}")

2-savol
yosh = int(input("Yoshingizni kiriting: "))
if yosh > 18:
    print("Voyaga yetgansiz")
else:
    print("Voyaga yetmagan")
    
3-savol
n = int(input("n sonini kiriting: "))
print("1 dan", n, "gacha bo'lgan juft sonlar:")
for i in range(1, n + 1):
    if i % 2 == 0:  
        print(i)
        
        
4-savol
ismlar = ["Ali", "Vali", "Anvar", "Dilnoza", "Shahnoza"]
print("Ismlar ro'yxati:")
for ism in ismlar:
    print(ism)


5-savol
def unikal_elementlar(ro'yxat):
    unikal_ro'yxat = list(set(ro'yxat))
    return unikal_ro'yxat
ro'yxat = ["Ali", "Vali", "Ali", "Dilnoza", "Vali", "Anvar"]
natija = unikal_elementlar(ro'yxat)
print("Takroriy elementlar olib tashlangan ro'yxat:")
print(natija)
'''
    await message.answer(f"Mana, kod:\n\n{code}")

@dp.message_handler(lambda message: message.text.lower() =="3-bilet")
async def send_code(message: types.Message):
    code = '''
1-savol
ism = input("Ismingizni kiriting: ")
familya = input("Familyangizni kiriting: ")
print(f"{familya} {ism}")


2-savol
son = float(input("Sonni kiriting: "))
if son > 0:
    print("Musbat son")
elif son < 0:
    print("Manfiy son")
else:
    print("Son 0 ga teng")


3-savol
n = int(input("n sonini kiriting: "))
yigindi = sum(range(1, n + 1))
print(f"1 dan {n} gacha bo'lgan sonlarning yig'indisi: {yigindi}")


4-savol
ro'yxat = [5, 12, 3, 7, 19, 1]
eng_katta_indeks = ro'yxat.index(max(ro'yxat))
print(f"Ro'yxatdagi eng katta elementning indeksi: {eng_katta_indeks}")


5-savol
def elementlar_yigindisi(ro'yxat):
    return sum(ro'yxat)
ro'yxat = [5, 12, 3, 7, 19, 1]
natija = elementlar_yigindisi(ro'yxat)
print(f"Ro'yxatdagi sonlarning yig'indisi: {natija}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")


@dp.message_handler(lambda message: message.text.lower() =="4-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
c = float(input("Uchinchi sonni kiriting: "))
o'rtacha = (a + b + c) / 3
print(f"Sonlarning o'rtacha qiymati: {o'rtacha}")


2-savol
soat = int(input("Soatni kiriting (0-24): "))
if 0 <= soat <= 12:
    print("Ertalab")
elif 13 <= soat <= 18:
    print("Kunning ikkinchi yarmi")
elif 18 < soat <= 24:
    print("Kech")
else:
    print("Noto'g'ri qiymat kiritildi")
    
    
3-savol
n = int(input("n sonini kiriting: "))
for i in range(1, n + 1):
    print(i)


4-savol
ro'yxat = [12, 3, 5, 9, 1, 15]
eng_katta = max(ro'yxat)
eng_kichik = min(ro'yxat)
print(f"Eng katta element: {eng_katta}")
print(f"Eng kichik element: {eng_kichik}")


5-savol
def musbat_sonlar_ajratish(ro'yxat):
    return [son for son in ro'yxat if son > 0]
ro'yxat = [-5, 12, -3, 7, 0, 19, -1]
musbat_sonlar = musbat_sonlar_ajratish(ro'yxat)
print(f"Musbat sonlar: {musbat_sonlar}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")

@dp.message_handler(lambda message: message.text.lower() =="5-bilet")
async def send_code(message: types.Message):
    code = '''
1-savol
matn = input("Matnni kiriting: ")
print(f"Matn uzunligi: {len(matn)}")


2-savol
son = int(input("Sonni kiriting: "))
if son % 5 == 0:
    print("Bu son 5 ga bo'linadi")
else:
    print("Bu son 5 ga bo'linmaydi")
    
    
3-savol
for i in range(1, 51):
    if i % 2 != 0:
        print(i)
        
        
4-savol
ro'yxat = [1, 2, 3, 4, 5]
yangi_ro'yxat = [x * 10 for x in ro'yxat]
print(f"10 ga ko'paytirilgan ro'yxat: {yangi_ro'yxat}")


5-savol
def birinchi_harf(matn):
    so'zlar = matn.split()
    birinchi_harf_ro'yxati = [so'z[0] for so'z in so'zlar]
    return birinchi_harf_ro'yxati
matn = input("Matnni kiriting: ")
natija = birinchi_harf(matn)
print(f"So'zlarning birinchi harflari: {natija}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")



@dp.message_handler(lambda message: message.text.lower() =="6-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
print(f"Yig'indisi: {son1 + son2}")


2-savol
kun_raqami = int(input("Kunning raqamini kiriting (1-7): "))
hafta_kunlari = {
    1: "Dushanba",
    2: "Seshanba",
    3: "Chorshanba",
    4: "Payshanba",
    5: "Juma",
    6: "Shanba",
    7: "Yakshanba"
}
print(hafta_kunlari.get(kun_raqami, "Noto'g'ri raqam kiritildi"))


3-savol
n = int(input("n sonini kiriting: "))
for i in range(1, n + 1):
    print(f"{i} ning kvadrati: {i ** 2}")
    
    
4-savol
ro'yxat = [5, 8, 12, 15, 20, 25, 30, 35, 40, 45]
print(f"Ro'yxatning oxirgi elementi: {ro'yxat[-1]}")


5-savol
def kvadrat_va_kub(ro'yxat):
    return [(x, x ** 2, x ** 3) for x in ro'yxat]
ro'yxat = [2, 3, 4, 5, 6]
natija = kvadrat_va_kub(ro'yxat)
print(f"Kvadrat va kub natijalari: {natija}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")

@dp.message_handler(lambda message: message.text.lower() =="6-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
print(f"Ko'paytmasi: {son1 * son2}")


2-savol
son = float(input("Sonni kiriting: "))
if son < 0:
    print("Manfiy son")
else:
    print("Musbat son")
    
    
3-savol
n = int(input("n sonini kiriting: "))
kopaytma = 1
for i in range(1, n + 1):
    kopaytma *= i
print(f"1 dan {n} gacha bo'lgan sonlarning ko'paytmasi: {kopaytma}")


4-savol
ro'yxat = [1, 2, 3, 4, 5]
yangi_ro'yxat = [x * 2 for x in ro'yxat]
print(f"Yangi ro'yxat: {yangi_ro'yxat}")


5-savol
def kvadratga_oshirish(ro'yxat):
    return [x ** 2 for x in ro'yxat]
ro'yxat = [2, 4, 6, 8]
yangi_ro'yxat = kvadratga_oshirish(ro'yxat)
print(f"Kvadratga oshirilgan ro'yxat: {yangi_ro'yxat}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")


@dp.message_handler(lambda message: message.text.lower() =="7-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
print(f"Ko'paytmasi: {son1 * son2}")


2-savol
son = float(input("Sonni kiriting: "))
if son < 0:
    print("Manfiy son")
else:
    print("Musbat son")
    
    
3-savol
n = int(input("n sonini kiriting: "))
kopaytma = 1
for i in range(1, n + 1):
    kopaytma *= i
print(f"1 dan {n} gacha bo'lgan sonlarning ko'paytmasi: {kopaytma}")


4-savol
ro'yxat = [1, 2, 3, 4, 5]
yangi_ro'yxat = [x * 2 for x in ro'yxat]
print(f"Yangi ro'yxat: {yangi_ro'yxat}")


5-savol
def kvadratga_oshirish(ro'yxat):
    return [x ** 2 for x in ro'yxat]
ro'yxat = [2, 4, 6, 8]
yangi_ro'yxat = kvadratga_oshirish(ro'yxat)
print(f"Kvadratga oshirilgan ro'yxat: {yangi_ro'yxat}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")


@dp.message_handler(lambda message: message.text.lower() =="8-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
son = float(input("Sonni kiriting: "))
print(f"Sonning kvadrati: {son ** 2}")


2-savol
yil = int(input("Yilni kiriting: "))
if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
    print("Bu kabisa yili")
else:
    print("Bu kabisa yili emas")
    
    
3-savol
marta = int(input("Necha marta chiqarishni xohlaysiz? "))
for _ in range(marta):
    print("Salom")
    
    
4-savol
yosh = int(input("Yoshingizni kiriting: "))
ro'yxat = [1, 2, 3, 4, 5]
natija = [x * yosh for x in ro'yxat]
print(f"Yoshingizga ko'paytirilgan ro'yxat: {natija}")


5-savol
def uchga_ko'paytirish(ro'yxat):
    return [x * 3 for x in ro'yxat]
ro'yxat = [2, 4, 6, 8]
yangi_ro'yxat = uchga_ko'paytirish(ro'yxat)
print(f"3 ga ko'paytirilgan ro'yxat: {yangi_ro'yxat}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")


@dp.message_handler(lambda message: message.text.lower() =="9-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
ism = input("Ismingizni kiriting: ")
familiya = input("Familiyangizni kiriting: ")
print(f"To'liq ism: {ism} {familiya}")


2-savol
ism = input("Ismingizni kiriting: ")
familiya = input("Familiyangizni kiriting: ")
print(f"To'liq ism: {ism} {familiya}")


3-savol
n = int(input("n sonini kiriting: "))
for i in range(1, n + 1):
    print(f"Indeks: {i}, Son: {i}")


4-savol
ro'yxat = [12, -5, 7, -3, 0, -8, 15]
manfiy_sonlar = [x for x in ro'yxat if x < 0]
print(f"Manfiy sonlar: {manfiy_sonlar}")


5-savol
def orta_arifmetik(ro'yxat):
    return sum(ro'yxat) / len(ro'yxat) if ro'yxat else 0
ro'yxat = [10, 20, 30, 40, 50]
print(f"O'rta arifmetik: {orta_arifmetik(ro'yxat)}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")


@dp.message_handler(lambda message: message.text.lower() =="10-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
uzunlik = float(input("To'rtburchakning uzunligini kiriting: "))
eni = float(input("To'rtburchakning enini kiriting: "))
print(f"To'rtburchakning yuzi: {uzunlik * eni}")


2-savol
baho = int(input("Fan bahosini kiriting: "))
if baho > 90:
    print("A'lo baho")
elif baho > 80:
    print("Yaxshi baho")
else:
    print("Baho pastroq")


3-savol
n = int(input("n sonini kiriting: "))
for i in range(1, n + 1):
    print(f"{i}-sonning kubi: {i ** 3}")
    
    
4-savol
ro'yxat = [5, 12, 43, 88, 9, 100, 34, 7]
ikki_xonalik_sonlar = [x for x in ro'yxat if 10 <= x < 100]
print(f"Ikki xonalik sonlar: {ikki_xonalik_sonlar}")


5-savol
def unikal_elementlar(ro'yxat):
    return list(set(ro'yxat))
ro'yxat = [1, 2, 3, 2, 4, 1, 5, 3, 6]
natija = unikal_elementlar(ro'yxat)
print(f"Takrorlanmas elementlar: {natija}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")


@dp.message_handler(lambda message: message.text.lower() =="11-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
a = float(input("1-tomon uzunligini kiriting: "))
b = float(input("2-tomon uzunligini kiriting: "))
c = float(input("3-tomon uzunligini kiriting: "))
perimetr = a + b + c
print(f"Uchburchakning perimetri: {perimetr}")


2-savol
son = float(input("Sonni kiriting: "))
if son > 0:
    print(f"Sonning kvadrati: {son ** 2}")
else:
    print(f"Sonning kubi: {son ** 3}")


3-savol
n = int(input("n sonini kiriting: "))
juft_yigindi = sum(i for i in range(1, n + 1) if i % 2 == 0)
print(f"Juft sonlarning yig'indisi: {juft_yigindi}")


4-savol
n = int(input("n sonini kiriting: "))
juft_yigindi = sum(i for i in range(1, n + 1) if i % 2 == 0)
print(f"Juft sonlarning yig'indisi: {juft_yigindi}")


5-savol
def boluvchilar(son):
    return [i for i in range(1, son + 1) if son % i == 0]
son = int(input("Sonni kiriting: "))
print(f"{son} ning bo'luvchilari: {boluvchilar(son)}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")


@dp.message_handler(lambda message: message.text.lower() =="12-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
c = float(input("Uchinchi sonni kiriting: "))
ortacha_arifmetik = (a + b + c) / 3
print(f"Uch sonning o'rtacha arifmetik qiymati: {ortacha_arifmetik}")


2-savol
harorat = float(input("Haroratni kiriting: "))
if harorat < 0:
    print("Muzlash harorati")
else:
    print("Issiq harorat")
    
    
3-savol
son = int(input("Sonni kiriting: "))
karraliklar = [i for i in range(1, son + 1) if son % i == 0]
print(f"{son} sonining karraliklari: {karraliklar}")


4-savol
ro'yxat = [12, 5, 8, 20, 3]
eng_kichik = min(ro'yxat)
yangi_ro'yxat = [x * eng_kichik for x in ro'yxat]
print(f"Yangi ro'yxat: {yangi_ro'yxat}")


5-savol
import math
def faktorial_ro'yxat(ro'yxat):
    return [math.factorial(x) for x in ro'yxat]
ro'yxat = [3, 4, 5]
print(f"Faktorialar: {faktorial_ro'yxat(ro'yxat)}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")

@dp.message_handler(lambda message: message.text.lower() =="13-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
yosh = 2025 - int(input("Tug'ilgan yilingizni kiriting: "))
print(f"Sizning yoshingiz: {yosh}")


2-savol
a, b = float(input("Birinchi sonni kiriting: ")), float(input("Ikkinchi sonni kiriting: "))
print(f"Eng katta son: {max(a, b)}")


3-savol
for _ in range(int(input("Nechta marta chop etishni xohlaysiz? "))):
    print("Dasturlashni o'rganaman")
    
    
4-savol
print([x for x in [12, -5, 8, -2, 0, -9] if x < 0])


5-savol
ro'yxat = [12, -5, 8, -2, 0, -9]
print(f"Eng katta son: {max(ro'yxat)}, Eng kichik son: {min(ro'yxat)}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")


@dp.message_handler(lambda message: message.text.lower() =="14-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
a, b = float(input("Birinchi sonni kiriting: ")), float(input("Ikkinchi sonni kiriting: "))
if b != 0:
    print(f"Bo'linma: {a / b}")
else:
    print("Bo'linish xatosi! Ikkinchi son nolga teng bo'lishi mumkin emas.")
    
    
2-savol
son = float(input("Sonni kiriting: "))
if son < 0:
    print(f"Sonning kubi: {son ** 3}")
else:
    print(f"Sonning kvadrati: {son ** 2}")


3-savol
n = int(input("n sonini kiriting: "))
yigindi = sum(range(1, n + 1))
print(f"1 dan {n} gacha bo'lgan sonlarning yig'indisi: {yigindi}")


4-savol
ro'yxat = [12, 6, 8, 4, 2]
print([x / 2 for x in ro'yxat])


5-savol
def juft_sonlar(start, end):
    return [x for x in range(start, end + 1) if x % 2 == 0]
start = int(input("Boshlanish sonini kiriting: "))
end = int(input("Tugash sonini kiriting: "))
print(f"Juft sonlar: {juft_sonlar(start, end)}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")


@dp.message_handler(lambda message: message.text.lower() =="15-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
son = float(input("Sonni kiriting: "))
print(f"Sonning kubi: {son ** 3}")


2-savol
soat = int(input("Soatni kiriting: "))
if 0 <= soat <= 6:
    print("Tungi vaqt")
elif 7 <= soat <= 12:
    print("Ertalab")
elif 13 <= soat <= 18:
    print("Kunduzgi vaqt")
else:
    print("Kechki vaqt")
    

3-savol
n = int(input("n sonini kiriting: "))
print([x for x in range(1, n + 1) if x % 5 == 0])


4-savol
ro'yxat = [1, 2, 3, 4, 5]
print([x**2 for x in ro'yxat])


5-savol
def takrorlanmas(ro'yxat):
    return list(set(ro'yxat))
ro'yxat = [1, 2, 2, 3, 4, 4, 5]
print(f"Takrorlanmas elementlar: {takrorlanmas(ro'yxat)}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")


@dp.message_handler(lambda message: message.text.lower() =="16-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
eni = float(input("To'rtburchakning enini kiriting: "))
boyi = float(input("To'rtburchakning bo'yini kiriting: "))
yuz = eni * boyi
print(f"To'rtburchakning yuzasi: {yuz}")


2-savol
hafta_raqami = int(input("Haftaning raqamini kiriting (1-7): "))
if hafta_raqami in [6, 7]:
    print("Dam olish kuni")
else:
    print("Ish kuni")


3-savol
n = int(input("n sonini kiriting: "))
yigindi = sum(range(1, n + 1))
print(f"1 dan {n} gacha bo'lgan sonlarning yig'indisi: {yigindi}")


4-savol
ro'yxat = [1, 2, 3, 4, 5]
print(ro'yxat[::-1])


5-savol
def kichik_son(x, y, z):
    return min(x, y, z)
x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
z = float(input("Uchinchi sonni kiriting: "))
print(f"Eng kichik son: {kichik_son(x, y, z)}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")

@dp.message_handler(lambda message: message.text.lower() =="17-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
eni = float(input("To'rtburchakning enini kiriting: "))
boyi = float(input("To'rtburchakning bo'yini kiriting: "))
perimetr = 2 * (eni + boyi)
print(f"To'rtburchakning perimetri: {perimetr}")


2-savol
son = int(input("Sonni kiriting: "))
if son % 3 == 0 and son % 5 == 0:
    print("Perfect")
else:
    print("Buzz")


3-savol
n = int(input("Sonni kiriting: "))
bo'luvchilar = [x for x in range(1, n + 1) if n % x == 0]
print(f"{n} sonining bo'luvchilari: {bo'luvchilar}")


4-savol
ro'yxat = [1, 2, 3, 4, 5]
ortacha = sum(ro'yxat) / len(ro'yxat)
print(f"Ro'yxatning o'rtacha qiymati: {ortacha}")


5-savol
def kattaligi(x, y, z):
    return max(x, y, z)
x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
z = float(input("Uchinchi sonni kiriting: "))
print(f"Eng katta son: {kattaligi(x, y, z)}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")

@dp.message_handler(lambda message: message.text.lower() =="18-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
matn1 = input("Birinchi matnni kiriting: ")
matn2 = input("Ikkinchi matnni kiriting: ")
print(f"{matn1} {matn2}")


2-savol
son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
if son1 == son2:
    print("Sonlar teng")
else:
    print("Sonlar teng emas")


3-savol
n = int(input("Sonni kiriting: "))
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)


4-savol
ro'yxat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for element in ro'yxat:
    if element % 2 == 0:
        print(element)


5-savol
def kub(son):
    return son ** 3
son = float(input("Sonni kiriting: "))
print(f"Sonning kubi: {kub(son)}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")

@dp.message_handler(lambda message: message.text.lower() =="19-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
soz = input("So'zni kiriting: ")
print(f"So'zning uzunligi: {len(soz)}")


2-savol
son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
son3 = float(input("Uchinchi sonni kiriting: "))
eng_kichik = min(son1, son2, son3)
print(f"Eng kichik son: {eng_kichik}")


3-savol
n = int(input("Sonni kiriting: "))
for i in range(1, n + 1):
    print(i)


4-savol
ro'yxat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for element in ro'yxat:
    if element % 2 == 0:
        print(element * 11)


5-savol
def elementlar_soni(ro'yxat):
    return len(ro'yxat)
ro'yxat = [1, 2, 3, 4, 5]
print(f"Ro'yxatdagi elementlar soni: {elementlar_soni(ro'yxat)}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")


@dp.message_handler(lambda message: message.text.lower() =="20-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
yosh = int(input("Yoshingizni kiriting: "))
tugilgan_yil = 2025 - yosh
print(f"Sizning tug'ilgan yilingiz: {tugilgan_yil}")


2-savol
son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
if son1 > son2:
    print(f"Sonlarning ayirmasi: {son1 - son2}")
else:
    print(f"Sonlarning yig'indisi: {son1 + son2}")


3-savol
n = int(input("Sonni kiriting: "))
juft_sonlar_yig'indi = 0
for i in range(2, n + 1, 2):
    juft_sonlar_yig'indi += i
print(f"1 dan {n} gacha bo'lgan barcha juft sonlarning yig'indisi: {juft_sonlar_yig'indi}")


4-savol
ismlar = ["Ali", "Sami", "Yulduz", "Nodira", "Kamila"]
for ism in ismlar:
    print(ism)


5-savol
def yigindi(ro'yxat):
    return sum(ro'yxat)
ro'yxat = [1, 2, 3, 4, 5]
print(f"Ro'yxatdagi elementlar yig'indisi: {yigindi(ro'yxat)}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")


@dp.message_handler(lambda message: message.text.lower() =="21-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
matn = input("Matn kiriting: ")
print(f"Matnning birinchi harfi: {matn[0]}")


2-savol
son = int(input("Sonni kiriting: "))
if son % 2 == 0 and son % 7 == 0:
    print("Bu son universal")
else:
    print("Bu son universal EMAS")


3-savol
yigindi = sum(range(1, 51))
print(f"1 dan 50 gacha bo'lgan barcha sonlarning yig'indisi: {yigindi}")


4-savol
ro'yxat = [1, 12, 123, 456, 789, 1000, 5, 99]
for son in ro'yxat:
    if 100 <= son <= 999:
        print(son)


5-savol
def juft_yoki_toq(son):
    if son % 2 == 0:
        return "Juft"
    else:
        return "Toq"
son = int(input("Son kiriting: "))
print(f"Son {juft_yoki_toq(son)}.")
'''
    await message.answer(f"Mana, kod:\n\n{code}")

@dp.message_handler(lambda message: message.text.lower() =="22-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
qoldiq = a % b
print(f"Bo'linishdan olingan qoldiq: {qoldiq}")


2-savol
yil = int(input("Yilni kiriting: "))
if yil > 2000:
    print("Bu yangi asr")
else:
    print("Bu eski asr")


3-savol
n = int(input("n sonini kiriting: "))
for i in range(2, n+1, 2):
    print(i)


4-savol
ro_yxat = [1, 2, 3, 4, 5]  # Misol ro'yxat
ro_yxat.reverse()
print(ro_yxat)


5-savol
def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)

son = int(input("Sonni kiriting: "))
print(f"{son} ning faktoriali: {faktorial(son)}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")




@dp.message_handler(lambda message: message.text.lower() =="23-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
c = int(input("Uchinchi sonni kiriting: "))
eng_katta = max(a, b, c)
print(f"Eng katta son: {eng_katta}")


2-savol
kun = int(input("Kunning raqamini kiriting (1-7): "))
if 1 <= kun <= 5:
    print("Ish kuni")
elif kun == 6 or kun == 7:
    print("Dam olish kuni")
else:
    print("Noto'g'ri raqam kiritildi.")


3-savol
son = int(input("Sonni kiriting: "))
bo'luvchilar = []
for i in range(1, son + 1):
    if son % i == 0:
        bo'luvchilar.append(i)
print(f"{son} ning bo'luvchilari: {bo'luvchilar}")


4-savol
ro_yxat = [4, 7, 1, 9, 3]
eng_kichik_element = min(ro_yxat)
eng_kichik_index = ro_yxat.index(eng_kichik_element)
print(f"Eng kichik element: {eng_kichik_element}, Uning indeksi: {eng_kichik_index}")


5-savol
def hisobla(a, b):
    ko'paytma = a * b
    yig'indi = a + b
    ayirma = a - b
    bo'linma = a / b if b != 0 else "Bo'lish mumkin emas (nolga bo'lish)"
    return ko'paytma, yig'indi, ayirma, bo'linma
a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
ko'paytma, yig'indi, ayirma, bo'linma = hisobla(a, b)
print(f"Ko'paytma: {ko'paytma}")
print(f"Yig'indi: {yig'indi}")
print(f"Ayirma: {ayirma}")
print(f"Bo'linma: {bo'linma}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")



@dp.message_handler(lambda message: message.text.lower() =="24-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
matn = input("Matn kiriting: ")
print(f"Matnning so'nggi harfi: {matn[-1]}")


2-savol
son = float(input("Son kiriting: "))
if son > 0:
    print("Musbat")
elif son == 0:
    print("Nol")
else:
    print("Manfiy")


3-savol
n = int(input("n sonini kiriting: "))
toq_sonlar_yig'indisi = 0
for i in range(1, n+1):
    if i % 2 != 0:
        toq_sonlar_yig'indisi += i
print(f"1 dan {n} gacha bo'lgan toq sonlar yig'indisi: {toq_sonlar_yig'indisi}")


4-savol
ro_yxat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
juft_sonlar = [son for son in ro_yxat if son % 2 == 0]
print(f"Juft sonlar: {juft_sonlar}")


5-savol
def juft_sonlar(ro_yxat):
    return [son for son in ro_yxat if son % 2 == 0]
ro_yxat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
juft_sonlar = juft_sonlar(ro_yxat)
print(f"Juft sonlar: {juft_sonlar}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")





@dp.message_handler(lambda message: message.text.lower() =="25-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
ayirma = son1 - son2
print(f"Sonlarning ayirmasi: {ayirma}")


2-savol
harorat = float(input("Haroratni kiriting: "))
if harorat > 100:
    print("Issiq")
elif harorat < 0:
    print("Sovuq")
else:
    print("Iloji bor")


3-savol
n = int(input("n sonini kiriting: "))
yig_indis = sum(i for i in range(5, n+1, 5))
print(f"1 dan {n} gacha bo'lgan 5 ga karrali sonlar yig'indisi: {yig_indis}")


4-savol
n = int(input("n sonini kiriting: "))
yig_indis = sum(i for i in range(5, n+1, 5))
print(f"1 dan {n} gacha bo'lgan 5 ga karrali sonlar yig'indisi: {yig_indis}")


5-savol
def toq_sonlar(ro_yxat):
    return [son for son in ro_yxat if son % 2 != 0]
ro_yxat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
toq_sonlar = toq_sonlar(ro_yxat)
print(f"Toq sonlar: {toq_sonlar}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")



@dp.message_handler(lambda message: message.text.lower() =="26-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
son = float(input("Sonni kiriting: "))
print(f"Sonning 10 barobariga oshirilgan qiymati: {son * 10}")


2-savol
son = int(input("Sonni kiriting: "))
if son % 10 == 0:
    print("Nol bilan tugaydi")
else:
    print("Nol bilan tugamaydi")


3-savol
n = int(input("n sonini kiriting: "))
yig_indi = sum(i for i in range(2, n+1, 2))
print(f"1 dan {n} gacha bo'lgan juft sonlar yig'indisi: {yig_indi}")


4-savol
ro_yxat = [1, 3, 5, 7, 9, 11, 15, 2, 6, 4]
yangi_ro_yxat = [son for son in ro_yxat if son > 5]
print(f"5 dan katta sonlar: {yangi_ro_yxat}")


5-savol
def juft_sonlar_yig_indi(ro_yxat):
    return sum(son for son in ro_yxat if son % 2 == 0)
ro_yxat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Juft sonlarning yig'indisi: {juft_sonlar_yig_indi(ro_yxat)}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")


@dp.message_handler(lambda message: message.text.lower() =="27-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
son = float(input("Sonni kiriting: "))
print(f"Sonning kubi: {son ** 3}")


2-savol
soat = int(input("Soatni kiriting: "))
if 0 <= soat <= 12:
    print("Ertalab")
elif 13 <= soat <= 24:
    print("Kech")
else:
    print("Notog'ri soat kiritildi.")


3-savol
n = int(input("n sonini kiriting: "))
for i in range(1, n + 1):
    if i % 3 == 0:
        print(i)


4-savol
ro_yxat = [5, 12, 3, 18, 6, 9]
kichik = min(ro_yxat)
kattasi = max(ro_yxat)
print(f"Kichik son: {kichik}, Kattasi: {kattasi}")


5-savol
def toq_sonlar_kupaytmasi(ro_yxat):
    ko'paytma = 1
    for son in ro_yxat:
        if son % 2 != 0:
            ko'paytma *= son
    return ko'paytma
ro_yxat = [1, 2, 3, 4, 5, 6, 7]
print(f"Toq sonlarning ko'paytmasi: {toq_sonlar_kupaytmasi(ro_yxat)}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")



@dp.message_handler(lambda message: message.text.lower() =="28-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
c = float(input("Uchinchi sonni kiriting: "))
ko'paytma = a * b * c
print(f"Sonlarning ko'paytmasi: {ko'paytma}")


2-savol
baho = float(input("Bahonni kiriting: "))
if baho > 90:
    print("A'lo")
elif 80 <= baho <= 90:
    print("Yaxshi")
else:
    print("Qoniqarli")


3-savol
n = int(input("n sonini kiriting: "))
for i in range(1, n + 1):
    if i % 7 == 0:
        print(i)


4-savol
ro_yxat = [5, 12, 3, 18, 6, 9]
kichik = min(ro_yxat)
kattasi = max(ro_yxat)
kichik_index = ro_yxat.index(kichik)
kattasi_index = ro_yxat.index(kattasi)
print(f"Kichik sonning indeksi: {kichik_index}, Kattasi sonning indeksi: {kattasi_index}")


5-savol
def kichik_va_kattasini_yigindi(ro_yxat):
    kichik = min(ro_yxat)
    kattasi = max(ro_yxat)
    return kichik + kattasi
ro_yxat = [5, 12, 3, 18, 6, 9]
print(f"Kichik va kattasining yig'indisi: {kichik_va_kattasini_yigindi(ro_yxat)}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")



@dp.message_handler(lambda message: message.text.lower() =="29-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
ism = input("Ismingizni kiriting: ")
print(f"Ismingizning birinchi harfi: {ism[0]}")


2-savol
a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
if a < b:
    print("Kichik")
elif a > b:
    print("Katta")
else:
    print("Teng")


3-savol
n = int(input("n sonini kiriting: "))
for i in range(1, n + 1):
    print(f"{i} ning kvadrati: {i**2}")


4-savol
ro_yxat = [1, 2, 3, 4, 5]
for elem in reversed(ro_yxat):
    print(elem)


5-savol
def kichik_va_kattasi_orasidagi_sonlar(ro_yxat):
    kichik = min(ro_yxat)
    kattasi = max(ro_yxat)
    return ro_yxat.index(kattasi) - ro_yxat.index(kichik) - 1
ro_yxat = [3, 1, 5, 7, 9, 2, 6]
print(f"Kichik va kattasi orasida {kichik_va_kattasi_orasidagi_sonlar(ro_yxat)} ta son bor.")
'''
    await message.answer(f"Mana, kod:\n\n{code}")


@dp.message_handler(lambda message: message.text.lower() =="30-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))

ayirma = a - b
yig_indi = a + b

print(f"Sonlarning ayirmasi: {ayirma}")
print(f"Sonlarning yig'indisi: {yig_indi}")


2-savol
a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
c = float(input("Uchinchi sonni kiriting: "))

yig_indi = a + b + c
if yig_indi > 100:
    print("Katta")
else:
    print("Kichik")


3-savol
n = int(input("n sonini kiriting: "))
for i in range(1, n + 1):
    if i % 6 == 0:
        print(i)


4-savol
ro_yxat = [1, 2, 3, 4, 5]
for elem in ro_yxat:
    print(f"{elem}$")


5-savol
def ortacha_arifmetik(*sonlar):
    return sum(sonlar) / len(sonlar)
n = int(input("Nechta son kiritasiz? "))
sonlar = []
for _ in range(n):
    sonlar.append(float(input("Son kiriting: ")))
print(f"O'rta arifmetik qiymat: {ortacha_arifmetik(*sonlar)}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")



@dp.message_handler(lambda message: message.text.lower() =="31-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
son = float(input("Sonni kiriting: "))
print(f"Sonni 100 ga ko'paytirgan natija: {son * 100}")


2-savol
son = float(input("Sonni kiriting: "))
if son < 0:
    print(f"Sonning kubi: {son**3}")
else:
    print(f"Sonning kvadrati: {son**2}")


3-savol
n = int(input("n sonini kiriting: "))
for i in range(1, n + 1):
    print(f"{i} sonining kubi: {i**3}")


4-savol
ismlar = ["Ali", "Vali", "Zebo", "Laylo"]
for ism in ismlar:
    print(f"{ism[0]}")


5-savol
def kattasi(x, y, z):
    return max(x, y, z)
x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
z = float(input("Uchinchi sonni kiriting: "))
print(f"Eng katta son: {kattasi(x, y, z)}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")



@dp.message_handler(lambda message: message.text.lower() =="32-bilet")
async def send_code(message: types.Message):
    code ='''
1-savol
son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
print(f"Sonlarning ko'paytmasi: {son1 * son2}")


2-savol
yil = int(input("Yilni kiriting: "))
if yil % 4 == 0:
    print("Kabisa yili")
else:
    print("Oddiy yil")


3-savol
n = int(input("n sonini kiriting: "))
ko'paytma = 1
for i in range(1, n + 1):
    ko'paytma *= i
print(f"1 dan {n} gacha bo'lgan sonlarning ko'paytmasi: {ko'paytma}")


4-savol
ro'yxat = [1, 2, 3, 6, 8, 9, 12, 15, 18]
for element in ro'yxat:
    if element % 2 == 0 and element % 6 == 0:
        print(element)


5-savol
def ikki_xonali(ro'yxat):
    for element in ro'yxat:
        if 10 <= element < 100:
            return element
    return "Ikki xonali son topilmadi"

ro'yxat = [3, 7, 9, 12, 34, 6]
print(f"Birinci ikki xonali son: {ikki_xonali(ro'yxat)}")
'''
    await message.answer(f"Mana, kod:\n\n{code}")


if __name__ == '__main__':
    executor.start_polling(dp)