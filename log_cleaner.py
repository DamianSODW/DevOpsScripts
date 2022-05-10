#!/usr/bin/env python3
# ************************************************
# Developed by Dmitry S.
#
# Log cleaner
#
# CLI Arguments 1: LogFileName   2: SizeOfCleanedLog(Kb)
#               3: CountOfAdditionalLogFiles
#
# Date        Version   Info
# 01.07.2021  1.0       Stable version
#
# ************************************************

import shutil
import os
import sys

# Checking arguments
if len(sys.argv) < 4:
    print("Not enough arguments! Use --help or -h for additional information")
    exit(1)

# Checking run source (CLI or another program)
if __name__ == '__main__':
    print('resolve')
    exit(2)

file_name = sys.argv[1]
limit_size = int(sys.argv[2])
logfiles_count = int(sys.argv[3])

# Check primary log file existence
if os.path.isfile(file_name):
    logfile_size = os.stat(file_name).st_size  # In Bytes
    logfile_size = logfile_size / 1024         # Convert to Kilobytes

    if logfile_size >= limit_size:

        if logfiles_count > 0:
            for current_file_number in range(logfiles_count, 1, -1):
                source = f"{file_name}_{str(current_file_number-1)}"
                destination = f"{file_name}_{str(current_file_number)}"

                if os.path.isfile(source) == True:
                    shutil.copyfile(source, destination)
                    print(f"Copied: {source} to {destination}")

            shutil.copyfile(file_name, f"{file_name}_1")
            print(f"Copied: {file_name} to {file_name}_1")


