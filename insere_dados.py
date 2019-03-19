import psycopg2


con = psycopg2.connect(host='isilo.db.elephantsql.com', database='srdpapsh', user='srdpapsh', password='hvk59vXo_6OaxZl05YjY95pqpT7Ia0eX')
cur = con.cursor()
sql = "CREATE TABLE cidade (id INT, nome VARCHAR(100), uf VARCHAR(2))"
cur.execute(sql)
sql = "INSERT INTO cidade(id,nome,uf) VALUES (1,'São Paulo','SP')"
cur.execute(sql)
con.commit()
cur.execute("SELECT * FROM cidade")
recset = cur.fetchall()
for rec in recset:
	print (rec)
con.close()