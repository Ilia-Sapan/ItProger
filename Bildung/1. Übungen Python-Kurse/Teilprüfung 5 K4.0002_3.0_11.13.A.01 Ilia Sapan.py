#-------------------------------------------
# Dateiname: Quiz_app.py
# Autor: Ilia Sapan
# Python3 (K4.0002_3.0_VZ)
# Matrikelnummer
# 399644000031193700
# # Letzte Änderung: 14.02.2025, 08:40 AM
#-------------------------------------------

# Wir importieren nötige Bibliothken
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
import threading
import json

# Fragenlist für Harry_Potter_QUIZ
quiz_fragen = [
    {
        "frage": "Wie heißt die Schule, die Harry Potter besucht?",
        "optionen": ["A) Durmstrang", "B) Beauxbatons", "C) Hogwarts", "D) Ilvermorny"],
        "antwort": "C"
    },
    {
        "frage": "Welches Tier ist das Symbol des Hauses Gryffindor?",
        "optionen": ["A) Schlange", "B) Löwe", "C) Adler", "D) Dachs"],
        "antwort": "B"
    },
    {
        "frage": "Wie lautet der Zauberspruch, um einen Patronus zu beschwören?",
        "optionen": ["A) Lumos", "B) Expelliarmus", "C) Expecto Patronum", "D) Avada Kedavra"],
        "antwort": "C"
    }
]

# Global Variablen
current_question_index = 0  # Frage Index
user_answers = []  # List für User-Antworten
timer_seconds = 30  # Menge der Sekunden
timer_running = False  # Timer-Flag

# Funktion für die neue Frage
def load_question():
    global current_question_index, timer_seconds, timer_running
    if current_question_index < len(quiz_fragen):  # Wir prüfen, ob es noch Fragen gibt
        question_data = quiz_fragen[current_question_index]
        question_label.config(text=question_data["frage"])  # Wir erneuern Fragen

        # Wir erneuern Antwortvarianten
        for i in range(4):
            radio_buttons[i].config(text=question_data["optionen"][i], value=question_data["optionen"][i])

        var.set(None)  # den Timer zurücksetzen
        timer_seconds = 30  # den Timer zurücksetzen zu 30 Sek.
        timer_running = True  # Timer beginnt sich
        threading.Thread(target=update_timer, daemon=True).start()  # Starten Sie den Timer in einem separaten Thread
    else:
        messagebox.showinfo("Quiz beendet", "Das Quiz ist vorbei!")
        btn_erg_sp.config(state=tk.NORMAL)  # Unblocked Button bon Speichern

# Funktion für Button Nächste Frage
def next_question():
    global current_question_index
    if var.get():  # Wir prüfen, ob das Antwort gewält wurde
        user_answers.append({
            "frage": quiz_fragen[current_question_index]["frage"],
            "gewaehlt": var.get(),
            "korrekt": quiz_fragen[current_question_index]["antwort"] == var.get()
        })
        current_question_index += 1
        load_question()
    else:
        messagebox.showwarning("Fehler", "Bitte wähle eine Antwort aus!")

# Timer Funktion
def update_timer():
    global timer_seconds, timer_running
    if timer_seconds > 0 and timer_running:
        timer_seconds -= 1
        timer_label.config(text=f"Die Zeit ist: {timer_seconds} Sek.")
        fenster.after(1000, update_timer)
    elif timer_seconds == 0:
        timer_label.config(text="Zeit ist vorbei!")

# Start Timer Funktion
def start_timer():
    global timer_running, timer_seconds
    timer_seconds = 30  # Timer zurück
    timer_running = True
    update_timer()

# Speichern Funktion
def save_results():
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, "w") as f:
            json.dump(user_answers, f, indent=4)
        messagebox.showinfo("Gespeichert", "Ergebnisse wurden gespeichert!")

# Loading Funktion
def load_results():
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, "r") as f:
            data = json.load(f)
        messagebox.showinfo("Geladene Ergebnisse", f"Geladene Daten: {json.dumps(data, indent=4)}")

fenster = Tk()
fenster.title("Harry Potter Quiz \u26A1")
fenster.geometry('800x600')
fenster.configure(bg='#C4A484')
fenster.resizable(False,False)

# Fragen
question_label = Label(fenster,
              text = "Frage",
              font=('Old English Text MT', 20),
              justify='center',
              bg='#C4A484')

# Frames
button_frame = Frame(fenster, bg='#C4A484')
button_frame.pack(side='bottom', fill='x', pady=50)

# Radiobuttons variablen
var = StringVar()
radio_buttons = []
for i in range(4):
    rb = tk.Radiobutton(button_frame,
                        text="",
                        variable=var,
                        value="",
                        bg = "red",
                        relief = "raised",
                        font=("Old English Text MT", 15))
    rb.pack(anchor="center", padx=20, pady = 20)
    radio_buttons.append(rb)


 # Timers
timer_label = Label(fenster,
                    text=f"Zeit: {timer_seconds} Sek",
                    font=("Old English Text MT", 15),
                    fg="red",
                    bg = '#C4A484')
timer_label.pack(pady=10)

# Buttons
btn_erg_sp = Button(button_frame,
                    text="Ergebnisse speichern",
                    bg="grey",
                    fg = "black",
                    height=2,
                    command=save_results,
                    relief="solid",
                    font=('Old English Text MT', 15))

btn_next_fr = Button(button_frame,
                     text="Nächste Frage",
                     bg="grey",
                     fg = "black",
                     height=2,
                     command=next_question,
                     relief="solid",
                     font=('Old English Text MT', 15))

load_results_button = Button(button_frame,
                             text="Ergebnisse laden",
                             command=load_results,
                             bg="grey",
                             fg = "black",
                             height=2,
                             relief="solid",
                             font=('Old English Text MT', 15))

load_question()

load_results_button.pack(side='left', padx=50)
btn_erg_sp.pack(side='left', padx=50)
btn_next_fr.pack(side='right', padx=50)
question_label.pack(side = 'top')
fenster.mainloop()