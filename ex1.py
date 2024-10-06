# run "python ex1.py dst" in a directory of ex1.py

import os
import shutil
import argparse
from pathlib import Path

def copy_files_by_extension(src_dir, dest_dir):
    try:
        Path(dest_dir).mkdir(parents=True, exist_ok=True)
        
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)

            if os.path.isdir(item_path):
                new_dest_dir = os.path.join(dest_dir, os.path.basename(item_path))
                copy_files_by_extension(item_path, new_dest_dir)
            elif os.path.isfile(item_path):
                file_extension = Path(item).suffix[1:]
                extension_dir = os.path.join(dest_dir, file_extension)

                Path(extension_dir).mkdir(parents=True, exist_ok=True)
                shutil.copy2(item_path, extension_dir)

                print(f"Copied {item} to {extension_dir}")
    except Exception as e:
        print(f"Error processing {src_dir}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Copy files and sort by extension")
    parser.add_argument('src_dir', type=str, help="Path to the source directory")
    parser.add_argument('dest_dir', type=str, nargs='?', default='dist', help="Path to the destination directory ('dist' by default)")

    args = parser.parse_args()

    src_dir = args.src_dir
    dest_dir = args.dest_dir

    if not os.path.exists(src_dir):
        print(f"Source directory '{src_dir}' does not exist.")
        return

    print(f"Copying files from '{src_dir}' to '{dest_dir}' and sorting by file extension...")
    copy_files_by_extension(src_dir, dest_dir)
    print("File copying and sorting completed.")

if __name__ == "__main__":
    main()
