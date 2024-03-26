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
            print("The JPG with metadata sucessfully deleted.")

        return new_path

    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

def convert_to_webp(directory_path, compression_percentage=10):
    try:
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            if os.path.isfile(file_path) and filename.startswith('_') and (filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg')):
                img = Image.open(file_path)
                title, _ = os.path.splitext(os.path.basename(file_path))
                new_path = os.path.join(os.path.dirname(file_path), f"{title}.webp")
                img.save(new_path, "WEBP", quality=compression_percentage)
                os.remove(file_path)
                print(f"Successfully converted {filename} to WebP (without metadata) & ALL JPG versions deleted.")
    except Exception as e:
        print(f"Error converting images to WebP: {e}")

def process_images_in_directory(directory_path, delete_original):
    converted_images = []
    
    # Check if the directory exists
    if not os.path.exists(directory_path):
        print(f"Directory '{directory_path}' does not exist.")
        return

    # Iterate through files in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Check if the file is an image with .webp or .jpg extension
        if os.path.isfile(file_path) and (filename.lower().endswith('.webp') or filename.lower().endswith('.jpg')):
            new_path = strip_metadata(file_path, delete_original)
            if new_path:
                converted_images.append(new_path)

    print("'°°°·.°·..·°¯°·._.··._.·°¯°·.·° .·°°°")
    print("'°°°·.°·..·°¯°·._.··._.·°¯°·.·° .·°°°")
    print("Success! Metadata Deleted from images.")
    print("Try converting to .webp to save space!")
    print("'°°°·.°·..·°¯°·._.··._.·°¯°·.·° .·°°°")
    print("'°°°·.°·..·°¯°·._.··._.·°¯°·.·° .·°°°")

    # Ask user if they want to convert JPEG/JPG files to WebP format
    convert_to_webp_option = input("Do you want to convert JPEG/JPG files to WebP format? (y/n): ").strip().lower()
    if convert_to_webp_option == 'y' or convert_to_webp_option == 'yes':
        for image_path in converted_images:
            convert_to_webp(os.path.dirname(image_path))

    print("'°°°·.°·..·°¯°·._.··._.·°¯°·.·° .·°°°")
    print("'°°°·.°·..·°¯°·._.··._.·°¯°·.·° .·°°°")
    print("Success! JPGs Converted to webp format.")
    print("https://github.com/noarche/photo-metadata-batch-cleaner")
    print("'°°°·.°·..·°¯°·._.··._.·°¯°·.·° .·°°°")
    print("'°°°·.°·..·°¯°·._.··._.·°¯°·.·° .·°°°")

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

