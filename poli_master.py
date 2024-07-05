import requests
from pypdf import PdfReader
import os
from lxml.html import fromstring

def download_pdf(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)

origin = "https://upb.ro/programe-de-masterat-oferite-de-universitatea-politehnica-din-bucuresti/#FacultateaDeEnergetica"
wanted_str = "python"
r = requests.get(origin)
data = fromstring(r.text)
urls = data.xpath("//*[contains(@class, 'aio-icon-box-link')]//@href")
for url in urls:
    filename ="files/" +  url.split("/")[-1]

    download_pdf(url, filename)

    reader = PdfReader(filename)
    text = ""
    has_string = False

    for page in reader.pages:
        has_string = wanted_str in page.extract_text().lower()
        if has_string:
            break
    if has_string:
        print(f"Found at {url}")

    os.remove(filename)