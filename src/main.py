from clean_copy_paste import clean_copy_paste
from generator_funcs import generate_pages_recursive


def main():
    clean_copy_paste()
    generate_pages_recursive("content", "template.html", "public")



if __name__ == "__main__":
    main()