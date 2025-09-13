import qrcode
url = input("Enter the URL to generate QR code: ")


img = qrcode.make(url)
img.show()
img.save("qr_url.png")
print("QR code saved as qr_url.png")
