# sonucu tam sayı çıkan bölme işlemlerinin sonuçlarını tam sayı yazdırma
print("Sonucu Tam Sayı Çıkan Bölme İşlemleri İçin Değer Girin")

bölünen = int(input("Bölünecek Sayıyı Girin: "))
bölen = int(input("Bölecek Sayıyı Giriniz: "))

sonuç = bölünen / bölen
print("Tip Dönüşümü Yapılmadan Önce Sonuç: ", sonuç)

sonuç = int(sonuç)
print("Tip Dönüşümü Yapıldıktan Sonra Sonunç: ", sonuç)

# Ekran çıktısı
"""
Sonucu Tam Sayı Çıkan Bölme İşlemleri İçin Değer Girin
Bölünecek Sayıyı Girin: 36
Bölecek Sayıyı Giriniz: 12
Tip Dönüşümü Yapılmadan Önce Sonuç:  3.0
Tip Dönüşümü Yapıldıktan Sonra Sonunç:  3
"""