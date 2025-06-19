narx = 100

yosh = int(input("Yoshingizni kiriting: "))

if yosh <= 6:
    narx = narx * 0.5
if yosh >= 7 and yosh <= 17:
    narx = narx * 0.8
if yosh > 60:
    narx = narx * 0.7

print(f"Siz uchun chipta narxi: {narx} so'm")
