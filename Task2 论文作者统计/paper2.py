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


def findMost(data, column):
    f = data.groupby(column, as_index=False).agg({'id': 'count'})
    f = f.sort_values(by='id', ascending=False)

    return f.iloc[0, 0], f.iloc[0, 1]


def extract_name(data):
    all_authors = sum(data['authors_parsed'], [])
    authors_names = [' '.join(x) for x in all_authors]
    authors_names = pd.DataFrame(authors_names)

    return authors_names
