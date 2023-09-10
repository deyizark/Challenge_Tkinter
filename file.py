import tkinter as tk

file = tk.Tk()
file.geometry("550x450")
file.title("File_Editor")
file["bg"] = "gray"

def save():
    text = text_box.get("1.0", "end-1c")
    print(text)
    name = text_name.get("1.0", "end-1c")
    
    if text == '' or text == " " or name == "" or name == " ":
        save_label.config(text="Statut: Fichye a pa gen kontni oubyen ou pa mete non")
    else:
        with open(name, "w") as file:
            file.write(text)
        print()
        save_label.config(text="Statut: Tèks la anrejistre ak siksè")
afich = tk.Message(file, text="Tape kontni a nan gwo chan an epi non fiche a nan ti piti a.", width=250).pack()

text_box = tk.Text(file, height=15, width=65)
text_box.config(font=("Calibri", 14))
text_box.place(x=10, y=40)

text_name = tk.Text(file, height=1, width=55, font=("Calibri", 14))
text_name.place(x=10, y=360)

save_label = tk.Label(file, text="Statut:____")
save_label.place(x=10, y=335)

save_button = tk.Button(file, text="Anrejistre", relief="raised", command=save)
save_button.place(x=470, y=360)
file.mainloop()