[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Vgt0xfsF)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=13941640&assignment_repo_type=AssignmentRepo)
# Project 3: Basic C Game
**Overview**: 
 - Students are given a game written in C which they will need to reverse-engineer.
 - Students must determine how the game works on a low-level and how to win the game.
   - Winning the game without using any reverse-engineering tools is possible, but it is not the intended method, and it will take a long time.

**Goals**:
- Reverse Engineer the `number_guessing_game.exe` file.
  - This file is built using the MSVC compiler in 32-bit (x86) mode.
- Use IDA to disassemble the file and understand how it works.
  - Name all methods used within the `main` method.
    - Note that the `main` method is not the `start` address.
  - Name and define all structures/classes if applicable.
- Write  a script or program to win the game.
  - This will require an understanding of the random number generation used in the game.
- Identify and decrypt the encrypted win message.
- Identify and use any hidden features in the game.

**Estimated Time**: 4 hours

**Files**:
 - `number_guessing_game.exe`: The application that students will be reversing

## Setup
Students must download `number_guessing_game.exe`, which is the main focus of this project.
This file can only be run on a Windows machine. If required, students can request a Windows VM from the instructor or use a cloud-based solution.

The `number_guessing_game.exe` can be placed anywhere on the student's computer.

To run the application, students can double-click on the file, or run `./number_guessing_game.exe` from the command line.

Input is received via `stdin` and output is sent to `stdout`.

## Required Applications
  - IDA Pro
  - Windows 10 or higher

## Suggested Applications
- Python or another scripting language
- An IDE (VSCode, etc.)

## Submission
- Students should submit a writeup of their findings, including:
  - A list of all methods used within the `main` method.
    - Including the RVA, the method name (to your best guess), and a brief description of what the method does.
  - Any optional arguments or flags that can be used with the application.
  - An explanation of how the random number generation works.
    - Including the initial seeding method and the method used to generate the random number.
  - An explanation of the encryption method used for the win message.
  - How to win the game.
    - Any hidden features found within the game.
  - How a script or program can be used to win the game.
  - Any challenges faced during the reverse-engineering process.