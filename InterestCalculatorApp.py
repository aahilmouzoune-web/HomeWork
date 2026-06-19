
import tkinter as tk
def calculate():
    p = float(ent_p.get())
    r = float(ent_r.get())
    t = float(ent_t.get())
    si = (p * r * t) / 100
    ci = p * (pow((1 + r / 100), t)) - p
    lbl_res.config(text=f"Simple: {si:.2f}\nCompound: {ci:.2f}")
root = tk.Tk()
root.title("Interest Calculator")
tk.Label(root, text="Principal:").pack()
ent_p = tk.Entry(root)
ent_p.pack()
tk.Label(root, text="Rate (%):").pack()
ent_r = tk.Entry(root)
ent_r.pack()
tk.Label(root, text="Time (Years):").pack()
ent_t = tk.Entry(root)
ent_t.pack()
tk.Button(root, text="Calculate", command=calculate).pack()
lbl_res = tk.Label(root, text="")
lbl_res.pack()
root.mainloop()