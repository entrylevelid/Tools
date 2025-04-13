# =============================================
#  Entry Level ID
# =============================================

import os
import shutil

source_folder = "C:/Users/Xbravo/Downloads"
extension_map = {
    "Images": [".jpg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".xlsx"],
    "Software": [".exe", ".msi"],
    "Archives": [".zip", ".rar", ".7z"]
}

for folder in extension_map.keys():
    os.makedirs(os.path.join(source_folder, folder), exist_ok=True)

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)
    if os.path.isfile(file_path):
        for folder, extensions in extension_map.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(source_folder, folder, file))
                break