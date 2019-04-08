import requests

url = 'https://www.naver.com'


if __name__=='__main__':
    res = requests.get(url)

    print(res.cookies.get_dict())


