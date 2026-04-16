import os
import shutil

def clean_copy_paste(src_dir, dest_dir):
    public_path = dest_dir
    if os.path.exists(public_path) and os.path.isdir(public_path):
        print(f"Clean /{public_path} directory.")
        shutil.rmtree(public_path)
        os.mkdir(public_path)
    else:
        print(f"No /{public_path} directory found. Creating new /{public_path} directory.")
        os.mkdir(public_path)
    print("Starting copy/paste process:")
    static_path = src_dir
    if len(os.listdir(static_path)) != 0:
        copy_paste(static_path, public_path)
    else:
        print(f"/{static_path} directory is empty")
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

