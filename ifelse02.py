son1 = float(input("1-sonni kiriting: "))
son2 = float(input("2-sonni kiriting: "))
amal = input("Amalni kiriting (+, -, *, /): ")

if amal == "+":
    print("Natija:", son1 + son2)
if amal == "-":
    print("Natija:", son1 - son2)
if amal == "*":
    print("Natija:", son1 * son2)
if amal == "/":
    if son2 != 0:
        print("Natija:", son1 / son2)
    if son2 == 0:
        print("Nolga bo'lish mumkin emas!")
if amal != "+" and amal != "-" and amal != "*" and amal != "/":
    print("Noto'g'ri amal. Faqat +, -, *, / ishlatiladi.")

