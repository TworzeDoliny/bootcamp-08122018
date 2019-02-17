import tkinter
from tkinter import messagebox

def oblicz():
    try:
        a = float(cena_entry.get())
        b = float(spalanie_entry.get())
        c = float(dystans_entry.get())
        wynik = a*b*c/100
        wynik_label.configure(text=f"Za podróz zapłacisz: {wynik}")
    except ValueError:
        messagebox.showerror("Błędne dane", "Popraw dane - powinny być liczbami")

root = tkinter.Tk()
root.columnconfigure(1, weight=1)

cena_label = tkinter.Label(master=root, text="Cena za litr benzyny: ")
cena_label.grid(row=0, column=0)
cena_entry = tkinter.Entry(master=root)
cena_entry.grid(row=0, column=1)

spalanie_label = tkinter.Label(master=root, text="Spalanie samochodu na 100km: ")
spalanie_label.grid(row=1, column=0)
spalanie_entry = tkinter.Entry(master=root)
spalanie_entry.grid(row=1, column=1)

dystans_label = tkinter.Label(master=root, text="Przebyty dystans: ")
dystans_label.grid(row=2, column=0)
dystans_entry = tkinter.Entry(master=root)
dystans_entry.grid(row=2, column=1)


button = tkinter.Button(master=root, text="Przelicz", command=oblicz)
button.grid(row=3, column=1)

wynik_label = tkinter.Label(master=root, text="-")
wynik_label.grid(row=4, column=1)

root.mainloop()

