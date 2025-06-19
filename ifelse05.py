vazn = float(input("Vazningizni kiriting (kg): "))
boy = float(input("Bo'yingizni kiriting (m): "))

if vazn <= 0 or boy <= 0:
    print("Vazn va bo'y musbat bo'lishi kerak")
if boy < 0.5 or boy > 3.0:
    print("Bo'y 0.5 - 3.0 metr oralig'ida bo'lishi kerak")
if vazn < 1 or vazn > 500:
    print("Vazn 1 - 500 kg oralig'ida bo'lishi kerak")

if vazn > 0 and boy > 0 and boy >= 0.5 and boy <= 3.0 and vazn >= 1 and vazn <= 500:
    bmi = vazn / (boy ** 2)
    print("BMI:", round(bmi, 2))

    if bmi < 18.5:
        print("Kam vazn")
    if bmi >= 18.5 and bmi < 25:
        print("Oddiy vazn")
    if bmi >= 25 and bmi < 30:
        print("Ortiqcha vazn")
    if bmi >= 30:
        print("Semizlik")

