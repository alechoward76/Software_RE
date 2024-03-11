[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/MEZ8zmst)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=13717325&assignment_repo_type=AssignmentRepo)
# Project 2: File Reversing
**Overview**: 
 - Students are given a Java application that can open and display a custom image format.
 - Students will need to reverse-engineer the file format.
   - They will need to build tools to work with the format.

**Goals**:
 - Reverse Engineer the `.egi` file format.
   - This includes understanding how the file is structured and how the application reads it.
   - Determine the endianness of the file.
 - Understand how the application reads the file and displays it.
 - Create a schematic of the file format.
   - This can be in the form of a diagram, a table, or a written description.
   - Ensure you include the file offset and the size of each field.
   - If the file offset is dynamic, show the offset from the previous field.
 - Create an application that can read the `.egi` file format and convert it to a more common format (jpg, png, etc.).
   - This can be a command-line application or a GUI application.
 - Create an application that can convert a common format to the `.egi` file format.
    - This can be a command-line application or a GUI application.

**Estimated Time**: 4 hours

**Files**:
 - `image_viewer.jar`: The application that students will be reversing
   - Located in `files\image_viewer.jar`
 - All associated, pre-built images are located in `files\images` directory.
   - These should be downloaded and extracted into a known location.

## Setup
Students must download `image_viewer.jar`, which is the main focus of this project, as well as the associated `images` directory.

The `image_viewer.jar` can be placed anywhere on the student's computer.

The `images` folder must be downloaded; it is suggested that students place it in the same directory as `image_viewer.jar`.

To run the application, students can double-click on the file, or run `java -jar image_viewer.jar` from the command line.

## Required Applications
  - Java 21 or higher
  - Some sort of archive manager (7zip, WinRAR, etc.)

## Suggested Applications
  - Any sort of Java decompiler (JD-GUI, IntelliJ, VSCode, etc.)
  - An IDE (VSCode, etc.)
  - [ImHex](https://imhex.werwolv.net)

## Submission
- Students should submit a writeup of their findings, including:
 - A schematic of the file format
 - A general description of the file format
 - How they reverse-engineered the file format
 - Any tools they built to work with the file format
 - Any challenges they faced
 - Any additional information they found

# Extra Credit
Python was an ideal language candidate for Project 1, but that may not be the case for this project.

Any student who builds their tools using C/C++ will receive extra credit. This is not required, but it is encouraged.
Building tools in C/C++ will help the student in future projects, as well as in the real world.