# Girilen Saniye değerini Saat:Dakika:Saniye gösterimi
saniye = int(input("Saniye: "))

# 3600 saniye = 1 saat
saat = saniye//3600
saniye = saniye%3600

# 60 saniye = 1 dakika
dakika = saniye//60
saniye = saniye%60

print(saat, " :", dakika, " :", saniye)

# Ekran çıktısı
"""
Saniye: 29000
8  : 3  : 20
"""