import tkintes


window = tkinter.Tk()
window.title("Miles to KM")
window.minsize(width=200, height=100)
window.config(padx=30, pady=30)


def calculate_fun():
    output_entry["text"] = float(input_entry.get()) * 1.609344


# Button
calculate_button = tkinter.Button(text="Calculate", command=calculate_fun).grid(column=1, row=3)

# Label
equal_label = tkinter.Label(text="is equal to").grid(column=0, row=1)
miles_label = tkinter.Label(text="Miles").grid(column=2, row=0)
km_label = tkinter.Label(text="Km").grid(column=2, row=1)
output_entry = tkinter.Label(text="0")
output_entry.grid(column=1, row=1)

# Entry
input_entry = tkinter.Entry(width=7)
input_entry.grid(column=1, row=0)















window.mainloop()
