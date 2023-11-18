import tkinter
import json
from pathlib import Path
from tkinter import Menu, messagebox

fenetre = tkinter.Tk()
fenetre.geometry("500x600")
biblio_file = Path("gestio_biblio.json")
if biblio_file.is_file():
    biblio = json.loads(biblio_file.read_text())
else: 
    biblio = []

def update():
    liste_de_recherche.delete(0,tkinter.END)
    with open("gestio_biblio.json", "r") as f:
        biblio= json.load(f)
        for ajout in biblio:
            liste_de_recherche.insert(tkinter.END, f"{ajout['titre']} - {ajout['auteur']} - {ajout['isbn']} - {ajout['genre']}")
  
def ajouter_livre():
    titre = titre_entry.get()
    auteur = auteur_entry.get()
    isbn = isbn_entry.get()
    genre = genre_entry.get()
    for ajout in biblio:
        if isbn == ajout["isbn"]:
            messagebox.showwarning("Erreur", "Le livre existe de déjà")
            print("Le livre existe de déjà")
            return (ajouter_livre)
    ajout = {
        "titre" : titre,
        "auteur" : auteur,
        "isbn" : isbn,
        "genre" : genre
    }
    titre_entry.delete(0, 40)
    auteur_entry.delete(0, 40)
    isbn_entry.delete(0,40)
    genre_entry.delete(0,40)
    with open( "gestio_biblio.json", "w") as f:
        biblio.append(ajout)
        json.dump(biblio, f, indent= 4)
    update()
def supprimer():
    livre_supprimer= False
    isbn = code_isbn_entry.get()
    for ajout in biblio:
        if isbn == ajout["isbn"]:
            biblio.remove(ajout)
            print(biblio)
            with open("gestio_biblio.json", "w") as g:
                json.dump(biblio, g, indent=4)
            livre_supprimer = True
            print(f"le livre ayant le code  {isbn} a été supprimer")
            update()
            break
    if not livre_supprimer:
        print(f"le livre ayant le code  {isbn} n'exite pas ")
    code_isbn_entry.delete(0, 40)
def rechercher ():
    resultat_de_recherche = []
    titre = rechercher_entry.get()
    auteur = rechercher_entry.get()
    isbn = rechercher_entry.get()
    genre = rechercher_entry.get()

   
    for i in biblio:
        if (
            titre in i["titre"]
            or auteur in i["auteur"]
            or isbn in i["isbn"]
            or genre in i["genre"]
        ):
            resultat_de_recherche.append(i)
            liste_de_recherche.delete(0,tkinter.END)
            liste_de_recherche.insert(tkinter.END, f"{i['titre']} - {i['auteur']} - {i['isbn']} - {i['genre']}")
    if resultat_de_recherche:
        print(resultat_de_recherche)
    else:
        print("Aucun résultat")
    rechercher_entry.delete(0,40)
   
    
def modification():
    titre = titre_entry.get()
    auteur = auteur_entry.get()
    isbn = isbn_entry.get()
    genre = genre_entry.get()

    for ajout in biblio:
        if isbn == ajout["isbn"]:
            ajout["titre"] = titre
            ajout["auteur"] = auteur
            ajout["isbn"] = isbn
            ajout["genre"] = genre
            with open ("gestio_biblio.json", "w") as f:
                json.dump(biblio, f, indent=4)
    update()

titre_label = tkinter.Label(fenetre, text="titre")
titre_label.grid(row= 0 , column=0)
titre_entry = tkinter.Entry(fenetre)
titre_entry.grid(row= 0 , column=1)

auteur_label = tkinter.Label(fenetre, text="auteur")
auteur_label.grid(row=1, column=0)
auteur_entry = tkinter.Entry(fenetre)
auteur_entry.grid(row=1, column=1)

isbn_label = tkinter.Label(fenetre, text="isbn")
isbn_label.grid(row=2, column=0)
isbn_entry = tkinter.Entry(fenetre)
isbn_entry.grid(row=2, column=1)

genre_label = tkinter.Label(fenetre, text="genre")
genre_label.grid(row=3, column=0)
genre_entry = tkinter.Entry(fenetre)
genre_entry.grid(row=3, column=1)

bouton_ajout = tkinter.Button(fenetre, text="ajouter", font=("bold" ,15), command=ajouter_livre)
bouton_ajout.grid(row=4, columnspan=2)
bouton_ajout.pack

bouton_ajout = tkinter.Button(fenetre, text="modifier", font=("bold" ,15), command=modification)
bouton_ajout.grid(row=4, column=1)
bouton_ajout.pack

code_isbn_label = tkinter.Label(fenetre, text="code isbn")
code_isbn_label.grid(row=5 , column=0)
code_isbn_entry = tkinter.Entry(fenetre)
code_isbn_entry.grid(row=5,column=1)

bouton_supprimer = tkinter.Button(fenetre, text="supprimer", command=supprimer)
bouton_supprimer.grid(row=6, columnspan=2)
bouton_supprimer.pack

rechercher_label = tkinter.Label(fenetre, text="entrez votre recherche")
rechercher_label.grid(row=7, column=0)
rechercher_entry = tkinter.Entry(fenetre)
rechercher_entry.grid(row=7, column=1)

bouton_rechercher = tkinter.Button(fenetre,text="rechercher", command=rechercher)
bouton_rechercher.grid(row=8,column=1)
bouton_rechercher.pack

liste_de_recherche = tkinter.Listbox(fenetre, font="Arial 15", bg="#999595", width=30, )
liste_de_recherche.size()
liste_de_recherche.grid(row=9, column=0, columnspan=2, pady=10)

update()

fenetre.mainloop()