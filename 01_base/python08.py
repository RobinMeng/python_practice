## 字符串
### 双引号
a = "hello world"
### 三引号
b = """nhdaskhda
dahkdhkaskj
dasldjlas
dasohidaho"""
### str 函数
c = str(1)
print(a)
print(b)
print(c)

## 转译
d = " 他说\" 你好"
print(d)

### 连接字符串

aa = "hello"
bb = "world"

print(aa + " " + bb)

## 禁止转译字符串

text = r"hello world\n\n\n"
print(text)
## 对比
text = "hello world\n\n\n "
print(text)

## 获取字符串的字数
print(len(text))
