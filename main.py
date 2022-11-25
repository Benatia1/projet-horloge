from tkinter import *
import time
from datetime import datetime
from pytz import timezone

master = Tk()

master.title("Clock")
master.geometry("500x700+0+0")
master.config(bg="black")


def RecuperHeure():
    h = str(time.strftime("%H:%M:%S"))
    format = "%H:%M:%S"
    now_utc = datetime.now(timezone('UTC'))
    now_asia = now_utc.astimezone(timezone('Asia/Hong_Kong')).strftime(format)
    now_newy = now_utc.astimezone(
        timezone('America/New_York')).strftime(format)

    j = str(time.strftime("%A"))  # récuperer le jour
    jj = str(time.strftime("%d %B %Y"))  # récuperer la date d'aujourd'hui

    lbl_heure.config(text=h)
    lbl_jour.config(text=j)
    lbl_jourDet.config(text=jj)
    lbl_Nheure.config(text=now_asia)
    lbl_Newheure.config(text=now_newy)

    # la méthode after permet d'executer le traitement apres 200 millisecondes.
    lbl_heure.after(200, RecuperHeure)


# case pour stocker le jour
lbl_jour = Label(master, text="Mardi", font=(
    "times new roman", 20, "bold"), bg="black", foreground="white")
lbl_jour.place(x=10, y=5, width=340, height=50)
# case pour stocker la date courant
lbl_jourDet = Label(master, text="Détaille", font=(
    "times new roman", 20, "bold"), bg="black", foreground="white")
lbl_jourDet.place(x=0, y=45, width=350, height=50)
# (text=12) pour la taille du text et font pour définir le type de police et le mettre en gras par bold
lbl_heure = Label(master, text="12", font=(
    "times new roman", 50, "bold"), bg="green")
lbl_heure.place(x=10, y=100, width=300, height=90)
# emplacement d'heur minute et seconde
heure = Label(master, text="Heure", font=(
    "times new roman", 15, "bold"), bg="green")
heure.place(x=10, y=200, width=108, height=30)
Minute = Label(master, text="Minute", font=(
    "times new roman", 15, "bold"), bg="green")
Minute.place(x=120, y=200, width=78, height=30)
Seconde = Label(master, text="Seconde", font=(
    "times new roman", 15, "bold"), bg="green")
Seconde.place(x=200, y=200, width=110, height=30)
# Nom du Pays
lbl_Hong_Kong = Label(master, text="Hong-Kong time", font=(
    "times new roman", 20, "bold"), bg="black", foreground="white")
lbl_Hong_Kong.place(x=10, y=240, width=195, height=70)

# case pour stocké l'heure Hors UE exactement Hong-Kong
lbl_Nheure = Label(master, text="11", font=(
    "times new roman", 50, "bold"), bg="Yellow")
lbl_Nheure.place(x=10, y=300, width=300, height=90)
# emplacement d'heure minute et seconde
Nheure = Label(master, text="Heure", font=(
    "times new roman", 15, "bold"), bg="Yellow")
Nheure.place(x=10, y=400, width=108, height=30)
NMinute = Label(master, text="Minute", font=(
    "times new roman", 15, "bold"), bg="Yellow")
NMinute.place(x=120, y=400, width=78, height=30)
NSeconde = Label(master, text="Seconde", font=(
    "times new roman", 15, "bold"), bg="Yellow")
NSeconde.place(x=200, y=400, width=110, height=30)
# case pour stocké l'heure Hors UE exactement New-York
lbl_Newheure = Label(master, text="New-York Time",
                     font=("times new roman", 50, "bold"), bg="red")
lbl_Newheure.place(x=10, y=500, width=300, height=90)
# placer le nom du pays
lbl_New_York = Label(master, text="New-York time", font=(
    "times new roman", 20, "bold"), bg="black", foreground="white")
lbl_New_York.place(x=10, y=450, width=190, height=30)
# placement d'heure minute et seconde
Newyheure = Label(master, text="Heure", font=(
    "times new roman", 15, "bold"), bg="red")
Newyheure.place(x=10, y=600, width=108, height=30)
NewyMinute = Label(master, text="Minute", font=(
    "times new roman", 15, "bold"), bg="red")
NewyMinute.place(x=120, y=600, width=78, height=30)
NewySeconde = Label(master, text="Seconde", font=(
    "times new roman", 15, "bold"), bg="red")
NewySeconde.place(x=200, y=600, width=110, height=30)

RecuperHeure()
master.mainloop()
