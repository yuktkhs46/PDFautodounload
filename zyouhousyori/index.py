from bs4 import BeautifulSoup
import urllib.request as req
import urllib
import os
import time
from urllib.parse import urljoin

url = 'https://www.jitec.ipa.go.jp/1_04hanni_sukiru/mondai_kaitou_2018h30.html'
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")
result = soup.select("a[href]")
print(result)

# リンクのみ抜き出す
link_list = []
for link in result:
    href = link.get("href")
    link_list.append(href)
print(link_list)

# .pdfで終わるものについてのみ取得
pdf_list = [temp for temp in link_list if temp.endswith('pdf')]
print(pdf_list)

# データベーススペシャリスト試験のPDFのみを取得
dbpdf_list = [temp for temp in pdf_list if '_db_' in temp]
print(dbpdf_list)

# 相対URLから絶対URLに変換
abs_dbpdf_list = []
for relative in dbpdf_list:
    temp_url = urljoin(url, relative)
    abs_dbpdf_list.append(temp_url)
print(abs_dbpdf_list)

# URLからファイル名を取得
filename_list = []
for target in abs_dbpdf_list:
    temp_list = target.split("/")
    filename_list.append(temp_list[len(temp_list)-1])
print(filename_list)

# 保存先のディレクトリを作成
target_dir = "/Applications/MAMP/htdocs/lesson/zyouhousyori/pdf.file"
savepath_list = []
for filename in filename_list:
    savepath_list.append(os.path.join(target_dir, filename))
print(savepath_list)

# ダウンロード実行
for (pdflink, savepath) in zip(abs_dbpdf_list, savepath_list):
    urllib.request.urlretrieve(pdflink, savepath)
    time.sleep(2)
