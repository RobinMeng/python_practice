# csv 处理
import csv

## 读csv
with open('./data/test.csv', mode='r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print("*" * 50)

with open('./data/test.csv', mode='r') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        print(row)

## 写 csv
with open('./data/test.csv', mode='a') as f:
    writer = csv.writer(f)
    writer.writerow(['1009', '吴十test', '笔记本电脑支架test', '1test', '150.00test', '2023-10-30', '电子产品test', 'TRUE', '华东test'])
    print("写完毕")



