import qrcode
import qrcode.image.svg
from io import BytesIO
import base64

def generate_qr(text):
  qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=50,
    border=4,
  )
  qr.add_data(text)
  qr.make(fit=True)

  img = qr.make_image(back_color=(58, 46, 57), fill_color=(241, 81, 82))

  buffer = BytesIO()
  img.save(buffer, "PNG")
  buffer.seek(0)
  data = buffer.getvalue()

  return base64.b64encode(data).decode()