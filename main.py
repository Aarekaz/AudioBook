import pyttsx3
import PyPDF2

book = open('test.pdf', 'rb')  # reading the book as a binary book
reader = PyPDF2.PdfFileReader(book)
pages = reader.numPages
print(pages)
speaker = pyttsx3.init()  # Initializing the library
for num in range(7,pages):
    page = reader.getPage(1)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

