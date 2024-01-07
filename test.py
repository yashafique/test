import tkinter as tk
from tkinter import messagebox


def message():
    messagebox.showinfo("Happy holidays!!")


def main():
    root = tk.Tk()
    root.title('title')
    button = tk.Button(root, text="Click button", command=message)
    button.pack(pady=20)

    root.mainloop()


if __name__ == '__main__':
    main()
