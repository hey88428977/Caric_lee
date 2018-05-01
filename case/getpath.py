import os

# 当前脚本的路径

print(__file__)  # 左斜杠

# 右斜杠
real = os.path.realpath(__file__) # 真实路径
print(real)

# 当前脚本的文件夹路径
dirname = os.path.dirname(real)
print(dirname)
gc = os.path.dirname(dirname)
print(gc)

# 进common
com = os.path.join(gc, "common")
print(com)
exl = os.path.join(com, "testdata.xlsx")
print(exl)


