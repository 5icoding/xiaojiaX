# encoding:utf-8

import requests
import json

'''
Code Generation
'''
API_KEY = "fb293d668c444bd0b41cc6a2df76241c"  # 从控制台获取
API_SECRET = "34418873d65f4d549d4e918ea4901068"  # 从控制台获取
PROMPT = "from typing import List\n\ndef has_close_elements(numbers: List[float], threshold: float) -> bool:\n    \"\"\" Check if in given list of numbers, are any two numbers closer to each other than\n    given threshold.\n    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)\n    False\n    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)\n    True\n    \"\"\"\n"
NUMBER = 3
LANG = "Python"
request_url = "https://tianqi.aminer.cn/api/v2/multilingual_code_translate "
api = 'multilingual_code_translate'



# 指定请求参数格式为json
headers = {'Content-Type': 'application/json'}
request_url = request_url + api
data = {
    "apikey": API_KEY,
    "apisecret": API_SECRET,
    "prompt":PROMPT,
    "n":NUMBER,
    "lang":LANG
}

def main():
    response = requests.post(request_url, headers=headers, data=json.dumps(data))
    if response:
        print(response.json())
    elif response.status_code != 200:
        print("Error:", response.status_code, response.text)

if __name__ == '__main__':
    main()
