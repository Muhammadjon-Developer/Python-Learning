# print()  # function ni bizga terminalda yoki da boshqa joyda yozgan ma'lumotimizni ko'rsatadi

# print(10, 'Hello', True)  # javob: 10 Hello True
# print("Salom mening ismim Muhammadjon")

# # javob: <built-in function print> = print bu python ning shaxsiy functioni dir
# print(print)
# # javob: <built-in function input> = input bu python ning shaxsiy functioni dir
# print(input)

# # INPUT FUNCTION NI BILAN ISHLASH

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# job = input("Enter your job: ")

# # print(name, age, job)  #inputga yozgan ma'lumotlaringizni ko'rsatadi

# # CAPITALIZE
# ism = input("Ismingiz nima: ")
# # Qanday uslubda ma'lumot kiritmang ning bosh harifini katta
# print(ism.capitalize())
# # Asl o'zgaruvchining qiymatini o'zgartirmaydi yangi qiymat yaratadi capatalize va boshqa ko'plab funksiyalar
# print(ism)

# # UPPER
# hobby = input("Enter your hobby: ")
# print(hobby.upper())  # Kiritgan barcha ma'lumotlarni katta harfda ko'rsat


# # FUNKSIYALARNI KO'RIB CHIQISH

# def hello(name):
#     print("Hello there,", name)


# hello('Muhammadjon')

# # FUNKSIYADAGI RETURN KALIT SO'ZI


# def sum_nums(a, b):
#     sum = a + b
#     return sum
#     print("Return kalit so'zidan keyingi kodlar ko'rsatilmaydi (bu kod ham)")


# first_sum = sum_nums(10, 5)
# print(first_sum)

# print(sum_nums(10.5, 1))


# # IFODA - IFODALASH

# print(print(10 + 5))
# print('salom')

# print(input("Enter your name: "))


# STATEMENTLAR

# python modullarini import qilish

# import datetime

# print(datetime.MINYEAR)


# O'ZGARUVCHILAR

# Python da nomlash:

# snake_case = 'snake_case'  # snake_case usuli = metod, funksiya va o'zgaruvchilarni nomlashda

# PascalCase = 'PascalCase' # Pascal_Case = klass larni nomlashda ishlatiladi

# my-package = 'package' # paketlarni nomlashda

# DB_PASSWORD = 'SNAKE_CASE'  # const (o'zgarmatdigan) tanlarni nomlashda snake_case katta harfda. (Pythonda luboy o'zgaruvchining qiymatini o'zgartirish mumkin ammo siz o'zgartirmaydigan o'zgaruvchilarning nomi barchasini katatta harflarda yozish BEST_PRACTISE ga kiradi)


# O'ZGARUVCHILARNI ELON QILISH

show_my_name = 'Muhammadjon'  # snake_case uslubida yozilgan chunki bu mashhur uslub

print(show_my_name)  # Muhammadjon

show_my_name = 'Oybek'  # snake_case uslubida yozilgan chunki bu mashhur uslub

print(show_my_name)  # Oybek

number = 10

number = 20

print(number)  # 20

# Katta SBAKE_CASE uslubida yozilgan chunki biz bu o'zgaruvchini hech qachon o'zgartirmaymiz (misol uchun)
MY_PASSWORD = '1234567qqw'

# Kichik snake_case uslubida yozilgan chunki biz bu o'zgaruvchini o'zgartiramiz (misol uchun)
my_username = 'MuhammadDevelopment'
