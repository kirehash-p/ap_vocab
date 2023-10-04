import requests
from bs4 import BeautifulSoup
import time
import csv

url_tmp = "https://www.ap-siken.com/s/keyword/"
hiragana = "xaxixuxexokakikukekosasisusesotatitutetonaninunenohahihuhehomamimumemoyayuyorarirurerowa"
alphabet = "abcdefghijklmnopqrstuvwxyz"
output = "vocabs.csv"
words = []
query = [hiragana[x:x+2] for x in range(0, len(hiragana), 2)] + ["_"+alphabet[x] for x in range(0, len(alphabet), 1)]

for param in query:
    time.sleep(1)
    url = f"{url_tmp}{param}.html"
    print(f"getting vocab list from {url}...")
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    keywords = soup.find_all('div', class_="keywordBox")
    try:
        for i in keywords:
            words.append([i.find("p", class_="big").text,i.find("span", class_="cite").text,i.find("div").get_text()])
    except:
        print("Error!")

print(f"Done!\nTotal words:{len(words)}\nWriting vocab data to {output}...")

with open(output, mode="w", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in words:
        csv_writer.writerow(row)

print("All process done!!")