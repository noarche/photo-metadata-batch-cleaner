from PIL import Image
import os

def strip_metadata(image_path, delete_original):
    try:
        # Open the image
        img = Image.open(image_path)

        # Strip metadata
        img_without_metadata = Image.new("RGB", img.size)
        img_without_metadata.paste(img)

        # Get the image title without extension
        title, extension = os.path.splitext(os.path.basename(image_path))

        # Save the image without metadata with "_" added to the title
        new_path = os.path.join(os.path.dirname(image_path), f"_{title}{extension}")
        img_without_metadata.save(new_path)

        print(f"Metadata stripped and saved as: {new_path}")

        # Delete the original file if requested
        if delete_original:
            os.remove(image_path)
            print("Original file deleted.")

    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def process_images_in_directory(directory_path, delete_original):
    # Check if the directory exists
    if not os.path.exists(directory_path):
        print(f"Directory '{directory_path}' does not exist.")
        return

    # Iterate through files in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Check if the file is an image with .webp or .jpg extension
        if os.path.isfile(file_path) and (filename.lower().endswith('.webp') or filename.lower().endswith('.jpg')):
            strip_metadata(file_path, delete_original)

def main():
    # Prompt user for the directory path
    directory_path = input("Enter the directory path with images: ").strip()

    # Ask user if they want to delete the original files
    delete_original = input("Do you want to delete the original files? (y/n): ").strip().lower()
    delete_original = delete_original == 'y' or delete_original == 'yes'

    # Process images in the specified directory
    process_images_in_directory(directory_path, delete_original)

if __name__ == "__main__":
    main()
