import tkinter as tk
from tkinter import messagebox

def encrypt(plaintext, key):
    ciphertext = ''
    for i in range(len(plaintext)):
        # Calculate the shift for the current character based on the key
        shift = ord(key[i % len(key)]) - 48
        # Shift the current character by the calculated amount
        ciphertext += chr((ord(plaintext[i]) + shift - 97) % 26 + 97)
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    for i in range(len(ciphertext)):
        # Calculate the shift for the current character based on the key
        shift = ord(key[i % len(key)]) - 48
        # Shift the current character by the calculated amount
        plaintext += chr((ord(ciphertext[i]) - shift - 97) % 26 + 97)
    return plaintext

def submit():
    plaintext = plaintext_entry.get()
    key = "147"
    ciphertext = encrypt(plaintext, key)
    ciphertext_entry.delete(0, tk.END)
    ciphertext_entry.insert(0, ciphertext)

def clear():
    plaintext_entry.delete(0, tk.END)
    ciphertext_entry.delete(0, tk.END)

def show_decrypt():
    ciphertext = ciphertext_entry.get()
    key = "147"
    plaintext = decrypt(ciphertext, key)
    messagebox.showinfo("Decrypted Text", plaintext)

# Create GUI
window = tk.Tk()
window.title("Vigenere Cipher")
window.geometry("400x200")

# Create labels
plaintext_label = tk.Label(window, text="Plaintext:")
plaintext_label.grid(row=0, column=0, padx=5, pady=5)

ciphertext_label = tk.Label(window, text="Ciphertext:")
ciphertext_label.grid(row=1, column=0, padx=5, pady=5)

# Create entries
plaintext_entry = tk.Entry(window, width=30)
plaintext_entry.grid(row=0, column=1, padx=5, pady=5)

ciphertext_entry = tk.Entry(window, width=30)
ciphertext_entry.grid(row=1, column=1, padx=5, pady=5)

# Create buttons
submit_button = tk.Button(window, text="Encrypt", command=submit)
submit_button.grid(row=2, column=0, padx=5, pady=5)

decrypt_button = tk.Button(window, text="Decrypt", command=show_decrypt)
decrypt_button.grid(row=2, column=1, padx=5, pady=5)

clear_button = tk.Button(window, text="Clear", command=clear)
clear_button.grid(row=3, column=0, padx=5, pady=5)

exit_button = tk.Button(window, text="Exit", command=window.quit)
exit_button.grid(row=3, column=1, padx=5, pady=5)

window.mainloop()





