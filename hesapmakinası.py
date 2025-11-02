print("Hesap makinasına hoş geldiniz")


sayi = int(input("Lütfen ilk sayıyı giriniz:"))
sayi2 = int(input("Lütfen ikinci sayıyı da giriniz:"))

işlem = input("Bir işlem seçiniz (+,-,*,/,%,//):")

if işlem == "+":
    print(sayi + sayi2)
elif işlem == "-":
    print(sayi - sayi2)
elif işlem == "*":
    print(sayi*sayi2)
elif işlem == "/":
    if sayi2 != 0:
        print(sayi / sayi2)
    else:
        print("Sıfıra bölme hatası")
elif işlem == "%":
    if sayi2 != 0:
        print(sayi % sayi2)
    else:
        print("Sıfıra bölme hatası")
elif işlem == "//":
    if sayi2 != 0:
        print(sayi // sayi2)
    else:
        print("Sıfıra bölme hatası")
else:
    print("Yanlış giriş yaptınız.")





