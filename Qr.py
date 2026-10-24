import qrcode

url = input("Enter your url : ").strip()
file = "D:\\Python program\\QR.png"

qr = qrcode.QRCode()
qr.add_data(url)

image = qr.make_image()
image.save(file)

print("QR  Ganereted !")