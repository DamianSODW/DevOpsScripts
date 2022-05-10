#!/usr/bin/env python3
# ************************************************
# Developed by Dmitry S.
#
# Directory cleaner
#
# CLI Arguments 1: LogFileName   2: SizeOfCleanedLog(Kb)
#               3: CountOfAdditionalLogFiles
#
# Date        Version   Info
# 01.07.2021  1.0       Stable version
#
# ************************************************

from shutil import copyfile
from os import path, stat
from sys import argv

# Checking arguments
if len(argv) < 4:
    print("Not enough arguments!")
    exit(1)

file_name = argv[1]
limit_size = int(argv[2])
logfiles_count = int(argv[3])


def log_cleaner():
    """ Copy main log into another file and clean source """

    # Check primary log file existence
    if path.isfile(file_name):
        logfile_size = stat(file_name).st_size  # In Bytes
        logfile_size = logfile_size / 1024  # Convert to Kilobytes

        if logfile_size >= limit_size:

            if logfiles_count > 0:
                for current_file_number in range(logfiles_count, 1, -1):
                    source = f"{file_name}_{str(current_file_number - 1)}"
                    destination = f"{file_name}_{str(current_file_number)}"

                    if path.isfile(source):
                        copyfile(source, destination)
                        print(f"Copied: {source} to {destination}")

                copyfile(file_name, f"{file_name}_1")
                print(f"Copied: {file_name} to {file_name}_1")

            # Clean main log file
            main_logfile = open(file_name, "w")
            main_logfile.close()


# Checking run source (CLI or another program)
if __name__ == '__main__':
    log_cleaner()
