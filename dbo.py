import pyodbc,json

conn = pyodbc.connect('Driver={SQL Server};' 
'Server=192.168.0.117,3133;' 
'Database=unityprod_17092019;'
'uid=unityAppUser;pwd=Winter@2019')

command= ("SELECT * FROM dbo.GenderIdentity2020;")

cursor= conn.cursor().execute(command)

# results = cursor.execute(command)

results = []

columns = [column[0] for column in cursor.description]
print(columns)

for row in cursor.fetchall():
    results.append(dict(zip(columns,row)))

with open("db.txt", "w", encoding="utf-8") as writeJsonfile:
    json.dump(results, writeJsonfile, indent=4)


