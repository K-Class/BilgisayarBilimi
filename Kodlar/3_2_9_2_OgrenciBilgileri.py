# Öğrenci Bilgileri
print("Öğrenci Bilgileri Giriş Ekranı")
adı=input("Öğrenci Adı:")
soyadı=input("Öğrenci Soyadı:")
babaAdı=input("Baba Adı:")
anneAdı=input("Anne Adı:")
sınıfı=input("Sınıfı:")
# Kullanıcının girdiği doğum yılı verisi int değere çevrildi
# doğumYılı değişkeni int tipinde değer aldığı  için int tipinde
doğumYılı=int(input("Doğum Yılı:"))


günümüzYılı=2017

# \n karakteri bir satır boşluk verir
print("\nÖğrenci Bilgileri")
print("Öğrencinin Adı:",adı)
print("Öğrencinin Soyadı:",soyadı)
print("Baba Adı:",babaAdı)
print("Anne Adı:",anneAdı)
print("Öğrencinin Doğum Yılı:",doğumYılı)
print("Öğrencinin Sınıfı:",sınıfı)
# öğrencinin yaşı hesaplanarak yazdırılıyor
yaş = günümüzYılı - doğumYılı
print("Öğrencinin Yaşı:",yaş)

# Ekran çıktısı
"""
Öğrenci Bilgileri Giriş Ekranı
Öğrenci Adı:Ahmet
Öğrenci Soyadı:TUNA
Baba Adı:Mehmet
Anne Adı:Ayşe
Sınıfı:9-B
Doğum Yılı:2003

Öğrenci Bilgileri
Öğrencinin Adı: Ahmet
Öğrencinin Soyadı: TUNA
Baba Adı: Mehmet
Anne Adı: Ayşe
Öğrencinin Doğum Yılı: 2003
Öğrencinin Sınıfı: 9-B
Öğrencinin Yaşı: 14
"""