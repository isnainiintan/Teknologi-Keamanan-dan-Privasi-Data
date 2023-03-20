import tkinter as tk
from tkinter import messagebox

def encrypt(plaintext, key):
    # Create empty list to hold the ciphertext
    ciphertext = [''] * key
    # Loop through each character in the plaintext
    for i in range(len(plaintext)):
        # Calculate the index of the ciphertext list to add the character to
        index = i % key
        # Add the character to the correct position in the list
        ciphertext[index] += plaintext[i]
    # Combine the characters in the list to create the final ciphertext
    return ''.join(ciphertext)

def decrypt(ciphertext, key):
    # Calculate the number of columns in the grid
    columns = len(ciphertext) // key
    # Create an empty grid to hold the plaintext
    grid = [[''] * columns for i in range(key)]
    # Loop through each character in the ciphertext
    for i in range(len(ciphertext)):
        # Calculate the row and column of the grid to add the character to
        row = i % key
        column = i // key
        # Add the character to the correct position in the grid
        grid[row][column] = ciphertext[i]
    # Combine the characters in each row of the grid to create the final plaintext
    plaintext = ''
    for row in grid:
        plaintext += ''.join(row)
    return plaintext

def submit():
    plaintext = plaintext_entry.get()
    key = int(key_entry.get())
    ciphertext = encrypt(plaintext, key)
    ciphertext_entry.delete(0, tk.END)
    ciphertext_entry.insert(0, ciphertext)

def clear():
    plaintext_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)
    ciphertext_entry.delete(0, tk.END)

def show_decrypt():
    ciphertext = ciphertext_entry.get()
    key = int(key_entry.get())
    plaintext = decrypt(ciphertext, key)
    messagebox.showinfo("Decrypted Text", plaintext)

# Create GUI
window = tk.Tk()
window.title("Transposition Cipher")
window.geometry("400x200")

# Create labels
plaintext_label = tk.Label(window, text="Plaintext:")
plaintext_label.grid(row=0, column=0, padx=5, pady=5)

key_label = tk.Label(window, text="Key:")
key_label.grid(row=1, column=0, padx=5, pady=5)

ciphertext_label = tk.Label(window, text="Ciphertext:")
ciphertext_label.grid(row=2, column=0, padx=5, pady=5)

# Create entries
plaintext_entry = tk.Entry(window, width=30)
plaintext_entry.grid(row=0, column=1, padx=5, pady=5)

key_entry = tk.Entry(window, width=30)
key_entry.grid(row=1, column=1, padx=5, pady=5)

ciphertext_entry = tk.Entry(window, width=30)
ciphertext_entry.grid(row=2, column=1, padx=5, pady=5)

# Create buttons
submit_button = tk.Button(window, text="Encrypt", command=submit)
submit_button.grid(row=3, column=0, padx=5, pady=5)

decrypt_button = tk.Button(window, text="Decrypt", command=show_decrypt)
decrypt_button.grid(row=3, column=1, padx=5, pady=5)

clear_button = tk.Button(window, text="Clear", command=clear)
clear_button.grid(row=3, column=2, padx=5, pady=5)

window.mainloop()
