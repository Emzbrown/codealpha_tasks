import os
import shutil


def organize_jpg_images(source_dir: str, destination_dir: str) -> None:
    """
    Moves all .jpg and .jpeg files from source_dir to destination_dir.
    """
    # Create destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        print(f"Created directory: {destination_dir}")

    # Track how many files are moved
    moved_count = 0

    # Iterate through all files in the source directory
    for filename in os.listdir(source_dir):
        # Check if the file ends with .jpg or .jpeg (case-insensitive)
        if filename.lower().endswith(('.jpg', '.jpeg')):
            source_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(destination_dir, filename)

            # Ensure it's a file and not a subdirectory
            if os.path.isfile(source_path):
                shutil.move(source_path, dest_path)
                print(f"Moved: {filename}")
                moved_count += 1

    print(f"\nTask Complete: Successfully moved {moved_count} image(s).")


# --- Usage Example ---
if __name__ == "__main__":
    SOURCE_FOLDER = "./downloads"       # Replace with your source folder path
    TARGET_FOLDER = "./images_archive"  # Replace with your destination folder path

    organize_jpg_images(SOURCE_FOLDER, TARGET_FOLDER)
