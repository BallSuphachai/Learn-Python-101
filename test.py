
import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(user='root',password='mo0827975251',host='localhost',database='world')

# Create a cursor
db_cursor = cnx.cursor()

#สร้าง String ไว้รอใส่คำสั่งสำหรับการ SELECT
db_cursor.execute("SELECT * FROM country")

#ดึงข้อมูลมาเก็บไว้ใน result
result = db_cursor.fetchall()

#แสดงผลข้อมูลมาทีละตัวจากที่ SELECT ได้ทั้งหมด
for data in result:
  print(data)