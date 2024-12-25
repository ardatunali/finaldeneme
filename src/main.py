# main.py

def aralik_bul(age):
    """
    Girilen yaşa göre aralığı belirler ve döndürür.
    """
    if 0 <= age <= 14:
        return "Cocuklar ve ergenler aralıgindasiniz."
    elif 15 <= age <= 64:
        return "Aktif nufus veya calısan nufus aralıgindasiniz."
    elif age >= 65:
        return "Yasli ve bagimli nufus aralıgindasiniz."
    else:
        return "Gecersiz yas degeri."
