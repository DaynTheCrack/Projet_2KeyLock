import math
from tkinter import *

window = Tk()
window.title("2KeyLock")
window.geometry("1080x720")
window.minsize(480, 360)
window.maxsize(1080, 720)
window.config(background='#41B77F')

frame = Frame(window, bg='#41B77F', bd=1, relief=SUNKEN)

label_title = Label(frame, text="Welcome to 2KeyLock", font=("Arial", 30), bg="#41B77F")
label_title.pack()

label_subtitle = Label(frame, text="Entrer un fichier d'entrée a CHIFFRER/DECHIFFRER:", font=("Arial", 15), bg="#41B77F")
label_subtitle.pack()

lancement_button = Button(frame, text="Fichier", font=("Arial", 10), fg="#41B77F", bg="white")
lancement_button.pack(pady=10, fill=X)

notice_button = Button(frame, text="Notice d'utilisation", font=("Arial", 10), fg="#41B77F", bg="white")
notice_button.pack(pady=10, fill=X)

SecNiveau_button = Button(frame, text="Niveau de Sécurité", font=("Arial", 10), fg="#41B77F", bg="white")
SecNiveau_button.pack(pady=10, fill=X)

SecNiveau_button = Button(frame, text="Crédits", font=("Arial", 10), fg="#41B77F", bg="white")
SecNiveau_button.pack(pady=10, fill=X)

frame.pack(expand=YES)

window.mainloop()
