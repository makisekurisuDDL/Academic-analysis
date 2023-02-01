from paper2 import *

path = 'D:\\pythonProject\\arxiv-metadata-oai-2019.json'

data = readFile(path, columns=['id', 'authors', 'categories', 'authors_parsed'])
mostCate, mostCount = findMost(data, 'categories')  # 查询文章最多的分类，结果为cs.CV， 共5559篇

data1 = data[data['categories'] == mostCate]
authors_names = extract_name(data1)     # 返回仅有作者名字，只有一列的Dataframe

# 根据作者频率绘制直方图
plt.figure(figsize=(15, 6))
authors_names[0].value_counts().head(10).plot(kind='barh')

names = authors_names[0].value_counts().index.values[:10]
plt.yticks(range(0, len(names)))
plt.ylabel('Author')
plt.xlabel('Count')
plt.show()

