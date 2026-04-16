import os
import sys

from clean_copy_paste import clean_copy_paste
from generator_funcs import generate_pages_recursive


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    clean_copy_paste(basepath + "static", basepath + "docs")
    generate_pages_recursive(basepath + "content", basepath + "template.html", basepath + "docs", basepath)



if __name__ == "__main__":
    main()