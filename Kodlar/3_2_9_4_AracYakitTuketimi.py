# Deposu Dolu Aracın Yakıt Hesabı
print("Araç Kullanım Bilgileri Giriş Ekranı")
gidilenYol=float(input("Gidilen Yol(km):"))
alınanYakıtLitre=float(input("Aldığınız Yakıt Miktarı(lt):"))
alınanYakıtTutarı=float(input("Alınan Yakıt Tutarı:"))

yüzKm_litre = (alınanYakıtLitre/gidilenYol)*100
yüzKm_Tutar = (alınanYakıtTutarı/gidilenYol)*100

print("100km 'de Harcanan Yakıtın Litresi:",yüzKm_litre)
print("100km 'de Harcanan Yakıtın Tutarı:",yüzKm_Tutar)

# Ekran çıktısı
"""
Araç Kullanım Bilgileri Giriş Ekranı
Gidilen Yol(km):428.8
Aldığınız Yakıt Miktarı(lt):27.982
Alınan Yakıt Tutarı:146.6
100km 'de Harcanan Yakıtın Litresi: 6.525652985074625
100km 'de Harcanan Yakıtın Tutarı: 34.18843283582089
"""