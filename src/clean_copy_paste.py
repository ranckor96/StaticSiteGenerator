import os
import shutil

def clean_copy_paste():
    public_path = os.path.abspath("public")
    if os.path.exists(public_path) and os.path.isdir(public_path):
        print("Clean /public directory.")
        shutil.rmtree(public_path)
        os.mkdir(public_path)
    else:
        print("No /public directory found. Creating new /public directory.")
        os.mkdir(public_path)
    print("Starting copy/paste process:")
    static_path = os.path.abspath("static")
    if len(os.listdir(static_path)) != 0:
        copy_paste(static_path, public_path)
    else:
        print("/static directory is empty")
    print("Copy/paste process is complited")


def copy_paste(current_path, path_to_copy):
    dir_content = os.listdir(current_path)
    for name in dir_content:
        abs_path_name = os.path.join(current_path, name)
        abs_copy_name = os.path.join(path_to_copy, name)
        if os.path.isfile(abs_path_name):
            shutil.copy(abs_path_name, abs_copy_name)
            print(f"Found and copied file: {abs_path_name}")
        elif os.path.isdir(abs_path_name):
            os.mkdir(abs_copy_name)
            print(f"Found and copied directory: {abs_path_name}")
            copy_paste(abs_path_name, abs_copy_name)

