import customtkinter as ctk
from logic_simulator import open_logic_simulator
from oscilloscope import open_oscilloscope

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("800x500")
app.title("EC Virtual Lab")

title = ctk.CTkLabel(
    app,
    text="EC Virtual Lab",
    font=("Arial", 30, "bold")
)
title.pack(pady=30)

logic_btn = ctk.CTkButton(
    app,
    text="Logic Gate Simulator",
    command=open_logic_simulator,
    width=250
)
logic_btn.pack(pady=10)

scope_btn = ctk.CTkButton(
    app,
    text="Virtual Oscilloscope",
    command=open_oscilloscope,
    width=250
)
scope_btn.pack(pady=10)

app.mainloop()