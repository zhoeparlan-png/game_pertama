import sqlite3

# 1. Bikin database sementara di RAM (biar cepet kyk i7!)
db = sqlite3.connect(':memory:')
cursor = db.cursor()
cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
cursor.execute("INSERT INTO users VALUES ('admin', 'RahasiaRiz123')")

print("--- SELAMAT DATANG DI LAB SQLi RIZ ---")

# 2. Input dari "Hacker" Riz
# Coba masukin ini nanti: ' OR '1'='1
input_user = input("Masukkan Password Admin: ")

# 3. Kodingan "BENGEK" (Gampang Jebol)
# Kita pake f-string biar input lu langsung masuk ke perintah SQL
query = f"SELECT * FROM users WHERE username='admin' AND password='{input_user}'"

print(f"\nQuery yang jalan di mesin: \n{query}\n")

# 4. Eksekusi
cursor.execute(query)
result = cursor.fetchone()

if result:
    print("ALHAMDULILLAH, LOGIN BERHASIL! 🔓✅")
    print(f"Data ditemukan: {result}")
else:
    print("LOGIN GAGAL! 🚫❌")