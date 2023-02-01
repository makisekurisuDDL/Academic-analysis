from paper import *

path = "arxiv-metadata-oai-2019.json"

data = readFile(path, columns=['id', 'categories', 'update_date'])  # 读取数据
data['year'] = pd.to_datetime(data['update_date']).dt.year
data = data[data['year'] == 2019]   # 仅查看2019年的文章
del data['update_date']

url = "https://arxiv.org/category_taxonomy"
df_taxonomy = get_text(url)     # 爬虫爬取网页文本
_df = data.merge(df_taxonomy, on="categories", how="left").drop_duplicates(["id", "group_name"]).groupby(
    "group_name").agg({"id": "count"}).sort_values(by="id", ascending=False).reset_index()

fig = plt.figure(figsize=(15, 12))
explode = (0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5)
plt.pie(_df['id'], labels=_df['group_name'], autopct='%1.2f%%', explode=explode)
plt.show()

group_name = 'Computer Science'
cats = data.merge(df_taxonomy, on="categories").query("group_name == @group_name")
cats = cats.groupby(["year", "category_name"]).count().reset_index().pivot(index="category_name", columns="year",
                                                                           values="id")
print(cats)
