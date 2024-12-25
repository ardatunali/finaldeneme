# testmain.py

from main import aralik_bul

# Kullanıcıdan yaş bilgisini al
age = int(input("Yaşınızı girin: "))

# Fonksiyonu çağır ve sonucu al
result = aralik_bul(age)

# Sonucu 'aralığınız.txt' dosyasına yaz
with open("aralığınız.txt", "w") as file:
    file.write(result)

print("Sonuç 'aralığınız.txt' dosyasına yazıldı.")
