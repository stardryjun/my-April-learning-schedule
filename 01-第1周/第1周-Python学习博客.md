# 第1周 Python 新手教学博客（04/15 ~ 04/21）

> 这是一篇面向零基础同学的教程。你不需要“背代码”，重点是理解：**为什么这么写**、**每一行在做什么**、**我自己怎么改**。

---

## 先说学习目标（这一周学完你应该会什么）

你要拿下这 4 件事：

1. 看得懂并写出基础语法（变量、判断、循环、函数）。
2. 会用四种核心容器（list/tuple/dict/set）。
3. 会处理字符串、会读写文件、会处理报错（异常）。
4. 能做两个小项目：成绩管理器 + 词频统计器。

---

## 1. Python 基础语法：先把“会写”变成“看得懂”

### 1.1 第一段完整示例

```python
name = "Harry"      # 字符串 str
age = 20            # 整数 int
height = 1.78       # 小数 float
is_student = True   # 布尔 bool

print(name, age, height, is_student)
print(type(name), type(age), type(height), type(is_student))
```

### 1.2 逐行讲解

- `name = "Harry"`：把右边的值绑定给左边变量名。Python 变量不需要先声明类型。
- `print(...)`：把内容输出到终端，便于你观察程序运行结果。
- `type(name)`：查看变量类型，初学时非常有用。

### 1.3 新手易错点

- 变量名不能以数字开头（`1name` 错）。
- 字符串要加引号（`"Harry"`），不加就会被当成变量名。

---

## 2. 控制流：让程序会“判断”和“重复”

### 2.1 if / elif / else

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

print("成绩等级:", grade)
```

### 2.2 为什么这里必须缩进？

Python 用缩进表示代码块归属。  
`if` 下面缩进的几行，表示“条件成立时执行”。  
所以缩进不是“格式美观”，是语法本身。

### 2.3 for 循环（遍历）

```python
for i in range(1, 6):
    print("第", i, "次练习")
```

- `range(1, 6)` 生成 1 到 5（不包含 6）。
- 读作：从 1 到 5，依次赋值给 `i`。

---

## 3. 函数与作用域：把重复逻辑打包

### 3.1 函数基础

```python
def greet(user, prefix="你好"):
    message = f"{prefix}，{user}！"
    return message

print(greet("小明"))
print(greet("小红", "Hi"))
```

### 3.2 你需要理解的点

- `def`：定义函数。
- `user`：形参（调用时传入）。
- `prefix="你好"`：默认参数，不传就用默认值。
- `return`：把结果返回给调用者。

### 3.3 作用域（scope）一句话理解

函数内部创建的变量（比如 `message`）默认只在函数内部可见。  
这可以避免变量名互相污染。

---

## 4. 四大数据结构：list / tuple / dict / set

### 4.1 一次看懂区别

```python
# list：有序、可修改
numbers = [3, 1, 4]
numbers.append(1)
numbers.sort()

# tuple：有序、不可修改
point = (10, 20)

# dict：键值对
student = {"name": "Alice", "score": 92}
student["class"] = "CS1"

# set：无序、自动去重
tags = {"python", "algo", "python"}

print(numbers)
print(point)
print(student)
print(tags)
```

### 4.2 新手该怎么选

- 要存一串会变的数据：`list`
- 一组固定数据（如坐标）：`tuple`
- 通过“名字找值”：`dict`
- 只关心“有没有重复”：`set`

---

## 5. 推导式 + 切片：写更 Pythonic 的代码

### 5.1 列表推导式

```python
data = [1, 2, 3, 4, 5, 6]
even_square = [x * x for x in data if x % 2 == 0]
print(even_square)  # [4, 16, 36]
```

读法：从 `data` 里取每个 `x`，如果 `x` 是偶数，就放入 `x*x`。

### 5.2 切片

```python
print(data[:3])    # 前3个
print(data[-3:])   # 后3个
print(data[::2])   # 每隔1个取1个
```

切片格式是 `[start:end:step]`，省略就用默认值。

---

## 6. 字符串处理：几乎每个项目都会用到

```python
text = "  hello,Python  "

print(text.strip())                  # 去掉两端空格
print(text.lower())                  # 变小写
print(text.replace("Python", "CS"))  # 替换内容

name = "Bob"
score = 96.5
print(f"{name} 的分数是 {score:.1f}")
```

### f-string 是什么？

`f"..."` 里面可以直接写变量，非常直观。  
`{score:.1f}` 表示保留 1 位小数。

---

## 7. 常用内置函数：map / filter / zip / enumerate / sorted

```python
nums = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, nums))          # 映射：每个元素平方
evens = list(filter(lambda x: x % 2 == 0, nums))    # 过滤：保留偶数
pairs = list(zip(["a", "b", "c"], [10, 20, 30]))    # 打包

for idx, lang in enumerate(["python", "java"], start=1):
    print(idx, lang)  # 带下标遍历

students = [("Alice", 91), ("Bob", 87), ("Cindy", 95)]
rank = sorted(students, key=lambda x: x[1], reverse=True)  # 按分数排序
print(squares, evens, pairs, rank)
```

### 建议

如果你觉得 `lambda` 暂时不熟，可以先写普通函数，效果一样。

---

## 8. 文件读写：你的数据才能“保存下来”

### 8.1 文本文件

```python
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("Python 学习记录\n")
    f.write("第1周：基础语法\n")

with open("demo.txt", "r", encoding="utf-8") as f:
    content = f.read()

print(content)
```

### 8.2 为什么必须写 `with open(...)`？

因为它会自动关闭文件，减少资源泄漏和忘记关闭文件的问题。

---

## 9. 异常处理：程序报错时“优雅处理”

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "错误：除数不能为0"

print(safe_divide(10, 2))
print(safe_divide(10, 0))
```

### 结构理解

- `try`：先尝试执行
- `except`：如果出现指定错误，就进入这里

异常处理不是掩盖错误，而是给出可理解提示，避免程序直接崩溃。

---

## 10. 模块与包：让代码从“脚本”变“工程”

当文件变多时，把功能拆分：

```text
week1_project/
├── app.py
├── utils/
│   ├── __init__.py
│   └── file_ops.py
└── data/
    └── students.json
```

`app.py` 调用 `utils/file_ops.py` 的函数，结构清晰，后续维护更轻松。

---

## 11. 综合实操 1：成绩管理器（入门版）

下面这个版本包含：新增学生、显示成绩、按分数排序。

```python
students = []

def add_student(name, score):
    students.append({"name": name, "score": score})

def show_students():
    if not students:
        print("暂无数据")
        return
    for s in students:
        print(f"{s['name']} -> {s['score']}")

def show_rank():
    ranking = sorted(students, key=lambda x: x["score"], reverse=True)
    for i, s in enumerate(ranking, start=1):
        print(f"第{i}名: {s['name']} ({s['score']})")

add_student("Tom", 88)
add_student("Lucy", 95)
add_student("Jack", 90)
show_students()
show_rank()
```

### 你可以继续扩展

- 增加“删除学生”
- 增加“平均分/最高分”
- 增加“保存到 JSON 文件”

---

## 12. 综合实操 2：文本词频统计器（入门版）

```python
import re
from collections import Counter

def word_count(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read().lower()

    words = re.findall(r"[a-z]+", text)  # 提取英文单词
    counter = Counter(words)

    for word, cnt in counter.most_common(10):
        print(f"{word}: {cnt}")

word_count("demo.txt")
```

### 这段代码练到了什么

- 文件读取
- 正则提取
- 词频统计
- 排序输出

---

## 13. 本周打卡清单（照着做就不会乱）

- 完成至少 20 道 Python 简单题（每天 3~5 道）
- 完成 2 个小项目（成绩管理器、词频统计器）
- 每天把“今天新学会的 3 个点 + 1 个易错点”写入 `学习笔记.md`

---

## 14. 给新手的最后建议

你现在最重要的不是“追求高级”，而是“稳扎稳打”：

- 看懂一段代码后，**必须自己敲一遍**
- 把变量名改成自己的，再运行一次
- 每学一个知识点，都做一个 20~50 行的小练习

只要坚持一周，你对 Python 的陌生感会明显下降。
