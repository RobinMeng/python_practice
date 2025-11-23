## 在字符串中嵌入值

name = 'test'
date = 10

val = f"我是{name},现在是时间{date}点整"
print(val)

##
val = "我是{},现在是时间{}点整"

print(val.format(name, date))

##
val = "我是{name},现在是时间{date}点整"
print(val.format(name=name, date=date))
print(val.format(**{"name": name, "date": date}))
