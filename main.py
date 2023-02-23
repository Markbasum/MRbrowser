import tkinter as tk
from tkinter import messagebox as msg
from search_engine import GoogleSearchEngine

class GoogleSearchEngineGUI:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Google Search Engine")
        self.root.geometry("800x600")
        self.root.resizable(0, 0)
        self.root.configure(background='#f2f2f2')
        self.version_label = tk.Label(self.root, text='Version 0.1 BETA', fg='gray', bg='#f2f2f2', anchor='se')
        self.version_label.pack(side=tk.RIGHT, padx=10, pady=10)
        self.create_widgets()
        self.search_engine = GoogleSearchEngine(self.show_search_results)

    def create_widgets(self):
        self.search_label = tk.Label(self.root, text="Google Search", font=("Helvetica", 20), fg="black", bg="#f2f2f2")
        self.search_label.pack(side=tk.TOP, pady=50)

        self.search_entry = tk.Entry(self.root, width=50, font=("Helvetica", 16), fg="black", bg="white")
        self.search_entry.pack(side=tk.TOP, pady=20)

        self.search_button = tk.Button(self.root, text="Search", font=("Helvetica", 16), fg="white", bg="blue", command=self.search)
        self.search_button.pack(side=tk.TOP, pady=20)

    def search(self):
        query = self.search_entry.get()
        if not query:
            msg.showwarning("Empty query", "Please enter a search query.")
            return
        self.search_engine.search(query)

    def show_search_results(self, search_results):
        result_window = tk.Toplevel(self.root)
        result_window.title("Search Results")
        result_frame = tk.Frame(result_window)
        result_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        for result in search_results:
            link = result['link']
            title = result['title']
            description = result['description']
            result_label = tk.Label(result_frame, text=title, fg='blue', cursor='hand2')
            result_label.pack(side=tk.TOP, anchor='w')
            result_label.bind('<Button-1>', lambda e, url=link: self.search_engine.open_url(url))
            desc_label = tk.Label(result_frame, text=description, wraplength=600, justify=tk.LEFT)
            desc_label.pack(side=tk.TOP, anchor='w', padx=20)

if __name__ == '__main__':
    app = GoogleSearchEngineGUI()
    app.root.mainloop()
