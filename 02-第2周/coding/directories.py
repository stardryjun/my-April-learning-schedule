import os,sys,datetime

files = os.listdir()
modification_times = []
for file in files:
    if os.path.isfile(file):
        mtime = os.path.getmtime(filename=file)
        modification_times.append((file, datetime.datetime.fromtimestamp(timestamp=mtime)))

# 只保留2天内修改的文件
now = datetime.datetime.now()
filtered = [(f, t) for f, t in modification_times if (now - t).days < 2]
for file, mtime in filtered:
    print(f"{file} was modified on {mtime}")