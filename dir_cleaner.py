#!/usr/bin/env python3
# ************************************************
# Developed by Dmitry S.
#
# Directory cleaner
# Search and clean all empty folders and files older than parameter
#
# Date        Version   Info
# 16.08.2021  1.0       Stable version
#
# ************************************************
import os
from os import walk, remove, rmdir, path
from time import time, asctime

days_to_delete = 2  # All files older than value will be deleted
sekonds_to_delete = 60 * 60 * 24 * days_to_delete  # Convert days to seconds
folders_to_search = ["/home/kadzehana/python/DevOpsScripts/resources"]  # List of directories where program will search

empty_space = 0
deleted_file_count = 0
deleted_directories_count = 0
time_now = time()


def clean_old_files(folder, empty_space, deleted_file_count):
    """ Searching all files witch older than parameter value and delete them """
    for path_to_folder, directory_name, files in walk(folder):
        for file in files:
            file_name = path.join(path_to_folder, file)
            file_time = path.getmtime(file_name)
            if file_time < sekonds_to_delete:
                file_size = path.getsize(file_name)
                empty_space += file_size
                deleted_file_count += 1
                print(f"Deleting file: {str(file_name)}")
                remove(file_name)


def clean_empty_directories(folder, deleted_directories_count):
    """ Recursively search for empty folders and delete them """
    check_parent_folder_to_delete = False
    for path_to_folder, directory_name, files in walk(folder):
        if (not directory_name) and (not files):
            deleted_directories_count += 1
            check_parent_folder_to_delete = True  # Check the parent directory to see if it needs to be deleted.
            print(f"Deleting folder: {str(path_to_folder)}")
            rmdir(path_to_folder)
    if check_parent_folder_to_delete:
        clean_empty_directories(folder, deleted_directories_count)


# Checking run source (CLI or another program)
if __name__ == '__main__':
    start_time = asctime()
    for folder in folders_to_search:
        clean_old_files(folder, empty_space, deleted_file_count)
        clean_empty_directories(folder, deleted_directories_count)

    finish_time = asctime()

    print("------------------------------------------------------")
    print(f"Start time: {str(start_time)}")
    print(f"Clean space: {str(int(empty_space / 1024 / 1024))}")
    print(f"Deleted files: {str(deleted_file_count)}")
    print(f"Deleted empty folders: {str(deleted_directories_count)}")
    print("------------------------------------------------------")
