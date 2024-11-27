import tkinter as tk
import time
import random

def fake_hacker_attack():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg='black')

    label = tk.Label(root, text="Hacking in progress...", font=("Courier", 30), fg="green", bg="black")
    label.pack(pady=50)

    output = tk.Text(root, bg="black", fg="green", font=("Courier", 12), height=20, width=80)
    output.pack(pady=20)

    hack_phrases = [
        "[+] Establishing connection to target...",
        "[+] Connection established!",
        "[+] Downloading sensitive files...",
        "[+] Accessing system data...",
        "[+] Injecting malware...",
        "[+] Target files successfully compromised!",
        "[+] Transmitting data to server...",
        "[!] ERROR: Target is aware of the breach!",
        "[+] Initiating self-destruct protocol...",
        "[!] Connection lost!"
    ]

    def simulate_hacking():
        for phrase in hack_phrases:
            time.sleep(random.uniform(1, 3))  # Random delay to mimic real-time hacking
            output.insert(tk.END, f"{phrase}\n")
            output.see(tk.END)
            root.update()

        output.insert(tk.END, "\n[!] Just kidding! It's a prank!\n")
        output.see(tk.END)
        time.sleep(5)
        root.quit()

    root.after(1000, simulate_hacking)

    root.mainloop()

fake_hacker_attack()

