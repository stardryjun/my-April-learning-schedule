import re, json, jieba
from collections import Counter

# 读取文本内容
with open('01-第1周/coding/王小波作品大全集全15册.txt', 'r', encoding='utf-8') as file:
    text = file.read()

with open('01-第1周/coding/stopwords-master/四川大学机器智能实验室停用词库.txt', 'r', encoding='utf-8') as stopfile:
    stop_words = set(line.strip() for line in stopfile)
with open('01-第1周/coding/stopwords-master/哈工大停用词表.txt', 'r', encoding='utf-8') as stopfile2:
    stop_words.update(line.strip() for line in stopfile2)
with open('01-第1周/coding/stopwords-master/百度停用词表.txt', 'r', encoding='utf-8') as stopfile3:
    stop_words.update(line.strip() for line in stopfile3)
with open('01-第1周/coding/stopwords-master/中文停用词表.txt', 'r', encoding='utf-8') as stopfile4:
    stop_words.update(line.strip() for line in stopfile4)

# 正则提取所有单词（忽略大小写）
words = re.findall(r"[\u4e00-\u9fff]+", text.lower())

# 使用jieba进行分词
words = [word for word in jieba.lcut(" ".join(words)) if word not in stop_words]

# 过滤单个字符的词
words = [word for word in words if len(word) > 1]

# 统计词频
word_count = Counter(words)

# 输出出现频率最高的前1000个单词
for word, count in word_count.most_common(1000):
    print(f"{word}: {count}")

with open('01-第1周/coding/word_frequency.json', 'w', encoding='utf-8') as json_file:
    json.dump(word_count.most_common(1000), json_file, ensure_ascii=False, indent = 4)