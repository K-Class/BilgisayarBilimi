# Vücut Kitle Endeksi(BMI) Hesaplama
print("Vücut Kitle Endeksi(BMI) Hesaplama")
boy = float(input("Boyunuzu Metre Cinsinden Giriniz(1.85 gibi):"))
kilo = int(input("Kilonuzu Tam Sayı Olarak Giriniz(85 gibi):"))

# Vücut Kitle Endeksi formülü
vucutKitleEndeksi = kilo/(boy*boy)

print("Vücut Kitle Endeksiniz (BMI):",vucutKitleEndeksi)

# Ekran çıktısı
"""
Vücut Kitle Endeksi(BMI) Hesaplama
Boyunuzu Metre Cinsinden Giriniz(1.85 gibi):1.75
Kilonuzu Tam Sayı Olarak Giriniz(85 gibi):80
Vücut Kitle Endeksiniz (BMI): 26.122448979591837
"""