import requests #ensure that the security ext is installed: `pip install requests[security]`

CODEBOOK_URL = "https://www.usfa.fema.gov/downloads/pdf/nfirs/NFIRS_Spec_2005.pdf"

def download_codebook(file_path, url=CODEBOOK_URL):
    response = requests.get(url)
    with open(file_path, "wb") as write_stream:
        write_stream.write(response.content)
