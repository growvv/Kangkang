import pymysql

def update(id, flag=True):
    # 打开数据库连接
    db = pymysql.connect(
        host = '47.94.83.51',
        #host = '127.0.0.1',
        port = 3306,
        user = 'root',
        passwd = '123456',
        db = 'express_demo'
    )
    
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    
    # SQL 更新语句
    if flag:
        sql = "UPDATE details SET masknum = masknum + 1 WHERE id = '%d'" % (id)
    else:
        sql = "UPDATE details SET nomasknum = nomasknum + 1 WHERE id = '%d'" % (id)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
    
    # 关闭数据库连接
    db.close()
fo = open("out.txt",'r')
temp = fo.read()
fo.close()
if temp == '1':
    update(4, True)
else:
    update(4,False)
