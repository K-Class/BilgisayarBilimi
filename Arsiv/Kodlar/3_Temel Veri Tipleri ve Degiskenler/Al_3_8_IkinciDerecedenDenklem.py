# İkinci Dereceden Bir Bilinmeyenli Denklemlerin Köklerini Bulma

a = int(input("Tam Sayı a: "))
b = int(input("Tam Sayı b: "))
c = int(input("Tam Sayı c: "))

delta = b**2 - 4*a*c

x1 =(-b - delta**0.5)/(2 * a)
x2 =(-b + delta**0.5)/(2 * a)

print("\nBirinci Kök: ",x1 ,"\nİkinci Kök: ",x2)

# Ekran çıktısı
"""
Tam Sayı a: 1
Tam Sayı b: -4
Tam Sayı c: 4

Birinci Kök:  2.0 
İkinci Kök:  2.0
"""