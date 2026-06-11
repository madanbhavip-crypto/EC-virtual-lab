import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt

def generate_wave():

    try:
        freq = float(freq_entry.get())

        t = np.linspace(0, 1, 1000)

        wave = np.sin(
            2 * np.pi * freq * t
        )

        plt.figure(figsize=(8,3))
        plt.plot(t, wave)
        plt.title("Virtual Oscilloscope")
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.grid(True)
        plt.show()

    except:
        print("Invalid Input")

def open_oscilloscope():

    global freq_entry

    window = ctk.CTkToplevel()

    window.title("Oscilloscope")
    window.geometry("400x300")

    ctk.CTkLabel(
        window,
        text="Frequency (Hz)"
    ).pack(pady=10)

    freq_entry = ctk.CTkEntry(window)
    freq_entry.pack()

    ctk.CTkButton(
        window,
        text="Generate Wave",
        command=generate_wave
    ).pack(pady=20)