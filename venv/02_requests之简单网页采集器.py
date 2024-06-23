import requests

# UA伪装：浏览器会检测User-Agent，我们需要用到反爬虫机制，即UA伪装
if __name__ == '__main__':
    url = 'https://www.sogou.com/web'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    # 处理url携带的参数:封装到字典中
    kw = input("请输入你想爬取的关键词：")
    param = {
        'query': kw
    }
    # 发起请求
    response = requests.get(url=url, params=param,headers=headers)
    page_text = response.text

    fileName = kw + '.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName, "保存成功！")
    pass
