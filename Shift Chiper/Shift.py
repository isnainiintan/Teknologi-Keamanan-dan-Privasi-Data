import tkinter as tk
from string import ascii_lowercase, ascii_uppercase

class ShiftCipherGUI:
    def __init__(self, master):
        self.master = master
        master.title('Shift Cipher')

        self.input_label = tk.Label(master, text='Plain Text:')
        self.input_label.pack()

        self.input_text = tk.Entry(master, width=50)
        self.input_text.pack()

        self.key_label = tk.Label(master, text='Key:')
        self.key_label.pack()

        self.key_text = tk.Entry(master, width=50)
        self.key_text.insert(0, '47')
        self.key_text.pack()

        self.encrypt_button = tk.Button(master, text='Encrypt', command=self.encrypt)
        self.encrypt_button.pack()

        self.decrypt_button = tk.Button(master, text='Decrypt', command=self.decrypt)
        self.decrypt_button.pack()

        self.output_label = tk.Label(master, text='Result:')
        self.output_label.pack()

        self.output_text = tk.Text(master, width=50, height=10)
        self.output_text.pack()

    def encrypt(self):
        plain_text = self.input_text.get()
        shift = int(self.key_text.get())
        cipher_text = self.shift_cipher(plain_text, shift)
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.END, cipher_text)

    def decrypt(self):
        cipher_text = self.input_text.get()
        shift = int(self.key_text.get())
        plain_text = self.shift_cipher(cipher_text, -shift)
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.END, plain_text)

    def shift_cipher(self, text, shift):
        alphabet = ascii_lowercase + ascii_uppercase
        shifted_alphabet = alphabet[shift:] + alphabet[:shift]
        table = str.maketrans(alphabet, shifted_alphabet)
        return text.translate(table)

root = tk.Tk()
cipher_gui = ShiftCipherGUI(root)
root.mainloop()

