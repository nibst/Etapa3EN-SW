#EH PRECISO INTALAR pip install qrcode PARA UTILIZAR DESSA BIBLIOTECA
import qrcode

#Essa funcao recebe um link e um nome de arquivo e gera um arquivo .png com o qr code e o nome passado, no diretorio QR
def create_qr(link, id_evento):
    img = qrcode.make(link)
    img.save('src/images/QR/'+ id_evento+'.png')

def create_qrs_for_event_creation(domain, event):
    site = domain
    id_check_in = 'check_in' + str(event.get_id())
    link = site + "/event/" + str(event.get_id()) + "/check_in"
    create_qr(link,id_check_in)
    id_check_out = 'check_out' + str(event.get_id())
    link = site + "/event/" + str(event.get_id()) + "/check_out"
    create_qr(link,id_check_out)
#cria_qr("https://www.google.com", "120")