import customtkinter as ctk
import string
import secrets
import re

def controlla_forza(password):
    if len(password) == 0:
        return "Inserisci una password", "gray", []

    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("• Usa almeno 8 caratteri")
    
    if len(password) >= 12:
        score += 1
    else:
        feedback.append("• Meglio se 12+ caratteri")
    
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("• Aggiungi lettere maiuscole")
    
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("• Aggiungi lettere minuscole")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("• Aggiungi numeri")
    
    if re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=]", password):
        score += 1
    else:
        feedback.append("• Aggiungi simboli speciali")

    if len(password) >= 16:
        score += 1
    
    if re.search(r"(123|abc|qwerty|password)", password.lower()):
        score -= 2
        feedback.append("⚠️ Evita sequenze comuni")

    if score <= 2:
        return "Debole 🔴", "#ff5555", feedback
    elif score <= 4:
        return "Media 🟡", "#ffb86c", feedback
    else:
        return "Forte 🟢", "#50fa7b", feedback

def genera_nuova_password(lunghezza=16, usa_simboli=True, usa_numeri=True, usa_maiuscole=True):
    caratteri = string.ascii_lowercase
    
    if usa_maiuscole:
        caratteri += string.ascii_uppercase
    if usa_numeri:
        caratteri += string.digits
    if usa_simboli:
        caratteri += string.punctuation
    
    password = []
    if usa_maiuscole:
        password.append(secrets.choice(string.ascii_uppercase))
    if usa_numeri:
        password.append(secrets.choice(string.digits))
    if usa_simboli:
        password.append(secrets.choice(string.punctuation))
    
    for i in range(lunghezza - len(password)):
        password.append(secrets.choice(caratteri))
    
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

def evento_controlla():
    pwd = entry_password.get()
    testo, colore, feedback = controlla_forza(pwd)
    label_risultato.configure(text=testo, text_color=colore)
    
    if feedback:
        label_feedback.configure(text="\n".join(feedback))
    else:
        label_feedback.configure(text="✅ Ottima password!")

def evento_mostra_password():
    if entry_password.cget("show") == "*":
        entry_password.configure(show="")
        btn_mostra.configure(text="🙈")
    else:
        entry_password.configure(show="*")
        btn_mostra.configure(text="👁️")

def evento_genera():
    lunghezza = int(slider_lunghezza.get())
    usa_simboli = check_simboli.get()
    usa_numeri = check_numeri.get()
    usa_maiuscole = check_maiuscole.get()
    
    nuova_pwd = genera_nuova_password(lunghezza, usa_simboli, usa_numeri, usa_maiuscole)
    entry_generata.delete(0, "end")
    entry_generata.insert(0, nuova_pwd)
    
    label_lunghezza.configure(text=f"Lunghezza: {lunghezza} caratteri")
    
    testo, colore, _ = controlla_forza(nuova_pwd)
    label_forza_gen.configure(text=f"Forza: {testo}", text_color=colore)

def evento_copia():
    pwd = entry_generata.get()
    if pwd:
        app.clipboard_clear()
        app.clipboard_append(pwd)
        app.update()
        label_copia_status.configure(text="✅ Copiata negli appunti!", text_color="#50fa7b")
        app.after(2000, lambda: label_copia_status.configure(text=""))
    else:
        label_copia_status.configure(text="⚠️ Genera prima una password", text_color="#ffb86c")
        app.after(2000, lambda: label_copia_status.configure(text=""))

def evento_cancella():
    entry_password.delete(0, "end")
    entry_generata.delete(0, "end")
    label_risultato.configure(text="...")
    label_feedback.configure(text="")
    label_forza_gen.configure(text="")
    label_copia_status.configure(text="")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("450x700")
app.title("Password Security Tool Pro")
app.resizable(False, False)

lbl_title = ctk.CTkLabel(app, text="🔐 Password Security Tool", font=("Roboto", 26, "bold"))
lbl_title.pack(pady=20)

frame_check = ctk.CTkFrame(app, corner_radius=15)
frame_check.pack(pady=10, padx=20, fill="x")

lbl_info = ctk.CTkLabel(frame_check, text="Controlla la tua password:", font=("Arial", 16, "bold"))
lbl_info.pack(pady=10)

frame_entry = ctk.CTkFrame(frame_check, fg_color="transparent")
frame_entry.pack(pady=5)

entry_password = ctk.CTkEntry(frame_entry, placeholder_text="Inserisci password...", width=250, show="*", height=35)
entry_password.pack(side="left", padx=5)

btn_mostra = ctk.CTkButton(frame_entry, text="👁️", width=40, command=evento_mostra_password)
btn_mostra.pack(side="left")

btn_check = ctk.CTkButton(frame_check, text="🔍 Verifica Sicurezza", command=evento_controlla, height=35)
btn_check.pack(pady=10)

label_risultato = ctk.CTkLabel(frame_check, text="...", font=("Arial", 18, "bold"))
label_risultato.pack(pady=5)

label_feedback = ctk.CTkLabel(frame_check, text="", font=("Arial", 11), justify="left")
label_feedback.pack(pady=5, padx=10)

frame_gen = ctk.CTkFrame(app, corner_radius=15)
frame_gen.pack(pady=20, padx=20, fill="x")

lbl_gen = ctk.CTkLabel(frame_gen, text="Genera password sicura:", font=("Arial", 16, "bold"))
lbl_gen.pack(pady=10)

label_lunghezza = ctk.CTkLabel(frame_gen, text="Lunghezza: 16 caratteri", font=("Arial", 12))
label_lunghezza.pack(pady=5)

slider_lunghezza = ctk.CTkSlider(frame_gen, from_=8, to=32, number_of_steps=24, width=250,
                                  command=lambda v: label_lunghezza.configure(text=f"Lunghezza: {int(v)} caratteri"))
slider_lunghezza.set(16)
slider_lunghezza.pack(pady=5)

frame_opzioni = ctk.CTkFrame(frame_gen, fg_color="transparent")
frame_opzioni.pack(pady=10)

check_maiuscole = ctk.CTkCheckBox(frame_opzioni, text="Maiuscole (A-Z)")
check_maiuscole.select()
check_maiuscole.pack(side="left", padx=10)

check_numeri = ctk.CTkCheckBox(frame_opzioni, text="Numeri (0-9)")
check_numeri.select()
check_numeri.pack(side="left", padx=10)

check_simboli = ctk.CTkCheckBox(frame_opzioni, text="Simboli (!@#)")
check_simboli.select()
check_simboli.pack(side="left", padx=10)

btn_gen = ctk.CTkButton(frame_gen, text="🎲 Genera Password", fg_color="#2ecc71", 
                        hover_color="#27ae60", command=evento_genera, height=35, font=("Arial", 14, "bold"))
btn_gen.pack(pady=10)

entry_generata = ctk.CTkEntry(frame_gen, placeholder_text="Password generata apparirà qui", width=300, height=35)
entry_generata.pack(pady=5)

label_forza_gen = ctk.CTkLabel(frame_gen, text="", font=("Arial", 12, "bold"))
label_forza_gen.pack(pady=5)

frame_azioni = ctk.CTkFrame(frame_gen, fg_color="transparent")
frame_azioni.pack(pady=5)

btn_copia = ctk.CTkButton(frame_azioni, text="📋 Copia", command=evento_copia, width=100, 
                          fg_color="#3498db", hover_color="#2980b9")
btn_copia.pack(side="left", padx=5)

btn_cancella = ctk.CTkButton(frame_azioni, text="🗑️ Cancella", command=evento_cancella, width=100,
                             fg_color="#e74c3c", hover_color="#c0392b")
btn_cancella.pack(side="left", padx=5)

label_copia_status = ctk.CTkLabel(frame_gen, text="", font=("Arial", 11))
label_copia_status.pack(pady=5)

lbl_footer = ctk.CTkLabel(app, text="💡 Consiglio: usa password diverse per ogni account!", 
                          font=("Arial", 10), text_color="gray")
lbl_footer.pack(pady=10)

app.mainloop()
