# gera-qrcode

<tr>

# Instale a biblioteca qrcode no terminal

pip istall qrcode

# Importe a biblioteca qrcode no IDE

import qrcode

# Entrada da URL

link = input("URL: ")

# Gerando QrCode

qrcode = qrcode.make(link)

# Salvando imagem QrCode

qrcode.save("qrcode.jpg")

# Mensagem que retorna quando o processo é finalizado com êxito

print("Pronto!")
