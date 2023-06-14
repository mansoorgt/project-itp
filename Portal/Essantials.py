import qrcode

from django.shortcuts import HttpResponse 
class Qrcode_generate():
    def __init__(self,filename,data):
        self.url='media/qrcodes'
        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save('media/qrcodes/'+filename+'.png')
        self.url='https://www.nextwrld.sa/registration/media/qrcodes/'+filename+'.png'
        
    #def generate(self,):
        
        
        # return {'url':'media/qrcodes/'+filename+'.png'}

def check(request):
    Qrcode_generate(filename='new-qr',data='hi').url
    return HttpResponse('success')