import qrcode

code = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=50,
    border=2
)

code.add_data('https://github.com/cerenaktas1')
code.make(fit=True)

image = code.make_image(fill_color="blue", back_color="black")
image.save('vol2.png')
