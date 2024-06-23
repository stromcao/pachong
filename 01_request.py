import requests;

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # 1、指定url
    url = 'https://www.sogou.com/'

    # 2、发起请求
    response = requests.get(url)

    # 3、获取响应数据
    page_text = response.text
    print(page_text)
    # 4、持久化存储
    with open('./sogou.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print("爬取结束")

    pass
