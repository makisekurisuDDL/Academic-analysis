from paper4 import *

path = 'D:\\pythonProject\\arxiv-metadata-oai-2019.json'

data = readFile(path, columns=['id', 'categories', 'abstract'])

# 取文章数量前三的种类
data_sorted = data.groupby('categories', as_index=False).agg({'id': 'count'})
data_sorted = data_sorted.sort_values(by='id', ascending=False)
data_sorted = data_sorted[:3]
data = data[data.categories.isin(data_sorted['categories'].tolist())]

data1 = data[data['categories'] == data_sorted.iat[0, 0]]
data2 = data[data['categories'] == data_sorted.iat[1, 0]]
data3 = data[data['categories'] == data_sorted.iat[2, 0]]

imgWC1 = wordCloud_maker(data1)
imgWC2 = wordCloud_maker(data2)
imgWC3 = wordCloud_maker(data3)

imgWC1.save('cate1.jpg')
imgWC2.save('cate2.jpg')
imgWC3.save('cate3.jpg')
