
# Here will be function of creating simple tkinter window with button
import tkinter as tk

def create_window():
    window = tk.Tk()
    window.title("Simple Tkinter Window")

    def on_button_click():
        print("Button clicked!")

    button = tk.Button(window, text="Click Me", command=on_button_click)
    button.pack(pady=20)

    window.mainloop()