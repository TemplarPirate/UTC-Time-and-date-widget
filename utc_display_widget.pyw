import tkinter as tk
from datetime import datetime

def update_time():
    current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    label.config(text=current_time)
    root.after(1000, update_time)  # Update every second

# Set up the GUI
root = tk.Tk()
root.title("UTC Time Display")

# Make the background transparent
root.attributes('-alpha', 0.8)  # Adjust transparency (0.0 to 1.0)
root.attributes('-transparentcolor', 'black')  # Make black color transparent
root.overrideredirect(True)  # Remove the title bar

# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set up the label
label = tk.Label(root, font=("Helvetica", 20), bg="black", fg="lime", padx=45, pady=40)
label.pack()

# Calculate window size and position it on the right
window_width = 400  # Adjust based on your label size
window_height = 100  # Adjust based on your label size
x_position = screen_width - window_width - 10  # 10px padding from the right
y_position = 10 # vertically positioned top
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Make the window draggable
def move_window(event):
    root.geometry(f"+{event.x_root}+{event.y_root}")

label.bind("<B1-Motion>", move_window)

# Start the time update loop
update_time()

# Run the GUI event loop
root.mainloop()
