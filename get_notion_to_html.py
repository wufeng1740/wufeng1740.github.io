import requests
from bs4 import BeautifulSoup

# 输入你的 Notion 页面 URL
notion_url = "https://accidental-radiator-9d4.notion.site/Feng-Wu-s-Resume-121620a8da3a80d3b6d8f09ddbd7aef9?pvs=4"

# 添加请求头，模拟浏览器请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# 发送 GET 请求到 Notion 页面
response = requests.get(notion_url, headers=headers)

# 检查是否请求成功
if response.status_code == 200:
    # 解析 HTML 内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 保存为 HTML 文件
    with open("notion_page.html", "w", encoding='utf-8') as file:
        file.write(soup.prettify())
    
    print("Notion 页面已经成功保存为 notion_page.html")
else:
    print(f"请求失败，状态码: {response.status_code}")