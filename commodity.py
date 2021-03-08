import requests, re,os


payload = {}
headers = {
    'Connection': 'keep-alive',
    'Accept': 'text/html, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://ok.3r5j.cn/admin/shoplist.php?page=14',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': 'Cookie: mysid=b3490f4bc105aed98da3c89dcb45709b; admin_token=a629HDXunD0v%2Fuu%2BcZjUJaVifhyKmowNElw5L3Wz4BMTEqmIO6UZrRwCeAizv59JAHWuMc%2Bec3pcbbGD%2FXYPDhavPMjii0W4qRDRsTg; PHPSESSID=ltst606247ntjqcqko3gkmv62c; mysid=f9ee438f066ed65fcff9f40e5cf27d97'
}


for i in range(1, 16):
    response = requests.get(f"http://ok.3r5j.cn/admin/shoplist-table.php?num=100&page={i}&_=1611580750173", headers=headers, data=payload)
    with open(os.path.join(r"C:\Users\he\Desktop\固定数据\商品列表", f"{i}.html"), 'wb') as f:
        f.write(response.content)
    for j in re.findall('id="list1" value="(\d+)"',response.text,flags=re.S):
        response = requests.get(f"http://ok.3r5j.cn/admin/shopedit.php?my=edit&tid={j}",headers=headers, data=payload)
        with open(os.path.join(r"C:\Users\he\Desktop\固定数据\商品列表", f"{i}_{j}.html"), 'wb') as f:
            f.write(response.content)

# print(response.text)
