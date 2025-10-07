import re
import tkinter as tk
from tkinter import messagebox, simpledialog

IP_PATTERN = re.compile(
    r'\b(?:25[0-5]|2[0-4]\d|1?\d{1,2})\.'
    r'(?:25[0-5]|2[0-4]\d|1?\d{1,2})\.'
    r'(?:25[0-5]|2[0-4]\d|1?\d{1,2})\.'
    r'(?:25[0-5]|2[0-4]\d|1?\d{1,2})\b'
)

def find_ips():
    text = text_input.get("1.0", tk.END)
    ips = IP_PATTERN.findall(text)

    listbox.delete(0, tk.END)
    for ip in ips:
        listbox.insert(tk.END, ip)
    label_count.config(text=f"Found IP: {len(ips)}")

def delete_ip():
    selection = listbox.curselection()
    if not selection:
        messagebox.showwarning("Choose IP for deletion")
        return

    ip_to_delete = listbox.get(selection[0])
    text = text_input.get("1.0", tk.END)
    new_text = text.replace(ip_to_delete, "")
    text_input.delete("1.0", tk.END)
    text_input.insert(tk.END, new_text)

    find_ips()

def replace_ip():
    selection = listbox.curselection()
    if not selection:
        messagebox.showwarning("Choose IP for change")
        return

    old_ip = listbox.get(selection[0])
    new_ip = simpledialog.askstring("Change", f"Enter new IP in place of {old_ip}:")
    if not new_ip:
        return

    text = text_input.get("1.0", tk.END)
    new_text = text.replace(old_ip, new_ip)
    text_input.delete("1.0", tk.END)
    text_input.insert(tk.END, new_text)

    find_ips()

root = tk.Tk()
root.title("Find IP in text")

tk.Label(root, text="Enter text").pack()

text_input = tk.Text(root, height=10, width=60)
text_input.pack()

tk.Button(root, text="Find IPs", command=find_ips).pack(pady=5)

listbox = tk.Listbox(root, width=40, height=8)
listbox.pack()

label_count = tk.Label(root, text="Found Ips: 0")
label_count.pack()

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Button(frame, text="Delete IP", command=delete_ip).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Replace IP", command=replace_ip).grid(row=0, column=1, padx=5)

root.mainloop()
