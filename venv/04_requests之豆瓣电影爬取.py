import requests
import json

if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        'type': '5',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '20',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    response = requests.get(url=url, params=param, headers=headers)
    list_data = response.json()

    # 持久化存储
    fp = open('./豆瓣动作片.json', 'w', encoding='utf-8')
    json.dump(list_data, fp, ensure_ascii=False)
    print("over!!")
