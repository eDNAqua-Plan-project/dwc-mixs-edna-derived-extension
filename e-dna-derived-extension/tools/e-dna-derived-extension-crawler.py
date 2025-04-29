import requests
import xml.etree.ElementTree as ET
import pandas as pd
from bs4 import BeautifulSoup
import re
import time

url = "https://rs.gbif.org/extension/gbif/1.0/dna_derived_data_2024-07-11.xml"
response = requests.get(url)
response.raise_for_status()


ns = {'ext': 'http://rs.gbif.org/extension/'}  # Default namespace
root = ET.fromstring(response.content)

# extract name and qualName from all <property> elements
data = []
for prop in root.findall("ext:property", namespaces=ns):
    name = prop.attrib.get("name")
    qual_name = prop.attrib.get("qualName")
    # if name:
    #     name = f"dwc:{name}"
    term_label = None
    if qual_name:
        try:
            html_resp = requests.get(qual_name, timeout=10)
            html_resp.raise_for_status()
            soup = BeautifulSoup(html_resp.text, "html.parser")

            title_text = soup.title.string.strip() if soup.title else None

            # Extract text after colon and before parenthesis
            if title_text and ':' in title_text:
                match = re.search(r":\s*(.*?)\s*\(", title_text)
                if match:
                    term_label = match.group(1).strip()

            time.sleep(0.5)
        except Exception as e:
            full_title = f"Error: {e}"

    data.append({
        'name': name,
        'qualName': qual_name,
        'term_label': term_label,
    })

df = pd.DataFrame(data)

df.to_csv("gbif_dna_derived_data_fields.csv", index=False)
