import os
import sys
from PIL import Image
import tkinter as tk
from tkinter import filedialog

def compress_image(input_path, quality=80):
    try:
        img = Image.open(input_path)
        original_size = os.path.getsize(input_path) / 1024

        dir_name, file_name = os.path.split(input_path)
        name, ext = os.path.splitext(file_name)
        output_path = os.path.join(dir_name, f"{name}_compressed{ext}")

        img.save(output_path, optimize=True, quality=quality)

        compressed_size = os.path.getsize(output_path)/ 1024
        reduction = ((original_size - compressed_size) / original_size) * 100

        print(f"Image compressed: {file_name}")
        print(f"Original: {original_size:.2f} KB")
        print(f"Compressed: {compressed_size:.2f} KB")
        print(f"Reduction: {reduction:.2f}%")
        print(f"Saved to: {output_path}")

        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    file_paths = filedialog.askopenfilenames(
        title="Select images to compress",
        filetypes=[("Image files", "*.jpg *.jpeg *.png"), ("All files", "*.*")]
    )

    quality = 75

    count = 0
    for file_path in file_paths:
        if compress_image(file_path, quality):
            count += 1

    print(f"\nCompressed {count} images with quality level {quality}.")