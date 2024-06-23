import requests
import json

if __name__ == '__main__':
    post_url = 'https://fanyi.baidu.com/sug'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    kw = input("请输入想要获取的单词：")
    param = {
        'query': kw
    }
    # 发送请求,获取到json格式数据
    response = requests.post(post_url, param, headers)
    page_json = response.json()
    fileName = kw + '.json'
    fp = open(fileName, 'w', encoding='utf-8')
    # 持久化存储
    json.dump(page_json, fp, ensure_ascii=False)
    fp.close()
    print(kw + "查询完毕！！")
