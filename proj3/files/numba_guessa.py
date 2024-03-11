# Alec Howard
# 2/26/2024
# Number Guessing Game

import subprocess
import time
import argparse


# Find seconds since epoch
def get_seconds():
    """Returns the current time since epoch in seconds."""
    return int(time.time()) & 0x3F


def generate_random_number(my_seed, my_time):
    """Returns a random number and updated time value."""
    my_time = (0x41C64E6D * my_time + 0x3039) & 0x7FFFFFFF
    r_num = 1 + my_time % 50
    return r_num, my_time


def main():
    parser = argparse.ArgumentParser(description="A tool for Numba Guessing 8^)")
    parser.add_argument(
        "path", type=str, help="Path to the number_guessing_game.exe file"
    )

    parser.add_argument("--debug", action="store_true", help="Enable debug mode")

    try:
        args = parser.parse_args()
        exe_path = args.path

        if args.debug:
            process = subprocess.Popen([exe_path, "--debug"], stdin=subprocess.PIPE)
        else:
            process = subprocess.Popen([exe_path], stdin=subprocess.PIPE)

        my_time = get_seconds()

        for i in range(1000):

            my_seed = my_time
            r_num, my_time = generate_random_number(my_seed, my_time)

            process.stdin.write(f"{r_num}\n".encode())
            process.stdin.flush()
            process.stdin.write(b"y\n")
            process.stdin.flush()

        process.stdin.write(b"n\n")
        process.stdin.close()

    except Exception as e:
        print(f"Invalid Path: {e}")
        exit(1)


if __name__ == "__main__":
    main()
