import tkinter


def convert():
    """Takes the value from the Entry widget mile_input, calculates it to the equivalent of kilometers and sets the
       text of the Label widget label_km_value to the roundet value. Takes no arguments and returns nothing."""
    label_km_value.config(text=round(float(mile_input.get()) * 1.609344, 2))


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

mile_input = tkinter.Entry(width=10)
mile_input.grid(row=0, column=1)

label_miles = tkinter.Label(text="Miles")
label_miles.grid(row=0, column=2)

label_equal = tkinter.Label(text="is equal to")
label_equal.grid(row=1, column=0)

label_km_value = tkinter.Label(text="0")
label_km_value.grid(row=1, column=1)

label_km = tkinter.Label(text="Km")
label_km.grid(row=1, column=2)

button_convert = tkinter.Button(text="Calculate", command=convert)
button_convert.grid(row=2, column=1)


window.mainloop()
