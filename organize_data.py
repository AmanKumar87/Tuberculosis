# organize_data.py

import os
import shutil

# --- Configuration ---
# The path to your original, unorganized data folder
original_data_path = "Data"

# The path to the new, clean data folder we want to create
clean_data_path = "data"

# Define the source folders and their target class
source_map = {
    "normal": "Normal",
    "normal chest x-rays": "Normal",
    "Tuberculosis": "Tuberculosis",
    "TB Chest X-rays": "Tuberculosis"
}

print("--- Starting Data Consolidation ---")

# --- Create the new directory structure ---
normal_dest = os.path.join(clean_data_path, "Normal")
tb_dest = os.path.join(clean_data_path, "Tuberculosis")

os.makedirs(normal_dest, exist_ok=True)
os.makedirs(tb_dest, exist_ok=True)

print(f"Created clean directory structure at: '{clean_data_path}'")

# --- Move files from source to destination ---
total_moved = 0
for source_folder, dest_class in source_map.items():
    source_path = os.path.join(original_data_path, source_folder)
    
    if not os.path.isdir(source_path):
        print(f"Warning: Source folder not found, skipping: '{source_path}'")
        continue

    files_to_move = [f for f in os.listdir(source_path) if os.path.isfile(os.path.join(source_path, f))]
    
    if not files_to_move:
        print(f"No files found in '{source_path}', skipping.")
        continue

    print(f"Moving {len(files_to_move)} files from '{source_folder}' to '{dest_class}'...")
    
    # Determine the destination path
    destination_path = normal_dest if dest_class == "Normal" else tb_dest
    
    # Move each file
    for file_name in files_to_move:
        shutil.move(os.path.join(source_path, file_name), os.path.join(destination_path, file_name))
        total_moved += 1

print(f"\n--- Consolidation Complete ---")
print(f"Total files moved: {total_moved}")
print(f"Your data is now organized in the '{clean_data_path}' directory.")