def aralik_bul(age):
    """
    Girilen yaşa göre aralığı belirler ve döndürür.
    """
    if 0 <= age <= 14:
        return "Çocuklar ve ergenler aralığındasınız."
    elif 15 <= age <= 64:
        return "Aktif nüfus veya çalışan nüfus aralığındasınız."
    elif age >= 65:
        return "Yaşlı ve bağımlı nüfus aralığındasınız."
    else:
        return "Geçersiz yaş değeri."

def dosya_okuma_ve_isleme(dosya_adi):
    """
    input.txt dosyasını okuyarak, içeriğindeki yaşa göre aralığı belirler ve sonucu döndürür.
    """
    try:
        with open(dosya_adi, 'r') as file:
            # Dosyadaki ilk satırı al
            age = int(file.readline().strip())
            result = aralik_bul(age)
            return result
    except Exception as e:
        return f"Hata: {str(e)}"

