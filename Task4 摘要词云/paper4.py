import json
import pandas as pd
from wordcloud import WordCloud


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


def wordCloud_maker(data):
    str = ''
    for i in range(len(data)):
        str += data.iat[i, 2]
    wd1 = WordCloud(scale=4, background_color='grey', max_words=50, colormap='Pastel1').generate(str)
    imgWC = wd1.to_image()

    return imgWC