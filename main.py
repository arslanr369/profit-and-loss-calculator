import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Profit and Loss Calculator")

# Create the main frame
frame = tk.Frame(window)
frame.pack()

# Create the labels for the input fields
tk.Label(frame, text="Sales:").pack()
tk.Label(frame, text="Cost of Goods Sold:").pack()

# Create the input fields
sales_entry = tk.Entry(frame)
cost_entry = tk.Entry(frame)

# Pack the input fields
sales_entry.pack()
cost_entry.pack()

# Create the calculate button
def calculate():
  # Get the values from the input fields
  sales = float(sales_entry.get())
  cost = float(cost_entry.get())

  # Calculate the profit or loss
  profit = sales - cost

  # Set the result label text
  if profit > 0:
    result_label.config(text=f"Profit: ${profit:.2f}")
  else:
    result_label.config(text=f"Loss: ${-profit:.2f}")

calculate_button = tk.Button(frame, text="Calculate", command=calculate)
calculate_button.pack()

# Create the result label
result_label = tk.Label(frame, text="")
result_label.pack()

# Run the main loop
window.mainloop()
