#EH PRECISO INTALAR pip install qrcode PARA UTILIZAR DESSA BIBLIOTECA
import qrcode

#Essa funcao recebe um link e um nome de arquivo e gera um arquivo .png com o qr code e o nome passado, no diretorio QR
def cria_qr(link, id_evento):
    img = qrcode.make(link)
    img.save('src/images/QR/'+ id_evento+'.png')

#cria_qr("https://www.google.com", "120")