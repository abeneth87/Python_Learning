import tkinter as tk

def miles_to_km():
    miles = float(miles_entry.get())
    kilometers = round(miles * 1.60934)
    result_label.config(text=f"{miles} miles is equal to {kilometers:.2f} kilometers")

# Create the main window
window = tk.Tk()
window.title("Miles to Kilometers Converter")

# Create and place labels
miles_label = tk.Label(text="Enter Miles:")
miles_label.grid(column=0, row=0)

result_label = tk.Label(text="")
result_label.grid(column=0, row=2)

# Create an entry field
miles_entry = tk.Entry(width=20)
miles_entry.grid(column=1, row=0)

# Create a button
calculate_button = tk.Button(text="Convert", command=miles_to_km)
calculate_button.grid(column=1, row=1)

# Start the tkinter main loop
window.mainloop()
