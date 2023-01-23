import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="tugas_uas"
)

cursor = db.cursor()
sql = "INSERT INTO peserta (name, address) VALUES (%s, %s)"
values = [
  ("dzaki", "Tangerang"),
  ("Luthfi", "Jakarta"),
  ("Bagus", "Fakfak"),
  ("Julius", "Medan")
]

for val in values:
  cursor.execute(sql, val)
  db.commit()

print("{} data ditambahkan".format(len(values)))
