from PyPDF2 import PdfReader
import docx, csv, json
from bs4 import BeautifulSoup
import requests


def extract_text_from_url(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text()
def extract_text_from_file(file):
    if file.name.endswith(".pdf"):
        reader = PdfReader(file)
        return "\n".join([page.extract_text() for page in reader.pages])
    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        return "\n".join([p.text for p in doc.paragraphs])
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    elif file.name.endswith(".csv"):
        lines = file.read().decode("utf-8").splitlines()
        reader = csv.reader(lines)
        return "\n".join([" | ".join(row) for row in reader])
    elif file.name.endswith(".json"):
        data = json.load(file)
        return json.dumps(data, indent=2)
    elif file.name.endswith(".html") or file.name.endswith(".xml"):
        soup = BeautifulSoup(file, "html.parser")
        return soup.get_text()
    return ""