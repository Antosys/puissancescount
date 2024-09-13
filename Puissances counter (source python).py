
#             .__                                                                              __
#______  __ __|__| ______ ___________    ____   ____  ____   ______   ____  ____  __ __  _____/  |_
#\____ \|  |  \  |/  ___//  ___/\__  \  /    \_/ ___\/ __ \ /  ___/ _/ ___\/  _ \|  |  \/    \   __\
#|  |_> >  |  /  |\___ \ \___ \  / __ \|   |  \  \__\  ___/ \___ \  \  \__(  <_> )  |  /   |  \  |
#|   __/|____/|__/____  >____  >(____  /___|  /\___  >___  >____  >  \___  >____/|____/|___|  /__|
#|__|                 \/     \/      \/     \/     \/    \/     \/       \/                 \/
#___.                          __
#\_ |__ ___.__. _____    _____/  |_  ____
#| __ <   |  | \__  \  /    \   __\/  _ \
#| \_\ \___  |  / __ \|   |  \  | (  <_> )
#|___  / ____| (____  /___|  /__|  \____/
#    \/\/           \/     \/

# Ce programme ne nécessite que tkinter/customtk en raison de sa simplicité, toutefois celui-ci
# pourrait vous servir si vous en avez marre de taper "tableaux de puissances" sur internet :)
# Utilisation de l'IA pour réaliser le scroll personnalisé,
# je remercie CHATGPT pour m'avoir appris ces systèmes, j'utilisais les barres basiques de scroll qui ne
# charment pas spécialement l'utilisateur lors du lancement du .exe de ce fichier...

import customtkinter as ctk
from tkinter import messagebox, Toplevel

# configuration de l'apparence du thème
ctk.set_appearance_mode("dark")  # Mode sombre
ctk.set_default_color_theme("dark-blue")  # Couleur principale

# création de ma fenêtre principale, modifiable très simplement en cas de préférences
root = ctk.CTk()
root.geometry("770x500")
root.title("Calcul des puissances")


# Fonction pour générer les puissances et afficher dans mon tableau
def afficher_puissances():
    try:
        base = int(entry_base.get())  # Récupérer la base depuis l'entrée
        puissance_max = int(slider_puissance.get())  # Récupérer la valeur du slider
        for widget in frame_resultats.winfo_children():
            widget.destroy()  # Supprimer les anciens résultats quand reset
        # Ajouter les en têtes
        label_num = ctk.CTkLabel(frame_resultats, text="N°", width=100, anchor="w", fg_color="gray30", corner_radius=10)
        label_puissance = ctk.CTkLabel(frame_resultats, text=f"{base}^n", width=100, anchor="w", fg_color="gray30",
                                       corner_radius=10)
        label_resultat = ctk.CTkLabel(frame_resultats, text="Résultat", width=100, anchor="w", fg_color="gray30",
                                      corner_radius=10)
        label_num.grid(row=0, column=0, padx=10, pady=5)
        label_puissance.grid(row=0, column=1, padx=10, pady=5)
        label_resultat.grid(row=0, column=2, padx=10, pady=5)

        # Générer et afficher puissances avec calcul très basique, j'utilise ma boucle for et i pour mon calcul ainsi que ma numérotation
        for i in range(puissance_max + 1):
            label_index = ctk.CTkLabel(frame_resultats, text=f"{i + 1}", width=100, anchor="w")
            label_puissance = ctk.CTkLabel(frame_resultats, text=f"{base}^{i}", width=100, anchor="w")
            label_resultat = ctk.CTkLabel(frame_resultats, text=f"{base ** i}", width=100, anchor="w")
            label_index.grid(row=i + 1, column=0, padx=10, pady=5)
            label_puissance.grid(row=i + 1, column=1, padx=10, pady=5)
            label_resultat.grid(row=i + 1, column=2, padx=10, pady=5)

    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")


# Fonction pour réinitialiser le tableau
def reinitialiser():
    for widget in frame_resultats.winfo_children():
        widget.destroy()  # Supprimer tous les widgets dans le frame des résultats


# Fonction pour mettre à jour l'affichage de la valeur du slider
def update_slider_label(value):
    label_slider_value.configure(text=f"Puissance max : {int(value)}")


# Fonction pour la fenêtre d'entrée manuelle, en top
def ouvrir_fenetre_entree():
    top = Toplevel(root)
    top.title("Entrée manuelle")
    top.geometry("300x200")  # Agrandir la fenêtre pour le bouton de validation
    top.attributes("-alpha", 0.9)  # Transparence
    top.attributes("-topmost", True)  # Assurer que la fenêtre est au-dessus des autres
    top.configure(bg="gray20")

    def valider_entree():
        try:
            valeur = int(entry_manuel.get())
            if 0 <= valeur <= 20:
                slider_puissance.set(valeur)
                update_slider_label(valeur)
                top.destroy()
            else:
                messagebox.showerror("Erreur", "Afin d'éviter de charger trop de lignes, veuillez entrer une valeur entre 0 et 20.") # modifiable ligne 87 + modifier limite de la barre scroll si besoin
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre valide dans la fenêtre.")

    label = ctk.CTkLabel(top, text="Entrez la puissance maximale :", bg_color="gray20")
    label.pack(pady=10)

    entry_manuel = ctk.CTkEntry(top, width=100)
    entry_manuel.pack(pady=5)

    bouton_valider = ctk.CTkButton(top, text="Valider", command=valider_entree)
    bouton_valider.pack(pady=10)


# Créer un cadre pour les contrl
frame_controls = ctk.CTkFrame(root, fg_color="gray20")
frame_controls.pack(pady=20)

# Champ d'entrée pour choisir la base
label_base = ctk.CTkLabel(frame_controls, text="Choisissez la base : ", width=200)
label_base.grid(row=0, column=0, padx=10, pady=5)

entry_base = ctk.CTkEntry(frame_controls, width=100)
entry_base.insert(0, "2")  # Valeur par défaut
entry_base.grid(row=0, column=1, padx=10, pady=5)

# Créer un slider pour choisir la puissance maximale
label_slider = ctk.CTkLabel(frame_controls, text="Choisissez la puissance maximale", width=200)
label_slider.grid(row=1, column=0, padx=10, pady=5)

slider_puissance = ctk.CTkSlider(frame_controls, from_=0, to=20, number_of_steps=20, width=300,
                                 command=update_slider_label)
slider_puissance.set(10)
slider_puissance.grid(row=1, column=1, padx=10, pady=5)

# Affichage de la valeur du slider en tant que bouton click pour entrer (initialisé à 10 au début car c'est là où ma ligne se trouve)
label_slider_value = ctk.CTkButton(frame_controls, text="Puissance max : 10", width=200, command=ouvrir_fenetre_entree,
                                   fg_color="gray40")
label_slider_value.grid(row=1, column=2, padx=10, pady=5)

# Bouton pour générer les puissances en fonction des notions
btn_calculer = ctk.CTkButton(frame_controls, text="Calculer", command=afficher_puissances)
btn_calculer.grid(row=2, column=0, padx=10, pady=10)

# Bouton pour réinitialiser le tableau
btn_reinitialiser = ctk.CTkButton(frame_controls, text="Réinitialiser", command=reinitialiser, fg_color="gray")
btn_reinitialiser.grid(row=2, column=1, padx=10, pady=10)

# Créer un cadre avec une zone scrollable pour afficher les résultats
frame_scroll = ctk.CTkFrame(root)
frame_scroll.pack(fill="both", expand=True)

# Barre de défilement (customtk)
scrollbar = ctk.CTkScrollbar(frame_scroll, corner_radius=10, width=15)
scrollbar.pack(side="right", fill="y", padx=5)

# Créer un canvas pour permettre le scroll personnalisé
canvas = ctk.CTkCanvas(frame_scroll, yscrollcommand=scrollbar.set, background="gray20", highlightthickness=0)
canvas.pack(side="left", fill="both", expand=True)

scrollbar.configure(command=canvas.yview)

# Créer un frame dans le canva
frame_resultats = ctk.CTkFrame(canvas, fg_color="gray20")
canvas.create_window((0, 0), window=frame_resultats, anchor="nw")


# Mettre à jour la taille selon canva customtk
def update_canvas(event=None):
    canvas.configure(scrollregion=canvas.bbox("all"))


frame_resultats.bind("<Configure>", update_canvas)

# Ajout bas de page / crédit
footer = ctk.CTkLabel(root, text="Puissances count by anto", width=200, anchor="center", fg_color="gray20")
footer.pack(side="bottom", pady=10)

# Lancement
root.mainloop()
