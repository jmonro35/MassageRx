from app.scoring import get_db

db = get_db()
print("Connection successful")
db.close()
