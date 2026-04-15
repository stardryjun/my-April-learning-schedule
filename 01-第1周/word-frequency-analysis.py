import re, json
from collections import Counter

# 读取文本内容
with open('01-第1周/王小波作品大全集全15册.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 正则提取所有单词（忽略大小写）
words = re.findall(r"[\u4e00-\u9fff]+", text.lower())

# 统计词频
word_count = Counter(words)

# 输出出现频率最高的前100个单词
for word, count in word_count.most_common(100):
    print(f"{word}: {count}")

with open('01-第1周/word_frequency.json', 'w', encoding='utf-8') as json_file:
    json.dump(word_count.most_common(100), json_file, ensure_ascii=False, indent=4)