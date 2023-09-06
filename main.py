import time
import winsound
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

# Initialize variables
start_time = None
running = False
timer_duration = 0  # Default timer duration in seconds

# Define light and dark themes
light_theme_settings = {
    "theme_name": "plastik",
    "bg_color": "white",
    "fg_color": "black",
    "button_bg": "lightgray",
    "button_fg": "black",
}

dark_theme_settings = {
    "theme_name": "black",
    "bg_color": "black",
    "fg_color": "white",
    "button_bg": "darkgray",
    "button_fg": "white",
}

current_theme = light_theme_settings  # Start with the light theme

def switch_theme():
    global current_theme
    if current_theme == light_theme_settings:
        current_theme = dark_theme_settings
    else:
        current_theme = light_theme_settings

    # Apply the selected theme
    style.set_theme(current_theme["theme_name"])
    label.config(bg=current_theme["bg_color"], fg=current_theme["fg_color"])
    for button in [start_button, stop_button, reset_button, start_stopwatch_button, stop_stopwatch_button,
                   reset_stopwatch_button, set_timer_button]:
        button.config(style=f"{current_theme['theme_name'].capitalize()}.TButton")

def start_timer():
    global start_time, running
    start_time = time.time()
    running = True
    update_timer()

def stop_timer():
    global running
    running = False

def reset_timer():
    global running, start_time
    running = False
    start_time = None
    label.config(text="00:00")

def update_timer():
    if running:
        elapsed_time = time.time() - start_time
        minutes, seconds = divmod(int(elapsed_time), 60)
        timer_display = f"{minutes:02}:{seconds:02}"
        label.config(text=timer_display)
        root.after(1000, update_timer)
        if elapsed_time >= timer_duration:
            stop_timer()
            label.config(text="Time's up!")
            winsound.Beep(1000, 1000)  # Beep sound for 1 second when the timer is up

def start_stopwatch():
    global running
    running = True
    update_stopwatch()

def stop_stopwatch():
    global running
    running = False

def reset_stopwatch():
    global running, start_time
    running = False
    start_time = time.time()
    label.config(text="00:00")

def update_stopwatch():
    if running:
        elapsed_time = time.time() - start_time
        minutes, seconds = divmod(int(elapsed_time), 60)
        stopwatch_display = f"{minutes:02}:{seconds:02}"
        label.config(text=stopwatch_display)
        root.after(1000, update_stopwatch)

def set_timer_duration():
    global timer_duration
    timer_duration = int(entry.get()) * 60  # Convert minutes to seconds
    label.config(text=f"Set Timer: {entry.get()} min")

root = tk.Tk()
root.title("Timer and Stopwatch")

# Create a ThemedStyle object for the root window
style = ThemedStyle(root)
style.set_theme(current_theme["theme_name"])

label = ttk.Label(root, text="00:00", font=("Arial", 24))
label.pack(pady=20)

# Configure the font for the button using the style
style.configure("TButton", font=("Arial", 10))

# Create the theme button with the configured style
theme_button = ttk.Button(root, text="Toggle", command=switch_theme, style="TButton")
theme_button.pack(side=tk.BOTTOM, padx=10, pady=10) 

# The button now simply says "Toggle" and is smaller in size

start_button = ttk.Button(root, text="Start Timer", command=start_timer, style=f"{current_theme['theme_name'].capitalize()}.TButton")
start_button.pack()
stop_button = ttk.Button(root, text="Stop Timer", command=stop_timer, style=f"{current_theme['theme_name'].capitalize()}.TButton")
stop_button.pack()
reset_button = ttk.Button(root, text="Reset Timer", command=reset_timer, style=f"{current_theme['theme_name'].capitalize()}.TButton")
reset_button.pack()

start_stopwatch_button = ttk.Button(root, text="Start Stopwatch", command=start_stopwatch, style=f"{current_theme['theme_name'].capitalize()}.TButton")
start_stopwatch_button.pack()
stop_stopwatch_button = ttk.Button(root, text="Stop Stopwatch", command=stop_stopwatch, style=f"{current_theme['theme_name'].capitalize()}.TButton")
stop_stopwatch_button.pack()
reset_stopwatch_button = ttk.Button(root, text="Reset Stopwatch", command=reset_stopwatch, style=f"{current_theme['theme_name'].capitalize()}.TButton")
reset_stopwatch_button.pack()

entry_label = ttk.Label(root, text="Set Timer Duration (minutes):")
entry_label.pack()
entry = ttk.Entry(root)
entry.pack()
set_timer_button = ttk.Button(root, text="Set Timer", command=set_timer_duration, style=f"{current_theme['theme_name'].capitalize()}.TButton")
set_timer_button.pack()

root.mainloop()