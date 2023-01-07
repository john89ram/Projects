import tkinter as tk

class Calculator(tk.Frame):
  def __init__(self, parent, *args, **kwargs):
    tk.Frame.__init__(self, parent, *args, **kwargs)
    self.parent = parent
    self.create_widgets()

  def create_widgets(self):
    self.entry = tk.Entry(self, width=30)
    self.entry.pack(side="top", fill="x")

    self.button_frame = tk.Frame(self)
    self.button_frame.pack(side="top", fill="x")

    buttons = [
        'C', '7', '8', '9', '+',
        '4', '5', '6', '-',
        '1', '2', '3', '*',
        '0', '/', '.', '='
    ]

    for index, button in enumerate(buttons):
      callback = lambda x=button: self.button_press(x)
      tk.Button(self.button_frame, text=button, width=5, command=callback).grid(row=index // 4, column=index % 4)

  def button_press(self, value):
    if value == "=":
      try:
        result = eval(self.entry.get())
        self.entry.delete(0, tk.END)
        self.entry.insert(0, result)
      except Exception as e:
        self.entry.delete(0, tk.END)
        self.entry.insert(0, "Error")
    elif value == "C":
      self.entry.delete(0, tk.END)
    else:
      self.entry.insert(tk.END, value)

if __name__ == "__main__":
  root = tk.Tk()
  root.title("Calculator")
  Calculator(root).pack(side="top", fill="both", expand=True)
  root.mainloop()