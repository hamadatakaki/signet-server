import requests

def post_signet():
    payload = {
        "url": "https://www.tokuyama.ac.jp/",
        "icon": "https://www.tokuyama.ac.jp/icon.ico",
        "title": "徳山工業高等専門学校",
        "position": 1200
    }
    r = requests.post("http://localhost:8000/api/signet", json=payload)
    print(r.text)

if __name__=='__main__':
    post_signet()
