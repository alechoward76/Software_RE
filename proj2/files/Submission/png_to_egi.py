# Alec Howard
# 2/12/2024
# File Reversal

from PIL import Image, ImageDraw
import numpy as np


def user_input():
    """Get the file path from the user"""
    user_input = input("Enter a file path: ")
    return str(user_input)


def get_number_of_images():
    """Get the number of images in the file"""
    num_files = input("Enter the number of images: ")
    return int(num_files)


def output_name():
    """Get the name of the output file"""
    name = input("Enter the name of the output file: ")
    return name


def file_read(file):
    """Read in file bytes and create an array of bytes"""
    img = Image.open(file)
    img = img.convert("RGB")
    pixel_data = list(img.getdata())
    width, height = img.size
    return pixel_data, width, height


def set_header(num_images):
    """Set the header of the file"""
    magic_number = 1162299681
    magic_number = magic_number.to_bytes(4, byteorder="big")
    major_version = b"\x01"
    minor_version = b"\x00"
    image_count = num_images.to_bytes(2, byteorder="big")

    return magic_number + major_version + minor_version + image_count


def calculated_checksum(og_buffer):
    """Calculate the checksum from original buffer"""
    checksum = 0
    for i in range(len(og_buffer)):
        checksum = (checksum << 1) + og_buffer[
            i
        ] & 0xFFFFFFFF  # Ruh Roh, Integers grow too big

    return checksum.to_bytes(4, byteorder="big")


def assemble_file(header, images):
    """Assemble the file"""
    file = header
    for i in images:
        width, height, data = i
        file += width.to_bytes(4, byteorder="big")
        file += height.to_bytes(4, byteorder="big")
        file += data

    return file


def translate_bytes(data, width, height):
    """Translate the bytes to egi order"""

    new_data = []
    for x in range(width):
        for y in range(height):
            r, g, b = data[x + y * width]
            new_data.extend([r, g, b])

    new_data = bytearray(new_data)

    return new_data


def main():
    """Main function"""
    images = []
    num_images = get_number_of_images()
    for i in range(num_images):

        data, width, height = file_read(user_input())
        data = translate_bytes(data, width, height)
        images.append((width, height, data))

    header = set_header(num_images)

    file = assemble_file(header, images)
    checksum = calculated_checksum(file)
    file += checksum
    name = output_name()
    with open(name + ".egi", "wb") as f:
        f.write(file)


if __name__ == "__main__":
    main()
