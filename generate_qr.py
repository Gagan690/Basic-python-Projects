import qrcode


gen_qr = qrcode.make("Hello my name is Python")

gen_qr.save("qrcode.jpg")

