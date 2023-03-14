import pyttsx3
import PyPDF2

book = open('sample.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
totalPages = pdfReader.numPages
print("total pages in book are {} ".format(totalPages))
voice = pyttsx3.init()
for i in range(0, totalPages):
    page = pdfReader.getPage(i)
    text = page.extractText()
    voice.say(text)
    voice.runAndWait()