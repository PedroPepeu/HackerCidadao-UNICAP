import qrcode as qc

# Link enter here
link = input()

# Data to be encoded
data = link

# Encoding data using what I put in aspas
img = qc.make(data)

# Saving as an image file
img.save('QRCodeMaker/MyQRCode1.png')