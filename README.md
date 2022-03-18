# getNowcoder-interviewList
将牛客上的面试题集锦保存为markdown文件

- 测试：前端校招面试题合集
https://www.nowcoder.com/ta/review-frontend?query=&asc=true&order=&tagQuery=&page=1
即链接https://www.nowcoder.com/ta/review-frontend/review?page=1

脚本语言：python3
request+xpath解析
用到的库
- request
- lxml
- re

可以更改以下部分来爬取其他地方的题集，和修改文件路径
```python3
url='https://www.nowcoder.com/ta/review-frontend/review?page='
fname = 'nowcoder-前端面试题-HTML部分.md'
page_range = range(1,43) # 1-42页
```
保存的文件格式主要如下：
> ## 题目1
> - 答案
> - 答案
> discussion链接
> ## 题目2
> - 答案
> - 答案
> discussion链接

因为是前端的面试题，有大量html标签，进行了转义处理
其余部分的格式建议手动调整
