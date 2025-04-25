import os
import hashlib
import tkinter as tk
from tkinter import filedialog
from InquirerPy import prompt
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box

console = Console()

def calculate_file_hash(file_path, hash_algorithm="sha256", chunk_size=4096):
    hash_func = getattr(hashlib, hash_algorithm)()
    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(chunk_size):
                hash_func.update(chunk)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    return hash_func.hexdigest()

def find_duplicates(directory):
    file_hashes = {}
    duplicates = {}

    print("\n🔍 Scanning directory and calculating file hashes...\n")

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Analyzing: {file_path}")
            file_hash = calculate_file_hash(file_path)
            
            if file_hash:
                if file_hash in file_hashes:
                    if file_hash not in duplicates:
                        duplicates[file_hash] = [file_hashes[file_hash]]
                    duplicates[file_hash].append(file_path)
                else:
                    file_hashes[file_hash] = file_path
    
    return duplicates

def show_duplicates(duplicates):
    choices = []
    for idx, (hash_val, files) in enumerate(duplicates.items(), start=1):
        display = f"{idx}. {len(files)} files - Hash: {hash_val[:12]}..."
        for file in files:
            display += f"\n   - {file}"
        choices.append({"name": display, "value": hash_val})
    
    return choices

def delete_duplicates(duplicates, selected_hashes):
    for selected_hash in selected_hashes:
        files_to_delete = duplicates[selected_hash][1:]
        for file in files_to_delete:
            try:
                os.remove(file)
                print(f"✅ Deleted: {file}")
            except Exception as e:
                print(f"❌ Failed to delete {file}: {e}")

def select_directory():
    root = tk.Tk()
    root.withdraw() 
    folder_selected = filedialog.askdirectory(title="📂 Select directory to scan for duplicates")
    return folder_selected
def print_header():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    title_text = Text("FILE DEDUPLICATOR", style="bold cyan", justify="center")
    subtitle = Text("A CLI tool to find and clean duplicate files", style="green", justify="center")
    author = Text("By: Entry Level ID", style="dim", justify="center")
    
    header_panel = Panel.fit(
        Text.assemble(title_text, "\n", subtitle, "\n", author),
        border_style="blue",
        box=box.ROUNDED,
        padding=(1, 4)
    )
    
    console.print(header_panel)

def main():
    print_header()
    while True:
        menu_question = [
            {
                "type": "list",
                "name": "menu_choice",
                "message": "📋 What would you like to do?",
                "choices": [
                    {"name": "🔍 Scan for duplicate files", "value": "scan"},
                    {"name": "❌ Exit", "value": "exit"}
                ]
            }
        ]
        menu = prompt(menu_question)

        if menu["menu_choice"] == "exit":
            print("👋 Exiting program. Goodbye!")
            break

        directory = select_directory()
        if not directory:
            print("❎ No directory selected. Returning to main menu...")
            continue

        duplicates = find_duplicates(directory)
        
        if not duplicates:
            print("\n🎉 No duplicate files found.")
            continue

        duplicate_choices = show_duplicates(duplicates)

        select_question = [
            {
                "type": "checkbox",
                "name": "hashes_to_delete",
                "message": "🧹 Select duplicate sets to clean (one file will be kept):",
                "choices": duplicate_choices,
            }
        ]
        selected = prompt(select_question)

        if selected["hashes_to_delete"]:
            confirm_question = [
                {
                    "type": "confirm",
                    "name": "confirm_delete",
                    "message": f"⚠️ Are you sure you want to delete selected duplicates?",
                    "default": False,
                }
            ]
            confirm = prompt(confirm_question)
            if confirm["confirm_delete"]:
                delete_duplicates(duplicates, selected["hashes_to_delete"])
            else:
                print("❎ Deletion cancelled.")
        else:
            print("No duplicate sets selected.")

        print("\n✅ Process completed. Returning to main menu...")

if __name__ == "__main__":
    main()
