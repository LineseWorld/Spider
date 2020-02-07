import pymysql

# 使用 connect 方法，传入数据库地址，账号密码，数据库名就可以得到你的数据库对象
address = "localhost"
user = "root"
password = "lsj123"
db_name = "pytest"
db = pymysql.connect(address, user, password, db_name)

# 接着我们获取 cursor 来操作我们的 pytest 这个数据库
cursor = db.cursor()

# 比如我们来创建一张数据表
# sql = """create table test_table (
#    name char(20) not null,
#    age int)"""
# cursor.execute(sql)

# 插入一条记录
sql = "insert into beautyGirls(name, age) values ('Mrs.cang', 18)"

try:
    cursor.execute(sql)
    db.commit()
except:
    # 回滚
    db.rollback()

# 最后我们关闭这个数据库的连接
db.close()