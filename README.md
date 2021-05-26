#  django_qrcode

http://127.0.0.1:8000/admin/websites/website/ <br>
Currently, We can save new website url and auto generate qr code.

<br>For example:<br>
url: somesite.com<br>
qr_code:  qr_codes/qr_code-somesite.com/.png
#  problem
While updating object with/without changing url, new qr_code file is generated.
<br>For exmaple:<br>
url: somesite.com<br>
qr_code:  qr_codes/qr_code-somesite.com/.png_VeTc9nR<br>

Every time new qr_code is generated and also stores previously generated file in the given path.
<br>
#  want I want
1. While updating object without changing url field, new qr_code should not be generated.<br>
2. While updating object changing url field, new qr_code should be genrated and previously generate file should be deleted.

#  how can I achieve this
