suma = int(input("yechmoqchi bulgan suma:"))

hisob= 5000

if suma <= hisob:
    hisob-=suma
    print(f"Pul yechildi. Qolgan balans: {hisob} so'm")
else:
    print("Mablag' yetarli emas. Sizning balansingiz: 5000 so'm")
if suma < 0:
    print("Manfiy summa kiritib bo'lmaydi.")