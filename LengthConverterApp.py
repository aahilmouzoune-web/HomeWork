import tkinter as tk
def convert_inches_to_cm():
    try:
        inches = float(entry_inches.get())
        cm = inches * 2.54
        label_result.config(text=f"{cm:.2f} cm", fg="black")
    except ValueError:
        label_result.config(text="Please enter a valid number", fg="red")
window = tk.Tk()
window.title("Length Converter App")
window.geometry("400x400")
title_label = tk.Label(window, text="Inches to Centimeters", font=("Arial", 14, "bold"))
title_label.pack(pady=20)
instruction_label = tk.Label(window, text="Enter length in inches:")
instruction_label.pack()
entry_inches = tk.Entry(window)
entry_inches.pack(pady=10)
convert_button = tk.Button(window, text="Convert", command=convert_inches_to_cm, bg="#4CAF50", fg="white")
convert_button.pack(pady=10)
label_result = tk.Label(window, text="", font=("Arial", 12))
label_result.pack(pady=20)
window.mainloop()