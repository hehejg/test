import requests, os

payload = {}
headers = {
    'Connection': 'keep-alive',
    'Accept': 'text/html, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://ok.3r5j.cn/admin/list.php?page=2',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': 'Cookie: mysid=d802603451b81d6be885a3bbe24532c2; admin_token=319a6JrmQVIMffCLfpdAD591dy4fJfHyVKQcinCSRaC1X0KpbuKIzUwoo1xuP6jUmKfIm1MHZ9Z8WtIseGWcwbAUlL7w9xTh9g; PHPSESSID=l80kp3aqmggv9ug9riuefqt6v6; mysid=5d50e7ef1f09a408e54da12133f51cb9; sec_defend=aea2604dbacd70acaacf9ba6e870a218aab66e22939e4e5cc0e1e558a999279a; counter=2'
}


def download(max_page, save_path, url):
    for i in range(1, max_page + 2):
        response = requests.get(url % i, headers=headers, data=payload)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        with open(os.path.join(save_path, "%d.html" % i), 'wb') as f:
            f.write(response.content)


if __name__ == '__main__':
    a = int(input('最大页数'))
    b = input('保存路径')
    c = input('下载链接 http://ok.3r5j.cn/admin/fakalist.php?page=%d    page 后面改成%d')
    download(a, b, c)
