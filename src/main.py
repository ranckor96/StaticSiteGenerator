import sys

from clean_copy_paste import clean_copy_paste
from generator_funcs import generate_pages_recursive


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    clean_copy_paste("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)



if __name__ == "__main__":
    main()