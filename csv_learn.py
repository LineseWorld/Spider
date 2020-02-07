import csv
import pandas
# -i https://pypi.tuna.tsinghua.edu.cn/simple
with open('csv_file\\csv_test.csv', 'w',encoding='utf-8') as csv_file:
    fieldnames = ['你是谁', '你几岁', '你多高']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'你是谁': '小b', '你几岁': '18岁', '你多高': '18cm'})
    writer.writerow({'你是谁': '小c', '你几岁': '19岁', '你多高': '17cm'})
    writer.writerow({'你是谁': '小d', '你几岁': '20岁', '你多高': '16cm'})


# pandas ===
file = pandas.read_csv('csv_file\\csv_test.csv')
print(file)

# 另一种写入方式
b = ['小b', '小c', '小d']
c = ['18岁', '19岁', '20岁']
d = ['18cm', '17cm', '16cm']

df = pandas.DataFrame({'你是谁' : b, '你几岁' : c, '你多高' : d})
df.to_csv("csv_file\\xsb.csv", index=False, sep=',')