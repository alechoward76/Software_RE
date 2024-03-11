# Alec Howard
# 2/12/2024
# File Reversal

# Imports
from PIL import Image, ImageDraw
import numpy as np


def user_input():
    """Get the file path from the user"""
    user_input = input("Enter a file path: ")
    return str(user_input)


def file_read(file):
    """Read in file bytes and create an array of bytes"""
    try:
        with open(file, "rb") as f:
            data = f.read()
            data = bytearray(data)
        return data
    except:
        print("File not found")
        exit(1)


def read_header(byte_array):
    """Read & parse the first 16 bytes of the file"""
    magic_number = byte_array[:4]
    major_version = byte_array[4:5]
    minor_version = byte_array[5:6]
    image_count = byte_array[6:8]
    # Remove the header from the buffer
    byte_array = byte_array[8:]

    return magic_number, major_version, minor_version, image_count, byte_array


def bytes_to_int(bytes):
    """Converts a byte array to an integer"""
    return int.from_bytes(bytes, byteorder="big")


def read_checksum(byte_array):
    """Read & parse the last 4 bytes of the file"""
    checksum = byte_array[-4:]
    return checksum


def process_image(byte_array):
    """Read & parse the first 8 bytes of the image"""
    width = byte_array[0:4]
    height = byte_array[4:8]
    data = bytes_to_int(width) * bytes_to_int(height) * 3
    data_index = data
    data = byte_array[8 : 8 + data]
    # duplicate data
    # Convert data to a byte array
    # data = bytearray(data)
    # Remove the width and height from the buffer
    byte_array = byte_array[8:]
    width = bytes_to_int(width)
    height = bytes_to_int(height)
    # Remove the pixel data from the buffer
    byte_array = byte_array[data_index:]

    return width, height, data, byte_array


def calculated_checksum(og_buffer):
    """Calculate the checksum from original buffer"""
    checksum = 0
    for i in range(len(og_buffer) - 4):
        checksum = (checksum << 1) + og_buffer[
            i
        ] & 0xFFFFFFFF  # Ruh Roh, Integers grow too big

    return checksum


def create_image(images, u_input):
    """Convert the pixel data to a png image"""
    image_count = 0
    for i in images:
        image_count += 1

        width = i[0]
        height = i[1]
        pix = i[2]
        # convert pix to a byte array
        image = Image.new("RGB", (width, height))

        index = 0
        for x in range(width):
            for y in range(height):
                r = pix[index]
                index += 1
                g = pix[index]
                index += 1
                b = pix[index]
                index += 1
                rgb = r << 16 | g << 8 | b
                image.putpixel((x, y), rgb)
        image.show()
        image.save(u_input + str(image_count) + ".png")
    exit(0)


def main():
    """Main function to run the program"""
    # Get byte buffer & copy it
    u_input = user_input()
    byte_array = file_read(u_input)

    # Get the file name, exclude the file extension
    u_input = u_input.split(".")[0]
    og_buffer = byte_array.copy()
    images = []

    # Check that buffer is not empty
    if byte_array == None:
        print("Buffer is empty")
        exit(1)
    else:
        # Parse the data from the header
        magic_number, major_version, minor_version, image_count, byte_array = (
            read_header(byte_array)
        )
        print("Image Count: ", bytes_to_int(image_count))
        # convert all to ints
        magic_number = bytes_to_int(magic_number)

        # Create an array list of pixel data for each image

        # Check Magic Number
        if magic_number != 1162299681:
            print("Invalid Magic Number")
            exit(1)

        else:
            major_version = bytes_to_int(major_version)
            minor_version = bytes_to_int(minor_version)

            if (major_version <= 1) & (minor_version == 0):
                image_count = bytes_to_int(image_count)
                if image_count == 0:
                    print("Bad Image Count")
                    exit(1)
                else:
                    # Process the images
                    checksum = 0
                    for checksum in range(image_count):
                        width, height, pix, byte_array = process_image(byte_array)
                        img = width, height, pix
                        if img == None:
                            print("Error processing image")
                            exit(1)
                        else:
                            images.append(img)

                    # Get the checksum from the end of buffer
                    checksum = bytes_to_int(read_checksum(byte_array))
                    print("Checksum: ", checksum)
                    # Calculate the checksum from the original buffer
                    calculated = calculated_checksum(og_buffer)
                    print("Calculated: ", calculated)
                    # Check if the checksums match
                    if checksum != calculated:
                        print("Checksums do not match")
                        exit(1)
                    else:
                        print("Checksums match")

            else:
                print("Wrong Version")
                exit(1)

    # Create the images
    create_image(images, u_input)


if __name__ == "__main__":
    main()
