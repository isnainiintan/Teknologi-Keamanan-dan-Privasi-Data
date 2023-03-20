import tkinter as tk

class SubstitutionCipherGUI:
    def __init__(self, master):
        self.master = master
        master.title('Substitution Cipher')

        self.input_label = tk.Label(master, text='Plain Text:')
        self.input_label.pack()

        self.input_text = tk.Entry(master, width=50)
        self.input_text.pack()

        self.key_label = tk.Label(master, text='Key:')
        self.key_label.pack()

        self.key_text = tk.Entry(master, width=50)
        self.key_text.insert(0, 'zywvutsrqponmlkjihgfedcba')
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
        key = self.key_text.get()
        cipher_text = self.substitution_cipher(plain_text, key)
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.END, cipher_text)

    def decrypt(self):
        cipher_text = self.input_text.get()
        key = self.key_text.get()
        plain_text = self.substitution_cipher(cipher_text, key, inverse=True)
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.END, plain_text)

    def substitution_cipher(self, text, key, inverse=False):
        if not inverse:
            table = str.maketrans('zywvutsrqponmlkjihgfedcba', key)
        else:
            table = str.maketrans(key, 'zywvutsrqponmlkjihgfedcba')
        return text.translate(table)

root = tk.Tk()
cipher_gui = SubstitutionCipherGUI(root)
root.mainloop()

