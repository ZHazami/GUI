import tkinter as tk
from tkinter import ttk, messagebox

# --- 1. PHYSICS ENGINE ---
SPEED_OF_LIGHT = 299792458  # m/s

def calculate_wavelength(velocity, frequency):
    if frequency <= 0:
        raise ValueError("Frequency must be greater than zero.")
    if velocity < 0:
        raise ValueError("Wave speed cannot be negative.")
    return velocity / frequency  # Returns result in meters

# --- 2. GUI ACTIONS ---
def set_speed_of_light():
    entry_velocity.delete(0, tk.END)
    entry_velocity.insert(0, str(SPEED_OF_LIGHT))

def on_calculate():
    try:
        v = float(entry_velocity.get())
        f = float(entry_frequency.get())
        
        wavelength_m = calculate_wavelength(v, f)
        
        # Unit conversion
        selected_unit = unit_var.get()
        if selected_unit == "Nanometers (nm)":
            final_val = wavelength_m * 1e9
            unit_symbol = "nm"
        elif selected_unit == "Millimeters (mm)":
            final_val = wavelength_m * 1e3
            unit_symbol = "mm"
        else:
            final_val = wavelength_m
            unit_symbol = "m"

        # Format output cleanly (uses scientific notation for very large/small numbers)
        label_result.config(text=f"λ = {final_val:.4g} {unit_symbol}", fg="#0055aa")
        
    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid input:\n{e}")

def on_clear():
    entry_velocity.delete(0, tk.END)
    entry_frequency.delete(0, tk.END)
    label_result.config(text="λ = --", fg="black")

# --- 3. GUI LAYOUT ---
root = tk.Tk()
root.title("Wavelength Calculator")
root.geometry("360x310")
root.resizable(False, False)

# Header & Formula
tk.Label(root, text="Wave Wavelength Calculator", font=("Arial", 14, "bold")).pack(pady=(15, 2))
tk.Label(root, text="Formula: λ = v / f", font=("Arial", 11, "italic"), fg="gray").pack(pady=(0, 15))

# Velocity Input Frame
frame_v = tk.Frame(root)
frame_v.pack(pady=5)
tk.Label(frame_v, text="Wave Speed v (m/s):", width=18, anchor="e").grid(row=0, column=0, padx=5)
entry_velocity = tk.Entry(frame_v, width=15)
entry_velocity.grid(row=0, column=1)

# Helper button for light speed
tk.Button(root, text="Use Speed of Light (c)", font=("Arial", 8), command=set_speed_of_light).pack(pady=(0, 8))

# Frequency Input Frame
frame_f = tk.Frame(root)
frame_f.pack(pady=5)
tk.Label(frame_f, text="Frequency f (Hz):", width=18, anchor="e").grid(row=0, column=0, padx=5)
entry_frequency = tk.Entry(frame_f, width=15)
entry_frequency.grid(row=0, column=1)

# Output Unit Selector
frame_u = tk.Frame(root)
frame_u.pack(pady=8)
tk.Label(frame_u, text="Output Unit:", width=18, anchor="e").grid(row=0, column=0, padx=5)
unit_var = tk.StringVar(value="Meters (m)")
unit_dropdown = ttk.Combobox(frame_u, textvariable=unit_var, state="readonly", width=13,
                             values=["Meters (m)", "Millimeters (mm)", "Nanometers (nm)"])
unit_dropdown.grid(row=0, column=1)

# Buttons Frame
frame_btn = tk.Frame(root)
frame_btn.pack(pady=15)
tk.Button(frame_btn, text="Calculate", width=12, bg="#d0e8ff", command=on_calculate).grid(row=0, column=0, padx=5)
tk.Button(frame_btn, text="Clear", width=10, command=on_clear).grid(row=0, column=1, padx=5)

# Result Display
label_result = tk.Label(root, text="λ = --", font=("Arial", 14, "bold"))
label_result.pack(pady=5)

root.mainloop()
