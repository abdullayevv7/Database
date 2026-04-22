# #13.04.2026
import sqlite3 as sql

with sql.connect("baza.db") as con:
    cur = con.cursor()
    
    
    cur.execute("""CREATE TABLE IF NOT EXISTS students ( 
        id INTEGER PRIMARY KEY,
        first_name TEXT, 
        last_name TEXT,
        age INTEGER
    )""")
    
    cur.execute("""CREATE  TABLE IF NOT EXISTS xaridlar ( 
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        product_name TEXT,
        price INTEGER
    )""")
    
    cur.execute("""INSERT OR IGNORE INTO students (id, first_name, last_name, age)
                VALUES (1, 'Abdulaziz', 'Palvanbayev', 15)""")
    
    cur.execute("""INSERT OR IGNORE INTO students (id, first_name, last_name, age)
                VALUES (2, 'Shokirchon', 'Salayev', 17)""")
    
    
    cur.execute("""INSERT OR IGNORE INTO xaridlar (id, student_id, product_name, price)
                VALUES (1, 1, 'Uzum', 10000)""")
    
    cur.execute("""INSERT OR IGNORE INTO xaridlar (id, student_id, product_name, price)
                VALUES (2, 1, 'Anor', 40000)""")
    
    cur.execute("""INSERT OR IGNORE INTO xaridlar (id, student_id, product_name, price)
                VALUES (3, 1, 'Qazi', 150000)""")
    
    cur.execute("""INSERT OR IGNORE INTO xaridlar (id, student_id, product_name, price)
                VALUES (4, 2, 'Noutbook', 5000000)""")
    
    
    
    
    
    
    
# #15.04.2026


    # con.commit()
    #
    # # # # Ma'lumotlarni chiqarish
    #
    # print("=== Foydalanuvchilar ===")
    # cur.execute("SELECT * FROM users")
    # for row in cur.fetchall():
    #     print(row)
    #
    # print("\n=== Xaridlar ===")
    # cur.execute("SELECT * FROM xaridlar")
    # for row in cur.fetchall():
    #     print(row)
    
    
    
    
    


# #16.04.2026

# """CRUD asoslari (CREATE, INSERT, UPDATE, DELETE)"""

# """
# ==============================================================
#   DATABASE COURSE
#   MAVZU: MAKTAB AXBOROT TIZIMI (School Information System)

#   SELECT bo'yicha chuqurlashtirilgan dars:
#      - ORDER BY  (saralash)
#      - LIMIT     (chegaralash)
#      - LIKE      (matn qidirish)
#      - BETWEEN   (oraliq)
#      - IN        (ro'yxatdan)
#      - DISTINCT  (takrorlanmaydigan)
#      - COUNT, SUM, AVG, MIN, MAX  (aggregate funksiyalar)
#      - GROUP BY  (guruhlash)
#      - HAVING    (guruh filtri)

#   Maqsad: O'quvchilar, fanlar va baholar jadvallaridan
#           professional darajada ma'lumot olishni o'rganish.
# ==============================================================
# """







# #22.04.2026

oquvchilar_royxati = [
    # (id,   ism,         familiya,       sinf,   tugilgan_yil,   telefon)
    (1,     'Rasul',        'Xakimbayev',   10,     2008,           '998901234567'),
    (2,     'Durbek',       'Hayotbekov',   11,     2007,           '998901234568'),
    (3,     'Bexruz',       'Jumaboyev',    9,      2009,           '998901234569'),
    (4,     'Lazoyev',      'Behzod',       12,     2006,           '998901234570'),
    (5,     'Farhodjohn',   'Abdullayev',   10,     2008,           '998901234571'),
    (6,     'Sarvar',       'Salimov',      11,     2007,           '998901234572'),
    (7,     'Bexruz',       'Axmedov',      9,      2009,           '998901234573'),
    (8,     'Bexruz',       'Qurbonov',     12,     2006,           '998901234574'),
    (9,     'Bekzod',       'Arkayev',      10,     2008,           '998901234575'),
    (10,    'Alijon',       'Shokirov',     11,     2007,           '998901234576'),
]
cur.executemany(
    "INSERT OR IGNORE INTO oquvchilar VALUES (?, ?, ?, ?, ?, ?)",
        oquvchilar_royxati
)

fanlar_royxati = [
    # (id,   nomi,            oqituvchi,              haftalik_soat)
    (1,     'Matematika',     'Aliyev Ali',           5),
    (2,     'Fizika',         'Nuriddinov Jamshid',   4),
    (3,     'Informatika',    'Karimov Bobur',        3),
    (4,     'Kimyo',          'Rahmonov Said',        4),
    (5,     'Biologiya',      'Azimova Zohra',        3),
    (6,     'Tarix',          'Ibrohimov Ibrohim',    2),
    (7,     'Geografiya',     'Juraev Jura',          2),
    (8,     'Adabiyot',       'Karimova Karimah',     2),
    (9,     'Ingliz tili',    'Smith John',           3),
    (10,    'Rus tili',       'Ivanov Ivan',          3)
]
cur.executemany(
    "INSERT OR IGNORE INTO fanlar VALUES (?, ?, ?, ?)",
    fanlar_royxati
)

baholar_royxati = [
        # (id, oquvchi_id, fan_id, ball, sana)
        # Bekzod Karimov (1)
        (1,  1, 1, 92, '2026-04-05'),  (2,  1, 2, 78, '2026-04-08'),
        (3,  1, 3, 85, '2026-04-12'),  (4,  1, 5, 88, '2026-04-15'),
        (5,  1, 8, 95, '2026-04-18'),
        # Madina Yusupova (2)
        (6,  2, 1, 98, '2026-04-05'),  (7,  2, 2, 95, '2026-04-08'),
        (8,  2, 3, 90, '2026-04-12'),  (9,  2, 4, 96, '2026-04-14'),
        (10, 2, 5, 92, '2026-04-15'),
        # Aziz Rahimov (3)
        (11, 3, 1, 65, '2026-04-05'),  (12, 3, 2, 70, '2026-04-08'),
        (13, 3, 3, 58, '2026-04-12'),  (14, 3, 6, 75, '2026-04-16'),
        # Nilufar Tursunova (4)
        (15, 4, 1, 88, '2026-04-05'),  (16, 4, 4, 94, '2026-04-14'),
        (17, 4, 5, 90, '2026-04-15'),  (18, 4, 6, 85, '2026-04-16'),
        # Jasur Nazarov (5)
        (19, 5, 1, 72, '2026-04-05'),  (20, 5, 7, 80, '2026-04-17'),
        (21, 5, 8, 88, '2026-04-18'),
        # Sevara Ismoilova (6)
        (22, 6, 3, 95, '2026-04-12'),  (23, 6, 4, 92, '2026-04-14'),
        (24, 6, 6, 89, '2026-04-16'),
        # Otabek Sharipov (7)
        (25, 7, 2, 82, '2026-04-08'),  (26, 7, 8, 91, '2026-04-18'),
        # Dilnoza Karimova (8)
        (27, 8, 1, 86, '2026-04-05'),  (28, 8, 5, 94, '2026-04-15'),
        (29, 8, 6, 88, '2026-04-16'),
        # Alisher Xolmatov (9)
        (30, 9, 2, 76, '2026-04-08'),  (31, 9, 7, 85, '2026-04-17'),
        # Gulnora Abdullayeva (10)
        (32, 10, 3, 89, '2026-04-12'), (33, 10, 4, 91, '2026-04-14'),
        (34, 10, 5, 87, '2026-04-15'),
        # Sherzod Mirzayev (11)
        (35, 11, 1, 55, '2026-04-05'), (36, 11, 2, 60, '2026-04-08'),
        (37, 11, 8, 78, '2026-04-18'),
        # Zarina Saidova (12)
        (38, 12, 5, 96, '2026-04-15'), (39, 12, 6, 93, '2026-04-16'),
        (40, 12, 7, 90, '2026-04-17'),
    ]
cur.executemany(
        "INSERT OR IGNORE INTO baholar VALUES (?, ?, ?, ?, ?)",
        baholar_royxati
    )

con.commit()

    # Natijalarni chiroyli chiqarish uchun yordamchi funksiya
def chiqar(sarlavha, qatorlar):
        print("\n" + "=" * 65)
        print(f"  {sarlavha}")
        print("=" * 65)
        if not qatorlar:
            print("  (natija bo'sh)")
            return
        for q in qatorlar:
            print(" ", q)