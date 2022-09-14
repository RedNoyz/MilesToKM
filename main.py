import tkinter

import sv_ttk

window = tkinter.Tk()
window.title("GUI Program")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)

sv_ttk.set_theme("dark")

km_entry = tkinter.Entry()
km_entry.grid(column=1, row=0)
km_entry.config(width=10)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

converted_km_label = tkinter.Label(text="0")
converted_km_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)


def calculate_miles_to_km():
    miles = km_entry.get()
    km = int(miles) * 1.6
    converted_km_label.config(text=int(km))


calculate_button = tkinter.Button(text="Calculate", command=calculate_miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
