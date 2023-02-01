import seaborn as sns
from bs4 import BeautifulSoup
import re
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt


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
            d = {col: d[col] for col in columns}
            data.append(d)

    data = pd.DataFrame(data)
    return data


def with_code_only(data):
    data_with_code = data[(data.comments.str.contains('github') == True) |
                          (data.abstract.str.contains('github') == True)]

    data_with_code['text'] = data_with_code['abstract'].fillna('') + data_with_code['comments'].fillna('')

    pattern = '[a-zA-Z]+://github[^\s]*'
    data_with_code['code_flag'] = data_with_code['text'].str.findall(pattern).apply(len)

    data_with_code = data_with_code[data_with_code['code_flag'] == 1]
    data_with_code = data_with_code[['id', 'categories', 'code_flag']]
    data_with_code = data_with_code.groupby(['categories'], as_index=False).agg({'code_flag': 'count'})
    data_with_code = data_with_code.sort_values(by='code_flag', ascending=False)
    data_with_code = data_with_code[:10]

    return data_with_code
