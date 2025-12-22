import customtkinter as ctk
import string
import secrets
import re # Per le espressioni regolari (controllo pattern)

# --- LOGICA DEL PROGRAMMA ---

def controlla_forza(password):
    """
    Controlla la forza della password e restituisce un punteggio e un colore.
    """
    score = 0
    feedback = []
    
    if len(password) == 0:
        return "Inserisci una password", "gray"

    # Criteri di valutazione
    if len(password) >= 8: score += 1
    if len(password) >= 12: score += 1
    if re.search(r"[A-Z]", password): score += 1 # Cerca Maiuscole
    if re.search(r"[a-z]", password): score += 1 # Cerca Minuscole
    if re.search(r"\d", password): score += 1    # Cerca Numeri
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): score += 1 # Cerca Simboli

    # Risultato basato sul punteggio
    if score <= 2:
        return "Debole 🔴", "#ff5555" # Rosso
    elif score <= 4:
        return "Media 🟡", "#ffb86c" # Giallo/Arancio
    else:
        return "Forte 🟢", "#50fa7b" # Verde

def genera_nuova_password():
    """Genera una password casuale sicura di 16 caratteri"""
    alfabeto = string.ascii_letters + string.digits + string.punctuation
    # secrets.choice è più sicuro di random.choice per le password
    password = ''.join(secrets.choice(alfabeto) for i in range(16))
    return password

# --- INTERFACCIA GRAFICA (GUI) ---

def evento_controlla():
    pwd = entry_password.get()
    testo, colore = controlla_forza(pwd)
    label_risultato.configure(text=testo, text_color=colore)

def evento_genera():
    nuova_pwd = genera_nuova_password()
    entry_generata.delete(0, "end") # Pulisce il campo
    entry_generata.insert(0, nuova_pwd) # Inserisce la nuova pass
    # Copia anche negli appunti (opzionale, simulato qui)
    print(f"Password generata: {nuova_pwd}") 

# Setup Finestra principale
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x450")
app.title("Password Security Tool")

# TITOLO
lbl_title = ctk.CTkLabel(app, text="🔐 Password Tool", font=("Roboto", 24, "bold"))
lbl_title.pack(pady=20)

# SEZIONE 1: CHECKER
frame_check = ctk.CTkFrame(app)
frame_check.pack(pady=10, padx=20, fill="x")

lbl_info = ctk.CTkLabel(frame_check, text="Controlla la tua password:", font=("Arial", 14))
lbl_info.pack(pady=5)

entry_password = ctk.CTkEntry(frame_check, placeholder_text="Scrivi qui...", width=200, show="*") # show="*" nasconde i caratteri
entry_password.pack(pady=5)

btn_check = ctk.CTkButton(frame_check, text="Verifica Sicurezza", command=evento_controlla)
btn_check.pack(pady=10)

label_risultato = ctk.CTkLabel(frame_check, text="...", font=("Arial", 16, "bold"))
label_risultato.pack(pady=10)

# SEZIONE 2: GENERATOR
frame_gen = ctk.CTkFrame(app)
frame_gen.pack(pady=20, padx=20, fill="x")

lbl_gen = ctk.CTkLabel(frame_gen, text="Oppure generane una sicura:", font=("Arial", 14))
lbl_gen.pack(pady=5)

entry_generata = ctk.CTkEntry(frame_gen, placeholder_text="Password generata", width=250)
entry_generata.pack(pady=5)

btn_gen = ctk.CTkButton(frame_gen, text="Genera Password 🎲", fg_color="green", hover_color="darkgreen", command=evento_genera)
btn_gen.pack(pady=10)

# Avvio
app.mainloop()
