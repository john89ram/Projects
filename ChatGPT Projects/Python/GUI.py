import tkinter as tk

# Create the main window
window = tk.Tk()

# Set the window size
window.geometry("500x500")  # width x height

# Create a text box
text_box = tk.Entry(window, width=50)
text_box.pack()

# Create a button
button = tk.Button(window, text="Click me!")
button.pack()

# Run the Tkinter event loop
window.mainloop()