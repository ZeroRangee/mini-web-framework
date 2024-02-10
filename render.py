



def render(file_name: str, folder: str = 'templates', *context):
    with open(f"{folder}/{file_name}", "rb") as file:
        html_content = file.read().decode("utf-8")
        
    template_with_variables = html_content.format(*context)
    return b"HTTP/1.1 200 OK\nContent-Type: text/html\n\n"+template_with_variables.encode("utf-8")
        