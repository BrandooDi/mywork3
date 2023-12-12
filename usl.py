print(
    "Введите количество часов 0<h<=23, количество минут 0<=m<=59 и количество секунд 0<=s<=59"
)
h = int(input("h="))
m = int(input("m="))
s = int(input("s="))
sek = int(0)
if h <= 0 or h > 23 or m < 0 or m > 59 or s < 0 or s > 59:
    print("Вы ввели некоректное число")
else:
    h = h % 12
    sek = h * 3600 + m * 60 + s
if sek == 0:
    ygol = 0
else:
    ygol = 360 * sek / 43200
    print(ygol)
