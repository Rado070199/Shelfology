import tkinter as tk
from tkinter import messagebox, ttk
import json

class BookManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Zarządzanie Książkami w Bibliotece")
        self.create_widgets()
        self.books = []  # Lista do przechowywania książek

    def create_widgets(self):
        # Tworzenie nagłówka
        header_frame = tk.Frame(self.root)
        header_frame.pack(pady=10)

        tk.Label(header_frame, text="Tytuł").grid(row=0, column=0, padx=5)
        tk.Label(header_frame, text="Autor").grid(row=0, column=1, padx=5)
        tk.Label(header_frame, text="Rok Wydania").grid(row=0, column=2, padx=5)
        tk.Label(header_frame, text="Gatunek").grid(row=0, column=3, padx=5)

        # Pola do wprowadzania danych
        self.title_entry = tk.Entry(header_frame, width=20)
        self.title_entry.grid(row=1, column=0, padx=5)

        self.author_entry = tk.Entry(header_frame, width=20)
        self.author_entry.grid(row=1, column=1, padx=5)

        self.year_entry = tk.Entry(header_frame, width=10)
        self.year_entry.grid(row=1, column=2, padx=5)

        self.genre_entry = tk.Entry(header_frame, width=15)
        self.genre_entry.grid(row=1, column=3, padx=5)

        # Przycisk do dodawania książki
        add_button = tk.Button(header_frame, text="Dodaj Książkę", command=self.add_book)
        add_button.grid(row=1, column=4, padx=5)

        # Tabela do wyświetlania książek
        self.tree = ttk.Treeview(self.root, columns=("title", "author", "year", "genre"), show='headings')
        self.tree.pack(pady=10)

        # Ustawienie nagłówków kolumn
        self.tree.heading("title", text="Tytuł")
        self.tree.heading("author", text="Autor")
        self.tree.heading("year", text="Rok Wydania")
        self.tree.heading("genre", text="Gatunek")

        # Przyciski do zarządzania książkami
        remove_button = tk.Button(self.root, text="Usuń Wybraną Książkę", command=self.remove_book)
        remove_button.pack(pady=5)

        save_button = tk.Button(self.root, text="Zapisz do Pliku", command=self.save_to_file)
        save_button.pack(pady=5)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        year = self.year_entry.get()
        genre = self.genre_entry.get()

        if title and author and year and genre:
            self.books.append({"title": title, "author": author, "year": year, "genre": genre})
            self.tree.insert("", tk.END, values=(title, author, year, genre))
            self.clear_entries()
        else:
            messagebox.showwarning("Uwaga", "Wszystkie pola muszą być wypełnione.")

    def clear_entries(self):
        # Czyści pola wprowadzania
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.genre_entry.delete(0, tk.END)

    def remove_book(self):
        selected_item = self.tree.selection()
        if selected_item:
            for item in selected_item:
                self.tree.delete(item)
                # Usuń książkę z listy
                del self.books[int(item)]  # Usunięcie z listy książek
        else:
            messagebox.showwarning("Uwaga", "Wybierz książkę do usunięcia.")

    def save_to_file(self):
        with open("books.json", "w") as file:
            json.dump(self.books, file)
        messagebox.showinfo("Zapisano", "Dane zostały zapisane do pliku books.json")

# Uruchomienie aplikacji
if __name__ == "__main__":
    root = tk.Tk()
    app = BookManager(root)
    root.mainloop()
