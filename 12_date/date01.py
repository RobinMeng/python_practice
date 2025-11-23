## date
from datetime import datetime, date, timedelta

## 当前时间
print(datetime.now())
## 格式化时间
print(datetime.now().strftime("%Y:%m:%d %H:%M:%S:%s"))

var_date = '2020:01:01 00:00:01'
print(datetime.strptime(var_date, '%Y:%m:%d %H:%M:%S'))
## 年月日
print(datetime.strptime(var_date, '%Y:%m:%d %H:%M:%S').date())

print("*" * 50)
print(date.today())

print("*" * 50)

print(datetime.now() + timedelta(days=100) - datetime.now())

print(type(datetime.now()))
print(type(datetime.now() + timedelta(days=100) - datetime.now()))
diff_time = datetime.now() + timedelta(days=100) - datetime.now()

print(diff_time.days)
print(diff_time.seconds)
print(diff_time.microseconds)
