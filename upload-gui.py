import tkinter as tk
from tkinter import filedialog
import pandas as pd

def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        data = pd.read_csv(file_path)
        print(data)  # Print the data to the console (can be modified to display in the UI)

# Create the main window
root = tk.Tk()
root.title("CSV File Upload")

# Create an upload button
upload_button = tk.Button(root, text="Upload CSV", command=upload_file)
upload_button.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()
