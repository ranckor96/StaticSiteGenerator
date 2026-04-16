import os

from markdown_to_html import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            header = line.lstrip("# ")
            return header
    raise Exception("Error: no header # in markdown file")
        

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        markdown_content = f.read()
    with open(template_path) as f:
        template_content = f.read()

    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    title = extract_title(markdown_content)

    html_page = template_content.replace("{{ Title }}", title)
    html_page = html_page.replace("{{ Content }}", html_content)
    html_page = html_page.replace('href="/', f'href="{basepath}')
    html_page = html_page.replace('src="/', f'src="{basepath}')
    
    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))

    with open(dest_path, mode="w") as f:
        f.write(html_page)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)
    content = os.listdir(dir_path_content)
    for name in content:
        name_path = os.path.join(dir_path_content, name)
        if os.path.isfile(name_path) and name[-3:] == ".md":
            html_name = name[:-3] + ".html"
            generate_page(name_path, template_path, os.path.join(dest_dir_path, html_name), basepath)
        elif os.path.isdir(name_path):
            generate_pages_recursive(
                os.path.join(dir_path_content, name),
                template_path,
                os.path.join(dest_dir_path, name),
                basepath
            )