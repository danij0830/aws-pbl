import pymysql
import boto3

ssm = boto3.client('ssm')
parameter = ssm.get_parameter(Name='/myweb/database1_password', WithDecryption=True)
# print(parameter['Parameter']['Value'])

conn = pymysql.connect(host='database-1.cqcj9uctjs3w.ap-northeast-2.rds.amazonaws.com', \
                       db='pbldb', port=3306, passwd=parameter['Parameter']['Value'], user='admin')
cursor = conn.cursor()
sql = 'insert into test values (2,"정다은");'
cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()



