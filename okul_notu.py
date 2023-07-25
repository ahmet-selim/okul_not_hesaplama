not1 = int(input("Türkçe sınavı notunuzu giriniz :"))
not2 = int(input("Sosyal bilgiler sınavı notunuzu giriniz :"))
not3 = int(input("İngilizce sınavı notunuzu giriniz :"))
not4 = int(input("Fen bilimleri sınavı notunuzu giriniz :"))
not5 = int(input("Din kültürü sınavı notunuzu giriniz :"))
not6 = int(input("Matematik sınavı notunuzu giriniz :"))
not7 = int(input("Görsel sanatlar sınavı notunuzu giriniz :"))
not8 = int(input("Beden eğitimi sınavı notunuzu giriniz :"))
not9 = int(input("Almanca sınavı notunuzu giriniz :"))
ortalama = float((not1 + not2 + not3 + not4 + not5 + not6 + not7 + not8 + not9)/9)
ortalaman = str((not1 + not2 + not3 + not4 + not5 + not6 + not7 + not8 + not9)/9)


print(str("Senin ortalaman = " + ortalaman))
if(ortalama>85.0):
    print("Takdir belgesi aldın. Aferin sana.")
elif(ortalama>75.0):
    print("Teşekkür belgesi aldın. Bir dahakine daha çok çalış.")
else:
    print("Belge alamadın. Üzülme bir dahakine çok daha fazla çalış.")
