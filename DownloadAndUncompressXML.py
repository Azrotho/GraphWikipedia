import requests
import bz2

url = "https://mirror.accum.se/mirror/wikimedia.org/dumps/frwiki/20240701/frwiki-20240701-pages-articles.xml.bz2"

r = requests.get(url, allow_redirects=True)
open('frwiki-20240701-pages-articles.xml.bz2', 'wb').write(r.content)

with bz2.open('frwiki-20240701-pages-articles.xml.bz2', 'rb') as compressed_file:
    with open('frwiki-20240701-pages-articles.xml', 'wb') as decompressed_file:
        decompressed_file.write(compressed_file.read())