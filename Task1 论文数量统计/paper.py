import re
import seaborn as sns
import json
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup


def readFile(path, columns=None, count=None):

    if columns is None:
        columns = ['id', 'submitter', 'authors', 'title', 'comments', 'journal-ref', 'doi',
                   'report-no', 'categories', 'license', 'abstract', 'versions',
                   'update_date', 'authors_parsed']

    data = []
    with open(path, 'r') as f:
        for idx, line in enumerate(f):
            if idx == count:
                break
            d = json.loads(line)
            d = {col : d[col] for col in columns}
            data.append(d)

    data = pd.DataFrame(data)
    return data


def get_text(url):
    web_url = requests.get(url).text
    soup = BeautifulSoup(web_url)
    root = soup.find('div', {'id': 'category_taxonomy_list'})
    tags = root.find_all(['h2', 'h3', 'h4', 'p'], recursive=True)

    level_1_name = ""
    level_2_name = ""
    level_2_code = ""
    level_1_names = []
    level_2_codes = []
    level_2_names = []
    level_3_codes = []
    level_3_names = []
    level_3_notes = []

    for t in tags:
        if t.name == "h2":
            level_1_name = t.text
            level_2_code = t.text
            level_2_name = t.text
        elif t.name == "h3":
            raw = t.text
            level_2_code = re.sub(r"(.*)\((.*)\)", r"\2", raw)  # 正则表达式：模式字符串：(.*)\((.*)\)；被替换字符串"\2"；被处理字符串：raw
            level_2_name = re.sub(r"(.*)\((.*)\)", r"\1", raw)
        elif t.name == "h4":
            raw = t.text
            level_3_code = re.sub(r"(.*) \((.*)\)", r"\1", raw)
            level_3_name = re.sub(r"(.*) \((.*)\)", r"\2", raw)
        elif t.name == "p":
            notes = t.text
            level_1_names.append(level_1_name)
            level_2_names.append(level_2_name)
            level_2_codes.append(level_2_code)
            level_3_names.append(level_3_name)
            level_3_codes.append(level_3_code)
            level_3_notes.append(notes)

    df_taxonomy = pd.DataFrame({
        'group_name': level_1_names,
        'archive_name': level_2_names,
        'archive_id': level_2_codes,
        'category_name': level_3_names,
        'categories': level_3_codes,
        'category_description': level_3_notes

    })
    df_taxonomy.groupby(["group_name", "archive_name"])

    return df_taxonomy
