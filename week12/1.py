import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="onefit",
    user="pp2",
    password="pp2password"
)

sql = 'select id, user_type, subscription_id from authe_usertype where subscription_id=63'

cursor = conn.cursor()
cursor.execute(sql)
all_rows = cursor.fetchall()
print(all_rows)


# for row in cursor:
#     print(row)

cursor.close()
conn.close()

