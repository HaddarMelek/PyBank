from tkinter import Tk
from fenetres import FenetreInitiale

def main():
    fenetre_initiale = Tk()
    fenetre_initiale.title('Gestion Banque')
    fenetre_initiale.geometry('1080x720')
    fenetre_initiale.configure(bg='#ddd')
    fenetre_initiale.minsize(480, 360)
    fenetre_initiale.iconbitmap('resources/logo.ico')

    dictionnaire_des_clients = {}
    FenetreInitiale(fenetre_initiale, dictionnaire_des_clients)
    fenetre_initiale.mainloop()

if __name__ == "__main__":
    main()
