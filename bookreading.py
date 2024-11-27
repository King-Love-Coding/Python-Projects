# import speech_recognition as sr
# from googlesearch import search
# import requests
# import PyPDF2
# import pyttsx3
# import io
#
# def listen_for_book():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Say the name of the book:")
#         audio = recognizer.listen(source)
#
#     try:
#         book_name = recognizer.recognize_google(audio)
#         print(f"You said: {book_name}")
#         return book_name
#     except sr.UnknownValueError:
#         print("Sorry, I could not understand the audio.")
#     except sr.RequestError as e:
#         print(f"Could not request results; {e}")
#     return None
#
# def search_book_pdf(book_name):
#     query = f"{book_name} pdf"
#     for result in search(query, num_result=5):
#         if result.endswith('.pdf'):
#             return result
#     return None
#
# def read_pdf_aloud(pdf_url):
#     response = requests.get(pdf_url)
#     pdf_file = io.BytesIO(response.content)
#     pdf_reader = PyPDF2.PdfFileReader(pdf_file)
#     engine = pyttsx3.init()
#
#     for page_num in range(min(5, pdf_reader.numPages)):  # Read the first 5 pages for demo
#         page = pdf_reader.getPage(page_num)
#         text = page.extract_text()
#         engine.say(text)
#         engine.runAndWait()
#
# def main():
#     book_name = listen_for_book()
#     if book_name:
#         pdf_url = search_book_pdf(book_name)
#         if pdf_url:
#             print(f"Found PDF: {pdf_url}")
#             read_pdf_aloud(pdf_url)
#         else:
#             print("Sorry, no suitable PDF found.")
#     else:
#         print("Sorry, could not get the book name.")
#
# if __name__ == "__main__":
#     main()


import speech_recognition as sr
from googlesearch import search
import requests
import PyPDF2
import pyttsx3
import io


def listen_for_book():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say the name of the book:")
        audio = recognizer.listen(source)

    try:
        book_name = recognizer.recognize_google(audio)
        print(f"You said: {book_name}")
        return book_name
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    return None


def search_book_pdf(book_name):
    query = f"{book_name} pdf"
    try:
        for result in search(query, num_results=10):
            if result.lower().endswith('.pdf'):
                return result
    except Exception as e:
        print(f"Error during search: {e}")
    return None


def read_pdf_aloud(pdf_url):
    try:
        response = requests.get(pdf_url)
        response.raise_for_status()  # Check for HTTP errors
        pdf_file = io.BytesIO(response.content)

        try:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
        except PyPDF2.utils.PdfReadError:
            print("Error reading PDF file.")
            return

        engine = pyttsx3.init()

        for page_num in range(min(5, len(pdf_reader.pages))):  # Read the first 5 pages for demo
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            if text:
                engine.say(text)
                engine.runAndWait()
            else:
                print(f"No text found on page {page_num + 1}.")

    except requests.RequestException as e:
        print(f"Error fetching PDF: {e}")


def main():
    book_name = listen_for_book()
    if book_name:
        pdf_url = search_book_pdf(book_name)
        if pdf_url:
            print(f"Found PDF: {pdf_url}")
            read_pdf_aloud(pdf_url)
        else:
            print("Sorry, no suitable PDF found.")
    else:
        print("Sorry, could not get the book name.")


if __name__ == "__main__":
    main()
