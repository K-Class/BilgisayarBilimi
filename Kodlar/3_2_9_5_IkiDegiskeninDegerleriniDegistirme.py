# İki değişkenin değerini birbiriyle değiştirme
print("İkinci Değişkenin Değeri Birinciden Büyük Olmalı")
birinciDeğişken = int(input("Birinci Değişkeni Girin: "))
ikinciDeğişken = int(input("İkinci Değişkeni Girin: "))

fark = birinciDeğişken - ikinciDeğişken
print("Değişkenler İlk Durumuda Yapılan Çırkama İşleminin Sonucu:",fark)

# değişkenlerin değerleri bir biriyle değişiyor
birinciDeğişken,ikinciDeğişken = ikinciDeğişken,birinciDeğişken

fark = birinciDeğişken - ikinciDeğişken
print("Değişkenlerin Değerleri Bir Biriyle Değiştirilince Sonuç:",fark)

# Ekran çıktısı
"""
İkinci Değişkenin Değeri Birinciden Büyük Olmalı
Birinci Değişkeni Girin: 30
İkinci Değişkeni Girin: 45
Değişkenler İlk Durumuda Yapılan Çırkama İşleminin Sonucu: -15
Değişkenlerin Değerleri Bir Biriyle Değiştirilince Sonuç: 15
"""