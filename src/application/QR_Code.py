#EH PRECISO INTALAR pip install qrcode PARA UTILIZAR DESSA BIBLIOTECA
import qrcode

#Essa funcao recebe um link e um nome de arquivo e gera um arquivo .png com o qr code e o nome passado, no diretorio QR
def cria_qr(link, nome_arquivo):
    img = qrcode.make(link)
    img.save('././QR/'+ nome_arquivo)

#cria_qr("https://www.google.com", "google.png")