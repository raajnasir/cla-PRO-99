import os
import shutil
import time

def main():
    deleted_folder_count = 0
    deleted_files_count = 0

    path = "/PATH_TO_DELETE"

    days = 30


    seconds = time.time() - (days * 24 * 60 * 60)

    if os.path.exists(path):

        for root_folder , folders , files in os.walk(path):

            if seconds >= get_files(root_folder):

                remove_folder(root_folder)
                deleted_folder_count += 1

                


