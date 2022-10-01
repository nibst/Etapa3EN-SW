#EH PRECISO INTALAR pip install fpdf PARA UTILIZAR DESSA BIBLIOTECA
from fpdf import FPDF
import os

def gera_certificado(nome_pessoa, nome_evento, data_inicio, data_fim, local):
    pdf = FPDF('P', 'mm', (675, 500))
    pdf.add_page()
    base = os.path.abspath("./src/images/base.jpg")
    #print(base)
    pdf.image(base, x=0, y=0, w=0, h=0)
    pdf.ln(50)
    #Certificado de Participação
    pdf.set_font('Times', '', 100)
    pdf.set_text_color(70, 70, 70)
    pdf.cell(650, 50, "CERTIFICADO DE PARTICIPAÇÃO", align='C', border=0)
    pdf.ln(100)
    #Nome do Participante
    pdf.set_font('Times', 'B', size = 100)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(650, 50, nome_pessoa, align='C', border=0)
    pdf.ln(50)
    #Descrição pt1
    pdf.set_font('Times', '', 60)
    mensagem = "participou do evento " + nome_evento 
    pdf.cell(650, 20, mensagem, align='C', border=0)
    pdf.ln(20)
    #Descrição pt2
    mensagem = "realizado de " + data_inicio + " a " + data_fim + "."
    pdf.cell(650, 20, mensagem, align='C', border=0)
    pdf.ln(50)
    #Local e data
    pdf.set_font('Times', '', 60)
    pdf.set_text_color(20, 160, 60)
    mensagem = local + ", " + data_fim
    pdf.cell(650, 20, mensagem, align='C', border=0)
    pdf.ln(80)
    #Assinatura
    pdf.set_font('Times', '', 60)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(650, 20, "__________________", align='C', border=0)
    pdf.ln(25)
    pdf.cell(650, 20, "Assinatura", align='C', border=0)
    pdf.ln(20)
    #Imprime o certificado
    mensagem = "././Certificados/" + nome_pessoa + "_certificado.pdf"
    pdf.output(mensagem, 'F')

#gera_certificado("João da Silva", "Contrução avançada de robôs", "01/01/2020", "02/01/2020", "Porto Alegre")