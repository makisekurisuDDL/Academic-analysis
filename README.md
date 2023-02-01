# Academic-analysis
阿里天池比赛-学术前沿趋势分析  
链接：https://tianchi.aliyun.com/competition/entrance/531866/introduction  
数据集也可在上述链接中查看，太大了传不上来  

数据集格式如下：  
&emsp;&emsp; id：arXiv ID，可用于访问论文  
&emsp;&emsp; submitter：论文提交者  
&emsp;&emsp; authors：论文作者  
&emsp;&emsp; title：论文标题  
&emsp;&emsp; comments：论文页数和图表等其他信息  
&emsp;&emsp; journal-ref：论文发表的期刊的信息  
&emsp;&emsp; doi：数字对象标识符  
&emsp;&emsp; report-no：报告编号  
&emsp;&emsp; categories：论文在 arXiv 系统的所属类别或标签  
&emsp;&emsp; license：文章的许可证  
&emsp;&emsp; abstract：论文摘要  
&emsp;&emsp; versions：论文版本  
&emsp;&emsp; authors_parsed：作者信息（处理后）  

任务1：论文数量统计：统计2019年全年，计算机各个方向论文数量  
任务2：论文作者统计：统计所有论文作者出现频率Top10的姓名  
任务3：论文代码统计：统计所有论文类别下包含源代码论文的数量  
任务4：论文摘要词云：使用论文的摘要制作词云

## Task 1
Paper各类型数量分布  
![img](https://github.com/makisekurisuDDL/img_store/blob/main/Academic-analysis/Task1.JPG)  

各方向Paper统计(部分)  
|  year | 2019 |
|  ---- | ---- |
| category_name |  |
| Artificial Intelligence | 558 |
|  Computation and Language | 2153 |
|  Computational Complexity | 131 |
|  Computational Engineering, Finance, and Science | 108 |
|  Computational Geometry | 199 |
|  Computer Science and Game Theory | 281 |
|  Computer Vision and Pattern Recognition | 5559 |
|  Computers and Society | 346 |
|  Cryptography and Security | 1067 |
|  Data Structures and Algorithms | 711 |
|  Databases | 282 |
|  Digital Libraries | 125 |
|  Discrete Mathematics | 84 |    

## Task 2
对论文最多的分类"cs.CV"中的论文作者姓名出现次数进行统计，取Top10
![img](https://github.com/makisekurisuDDL/img_store/blob/main/Academic-analysis/Task2.jpg)  

## Task 3
对comments和abstract中含github代码链接的论文进行统计，取数量前十的类别制图  
![img](https://github.com/makisekurisuDDL/img_store/blob/main/Academic-analysis/Task3.jpg)

## Task 4
对论文最多的三个类型，使用其下所有论文的摘要制作词云  
![img](https://github.com/makisekurisuDDL/img_store/blob/main/Academic-analysis/cate1.jpg)  
![img](https://github.com/makisekurisuDDL/img_store/blob/main/Academic-analysis/cate2.jpg)  
![img](https://github.com/makisekurisuDDL/img_store/blob/main/Academic-analysis/cate3.jpg)  
