import pyttsx3
import PyPDF2

book= open('Evvvv.pdf','rb')#rb ---> reading book
pdfreader=PyPDF2.PdfFileReader(book)
pages=pdfreader.numPages
print(pages)
speaker=pyttsx3.init()
for num in range(7,14):
    page=pdfreader.getPage(num)
    text=page.extract_text()
    speaker.say(text)
    speaker.runAndWait()