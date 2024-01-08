import requests
import re
from os.path import join, realpath, dirname, exists

file_path = join(dirname(realpath(__file__)), "Othello.txt")

if not exists(file_path):
    resp = requests.get("https://www.gutenberg.org/cache/epub/2267/pg2267.txt")
    if resp.ok:
        with open(file_path, "x", encoding=resp.apparent_encoding) as file:
            file.write(resp.text)

with open(file_path, "r", encoding="utf-8") as file:
    book = file.read()
    sentences1 = re.findall(r'((?<=[.!?])\s+)', book)  # znaménko a potom mezera
    print(len(sentences1))
    sentences2 = re.findall(r'(?<!\b[A-Z][a-z])\.((?<=[.!?])\s+)', book)
  # prvni zavorka odebírá tituly jako mr. etc druha
  # zavorka je mezera po znaménku
    print(len(sentences2))