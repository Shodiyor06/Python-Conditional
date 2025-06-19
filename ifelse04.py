masofa = float(input("Masofani kiriting (km): "))

if masofa < 0:
    print("Masofa manfiy bo'la olmaydi!")
if masofa >= 0 and masofa <= 1:
    print("Piyoda yuring")
if masofa > 1 and masofa <= 5:
    print("Velosiped yoki elektr skuter")
if masofa > 5 and masofa <= 50:
    print("Avtobus yoki mashina")
if masofa > 50:
    print("Poyezd yoki samolyot")
if masofa < 0:
    print("musbat son kiritib bulmaydi")
    
