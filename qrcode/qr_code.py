
import pyqrcode
import png
msg = "PRAJAKTA KANK "
url= pyqrcode.create(msg)
url.png('myqr1.png',scale= 8)
