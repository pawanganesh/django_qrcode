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

    def qr_code_generator(self):
        qrcode_img = qrcode.make(self.url)
        canvas = Image.new('RGB', (370, 370), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.url}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()

    @classmethod
    def from_db(cls, db, field_names, values):
        instance = super().from_db(db, field_names, values)
        instance._loaded_values = dict(zip(field_names, values))

        # instance = super().from_db(db, field_names, values)
        # values = dict(zip(field_names, values))
        # instance._prev_url = values.get('url')

        return instance

    def save(self, *args, **kwargs):
        if not self.id:
            self.qr_code_generator()
        if self.id and self.url != self._loaded_values['url']:
            self.qr_code.delete(save=False)
            self.qr_code_generator()
        super().save(*args, **kwargs)
