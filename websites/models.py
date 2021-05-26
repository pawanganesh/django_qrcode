import qrcode

from django.db import models

from io import BytesIO
from django.core.files import File
from PIL import Image


class Website(models.Model):
    url = models.CharField(max_length=200)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return str(self.url)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.url)
        canvas = Image.new('RGB', (370, 370), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.url}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)
