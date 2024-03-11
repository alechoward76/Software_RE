# File Reversing

## Author
Alec Howard

## Time Taken
Approximately 8 hours

## Overview
The purpose of this project was to familiarize the student with the concepts of reversing proprietary file formats. This is a vital skill to a good reverse engineer.

## Objectives
- Reverse the file format completely and create a schematic to allow for a quick and total understanding of its design.
- Create an application to read in the egi file format and convert it to a png file.
- Create an application to read in a png file and convert it to the egi format.

## Terminology
- Buffer: A region of a memory used to store data temporarily while it is being moved from one place to another.
- Offset: An adjustable value or position that is added to or subtracted from a starting point.
- Schematic: A detailed representation of a system.

## Key Technologies/Tools Used
- IntelliJ IDEA
- Visual Studio Code
- ImHex
- Google Search Engine
  
## Challenges
Some noteworthy challenges were realizing that python had issues with the checksum function because it didn't cap the value of ints, so I had to replace -1 with 0xFFFFFF. Another challenge was figuring out how to implement the actual writing of image data for both applications, as the original Java application used a unique method.

## Results/Findings
I quickly discovered that the format uses Big Endian. The following is the schematic/description of the egi file format:

- Header
  - 32-bit Integer that serves as the magic number to be checked by the reader.
  - 2 8-bit Integers that represent major then minor version numbers, respectfully, that have values checked to ensure that the correct version of file is being read.
  - 16-bit short that represents the number of images contained within the file.
- Image Data
  - 32-bit Integer that represents the width of the image.
  - 32-bit Integer that represents the height of the image.
  - Pixel data (An array of 24-bit integers that are width*height long) that represents RGB values for each pixel in the image.
- Checksum
  - 32-bit integer at the end of the file representing the checksum. 
- Offsets
  - Static (Address in hex)
    - Magic Number: 0x00000000
    - Major Version: 0x00000004
    - Minor Version: 0x00000005
    - Image Count: 0x00000006
    - Image 1 Width: 0x00000008
    - Image 1 Height: 0x0000000C
    - Image 1 Pixel Data: 0x00000010
  - Dynamic (Address in bytes)
    - Image n Width:
      - (W(n-1) * H(n-1))  
    - Image n Height:
      - (W(n-1) * H(n-1)) + 4 
    - Image n Pixel Data:
      - (W(n-1) * H(n-1)) + 8
    - Checksum:
      - (egi_file_length – 4)

## Reversing
I started reversing the file format by decompiling the java code and tracing the EvilGraphicalImageReader Class. From here I was able to define a structure in ImHex with every element of the header as well as the way the image data and checksum were stored. From there, I began writing a program to interact with the file format, referring back to the java class to implement the functions for checksum and writing image data.
  
## Conclusion
In conclusion, this project was an excellent exercise in both understanding file formats, as well as reversing & programming.
