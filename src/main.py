import os
import sys

from clean_copy_paste import clean_copy_paste
from generator_funcs import generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"


def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    clean_copy_paste(dir_path_static, dir_path_public)
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)



if __name__ == "__main__":
    main()