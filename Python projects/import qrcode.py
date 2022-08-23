import qrcode

features= qrcode.QRCode(version=1,box_size=40,border=5)

features.add_data('https://tbklaa-logesh-tce.netlify.app/')
features.make(fit=True)     #whatever we given the boxsize nd border must be fit
generate_image= features.make_image(fill_color="black",back_color="white")
generate_image.save('mywebqrcode.png')

