import qrcode

link = input("URL: ")

qrcode = qrcode.make(link)

qrcode.save("qrcode.jpg")

print("Pronto!")
