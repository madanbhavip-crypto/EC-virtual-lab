import customtkinter as ctk

def calculate():

    try:
        a = int(entry_a.get())
        b = int(entry_b.get())

        gate = gate_menu.get()

        if gate == "AND":
            result = a & b

        elif gate == "OR":
            result = a | b

        elif gate == "XOR":
            result = a ^ b

        elif gate == "NAND":
            result = int(not (a & b))

        elif gate == "NOR":
            result = int(not (a | b))

        output.configure(text=f"Output = {result}")

    except:
        output.configure(text="Enter 0 or 1")

def open_logic_simulator():

    global entry_a
    global entry_b
    global gate_menu
    global output

    window = ctk.CTkToplevel()

    window.title("Logic Simulator")
    window.geometry("400x400")

    ctk.CTkLabel(window,text="Input A").pack(pady=5)

    entry_a = ctk.CTkEntry(window)
    entry_a.pack()

    ctk.CTkLabel(window,text="Input B").pack(pady=5)

    entry_b = ctk.CTkEntry(window)
    entry_b.pack()

    gate_menu = ctk.CTkComboBox(
        window,
        values=["AND","OR","XOR","NAND","NOR"]
    )
    gate_menu.pack(pady=10)

    ctk.CTkButton(
        window,
        text="Calculate",
        command=calculate
    ).pack(pady=10)

    output = ctk.CTkLabel(window,text="")
    output.pack()