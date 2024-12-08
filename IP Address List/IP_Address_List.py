import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

DATABASE = 'ip_address.db'

def connect():
    return sqlite3.connect(DATABASE)

def initialize_database():
    conn = connect()
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE IF NOT EXISTS ip_address (
                     name TEXT NOT NULL,
                     ip TEXT NOT NULL UNIQUE)''')
        conn.commit()
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Error initializing database: {e}")
    finally:
        conn.close()

def tampilkan_semua_ip():
    conn = connect()
    c = conn.cursor()
    try:
        c.execute("SELECT name, ip FROM ip_address")
        rows = c.fetchall()
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Error fetching IP addresses: {e}")
        rows = []
    finally:
        conn.close()
    return rows

def tambah_ip(name, ip):
    conn = connect()
    c = conn.cursor()
    try:
        c.execute("INSERT INTO ip_address (name, ip) VALUES (?, ?)", (name, ip))
        conn.commit()
        messagebox.showinfo("Success", "IP Address berhasil ditambahkan.")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "IP Address sudah ada.")
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Error adding IP address: {e}")
    finally:
        conn.close()

def edit_ip(old_ip, new_name, new_ip):
    conn = connect()
    c = conn.cursor()
    try:
        c.execute("UPDATE ip_address SET name = ?, ip = ? WHERE ip = ?", (new_name, new_ip, old_ip))
        conn.commit()
        messagebox.showinfo("Success", "IP Address berhasil diperbarui.")
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Error editing IP address: {e}")
    finally:
        conn.close()

def hapus_ip(ip):
    conn = connect()
    c = conn.cursor()
    try:
        c.execute("DELETE FROM ip_address WHERE ip = ?", (ip,))
        conn.commit()
        messagebox.showinfo("Success", "IP Address berhasil dihapus.")
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Error deleting IP address: {e}")
    finally:
        conn.close()

def cari_berdasarkan_nama(name):
    conn = connect()
    c = conn.cursor()
    try:
        c.execute("SELECT name, ip FROM ip_address WHERE name LIKE ?", ('%' + name + '%',))
        rows = c.fetchall()
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Error searching by name: {e}")
        rows = []
    finally:
        conn.close()
    return rows

def cari_berdasarkan_ip(ip):
    conn = connect()
    c = conn.cursor()
    try:
        c.execute("SELECT name, ip FROM ip_address WHERE ip LIKE ?", ('%' + ip + '%',))
        rows = c.fetchall()
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Error searching by IP: {e}")
        rows = []
    finally:
        conn.close()
    return rows

class IPManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("IP Address Manager")
        self.root.configure(bg='black')

        self.tabControl = ttk.Notebook(root)
        self.tab_ip = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab_ip, text="IP Address")
        self.tabControl.pack(expand=1, fill="both")

        style = ttk.Style()
        style.configure('TNotebook.Tab', background='gray20', foreground='white')
        style.configure('TFrame', background='black')
        style.configure('Treeview', background='black', foreground='white', fieldbackground='gray20')
        style.configure('Treeview.Heading', background='gray20', foreground='black')
        style.map('Treeview', background=[('selected', 'gray30')])

        initialize_database()

        self.create_ip_tab()

        self.footer_label = tk.Label(root, text="KenkyoAdrian @2024", bg='black', fg='white', font=('Arial', 10))
        self.footer_label.pack(side=tk.BOTTOM, pady=10)

    def create_ip_tab(self):
        self.ip_tree = ttk.Treeview(self.tab_ip, columns=("Name", "IP"), show='headings')
        self.ip_tree.heading("Name", text="Name", command=self.sort_by_name)
        self.ip_tree.heading("IP", text="IP Address")
        self.ip_tree.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky='nsew')

        self.btn_add_ip = tk.Button(self.tab_ip, text="Add IP Address", command=self.add_ip, bg='gray30', fg='white')
        self.btn_add_ip.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

        self.btn_edit_ip = tk.Button(self.tab_ip, text="Edit IP Address", command=self.edit_ip, bg='gray30', fg='white')
        self.btn_edit_ip.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

        self.btn_delete_ip = tk.Button(self.tab_ip, text="Delete IP Address", command=self.delete_ip, bg='gray30', fg='white')
        self.btn_delete_ip.grid(row=1, column=2, padx=10, pady=10, sticky='ew')

        self.btn_search_by_name = tk.Button(self.tab_ip, text="Search by Name", command=self.search_by_name, bg='gray30', fg='white')
        self.btn_search_by_name.grid(row=1, column=3, padx=10, pady=10, sticky='ew')

        self.btn_search_by_ip = tk.Button(self.tab_ip, text="Search by IP", command=self.search_by_ip, bg='gray30', fg='white')
        self.btn_search_by_ip.grid(row=1, column=4, padx=10, pady=10, sticky='ew')

        self.tab_ip.grid_columnconfigure(0, weight=1)
        self.tab_ip.grid_columnconfigure(1, weight=1)
        self.tab_ip.grid_columnconfigure(2, weight=1)
        self.tab_ip.grid_columnconfigure(3, weight=1)
        self.tab_ip.grid_columnconfigure(4, weight=1)

        self.refresh_ip_list()

    def refresh_ip_list(self):
        for row in self.ip_tree.get_children():
            self.ip_tree.delete(row)
        try:
            ips = tampilkan_semua_ip()
            sorted_ips = sorted(ips, key=lambda x: x[0]) 
            for ip in sorted_ips:
                self.ip_tree.insert("", "end", values=ip)
        except Exception as e:
            messagebox.showerror("Error", f"Error refreshing IP list: {e}")

    def add_ip(self):
        name = simpledialog.askstring("Input", "Enter Name:")
        ip = simpledialog.askstring("Input", "Enter IP Address:")
        if name and ip:
            tambah_ip(name, ip)
            self.refresh_ip_list()

    def edit_ip(self):
        selected_item = self.ip_tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Select an IP Address to edit.")
            return
        old_ip = self.ip_tree.item(selected_item, 'values')[1]
        new_name = simpledialog.askstring("Input", "Enter new Name:")
        new_ip = simpledialog.askstring("Input", "Enter new IP Address:")
        if new_name and new_ip:
            edit_ip(old_ip, new_name, new_ip)
            self.refresh_ip_list()

    def delete_ip(self):
        selected_item = self.ip_tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Select an IP Address to delete.")
            return
        ip = self.ip_tree.item(selected_item, 'values')[1]
        hapus_ip(ip)
        self.refresh_ip_list()

    def search_by_name(self):
        name = simpledialog.askstring("Input", "Enter Name to Search:")
        if name:
            results = cari_berdasarkan_nama(name)
            self.display_search_results(results)

    def search_by_ip(self):
        ip = simpledialog.askstring("Input", "Enter IP Address to Search:")
        if ip:
            results = cari_berdasarkan_ip(ip)
            self.display_search_results(results)

    def display_search_results(self, results):
        if not results:
            messagebox.showinfo("Search Results", "No records found.")
            return
        
        search_window = tk.Toplevel(self.root)
        search_window.title("Search Results")
        search_window.configure(bg='black')

        tree = ttk.Treeview(search_window, columns=("Name", "IP"), show='headings')
        tree.heading("Name", text="Name", command=lambda: self.sort_tree_by_name(tree))
        tree.heading("IP", text="IP Address")
        tree.pack(fill=tk.BOTH, expand=True)

        style = ttk.Style()
        style.configure('Treeview', background='black', foreground='white', fieldbackground='gray20')
        style.configure('Treeview.Heading', background='gray20', foreground='black')
        style.map('Treeview', background=[('selected', 'gray30')])

        sorted_results = sorted(results, key=lambda x: x[0])
        for row in sorted_results:
            tree.insert("", "end", values=row)

        button_frame = tk.Frame(search_window, bg='black')
        button_frame.pack(pady=10)

        edit_button = tk.Button(button_frame, text="Edit", command=lambda: self.edit_search_result(tree), bg='gray30', fg='white')
        edit_button.pack(side=tk.LEFT, padx=10)

        delete_button = tk.Button(button_frame, text="Delete", command=lambda: self.delete_search_result(tree), bg='gray30', fg='white')
        delete_button.pack(side=tk.LEFT, padx=10)

        close_button = tk.Button(search_window, text="Close", command=search_window.destroy, bg='gray30', fg='white')
        close_button.pack(pady=10)

    def edit_search_result(self, tree):
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Select an IP Address to edit.")
            return
        old_ip = tree.item(selected_item, 'values')[1]
        new_name = simpledialog.askstring("Input", "Enter new Name:")
        new_ip = simpledialog.askstring("Input", "Enter new IP Address:")
        if new_name and new_ip:
            edit_ip(old_ip, new_name, new_ip)
            self.refresh_ip_list()

    def delete_search_result(self, tree):
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Select an IP Address to delete.")
            return
        ip = tree.item(selected_item, 'values')[1]
        hapus_ip(ip)
        self.refresh_ip_list()

    def sort_by_name(self):
        self.sort_tree_by_name(self.ip_tree)

    def sort_tree_by_name(self, tree):
        # Get all items
        items = list(tree.get_children())
        # Sort items by Name
        sorted_items = sorted(items, key=lambda i: tree.item(i, 'values')[0])
        # Re-insert sorted items
        for index, item in enumerate(sorted_items):
            tree.move(item, '', index)

if __name__ == "__main__":
    root = tk.Tk()
    app = IPManagerApp(root)
    root.mainloop()
