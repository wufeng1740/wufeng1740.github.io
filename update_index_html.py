import re

def update_max_width_in_media_body(file_path, new_value):
    # 打开并读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    # 正则表达式匹配 @media only screen 中的 body 样式以及 max-width
    media_body_pattern = re.compile(r'@media\s+only\s+screen\s*{\s*body\s*{[^}]*max-width:\s*\d+px;[^}]*}', re.DOTALL)
    # 查找匹配的 @media only screen {... body {... max-width: ... }}
    matches = media_body_pattern.findall(content)
    if matches:
        # 对每个匹配进行处理
        for match in matches:
            # 替换 max-width 的值
            updated_match = re.sub(r'max-width:\s*\d+px;', f'max-width: {new_value}px;', match)
            content = content.replace(match, updated_match)
        # 将修改后的内容写回文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"max-width has been updated to {new_value}px in @media only screen body in {file_path}")
    else:
        print("No matching @media only screen body block found.")

def update_padding_in_body(file_path, new_value):
    # 打开并读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    # 正则表达式匹配 body 样式中的 padding
    body_padding_pattern = re.compile(r'body\s*{\s*[^}]*padding:\s*\d+[^;}]*;', re.DOTALL)
    # 查找匹配的 body {... padding: ... }
    matches = body_padding_pattern.findall(content)
    if matches:
        # 对每个匹配进行处理
        for match in matches:
            # 替换 padding 的值
            updated_match = re.sub(r'padding:\s*\d+[^;]*;', f'padding: {new_value}px;', match)
            content = content.replace(match, updated_match)
        # 将修改后的内容写回文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"padding has been updated to {new_value}px in body style in {file_path}")
    else:
        print("No matching body padding found.")

def update_font_size_in_blockquote(file_path, new_value):
    # 打开并读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 正则表达式匹配 blockquote 样式中的 font-size
    blockquote_font_size_pattern = re.compile(r'blockquote\s*{\s*[^}]*font-size:\s*\d+[^;}]*;', re.DOTALL)

    # 查找匹配的 blockquote {... font-size: ... }
    matches = blockquote_font_size_pattern.findall(content)

    if matches:
        # 对每个匹配进行处理
        for match in matches:
            # 替换 font-size 的值
            updated_match = re.sub(r'font-size:\s*\d+[^;]*;', f'font-size: {new_value};', match)
            content = content.replace(match, updated_match)

        # 将修改后的内容写回文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

        print(f"font-size has been updated to {new_value} in blockquote style in {file_path}")
    else:
        print("No matching blockquote font-size found.")



# 指定html文件路径
file_path = 'index.html'
max_width = 1600
padding = 40
font_size_quote = 1
# 调用函数，修改 max-width 为1536
update_max_width_in_media_body(file_path, max_width)
# 调用函数，修改 padding 为 40
update_padding_in_body(file_path, padding)
# 调用函数，修改 font-size 为 1em
update_font_size_in_blockquote(file_path, f'{font_size_quote}em')