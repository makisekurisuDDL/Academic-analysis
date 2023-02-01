from paper3 import *

path = 'D:\\pythonProject\\arxiv-metadata-oai-2019.json'

data = readFile(path)

data_with_code = with_code_only(data)

plt.figure(figsize=(12, 10))
plt.bar(data_with_code['categories'], data_with_code['code_flag'])
plt.xticks(rotation=-45)
plt.show()
