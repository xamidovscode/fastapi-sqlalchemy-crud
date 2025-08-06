# 🚀 FastAPI, SQLAlchemy (Async) va Alembic bilan Ishlashni Boshlash

Yangi FastAPI loyihangizga xush kelibsiz! Ushbu hujjat loyiha tuzilishini tushunish, ishlab chiqish muhitini sozlash va kuchli asinxron API’lar qurishni boshlash bo‘yicha to‘liq qo‘llanmani taqdim etadi.

## 🌟 Loyiha Umumiy Ko‘rinishi

Ushbu shablon loyiha zamonaviy Python asinxron stekidan foydalangan holda kuchli va kengaytiriladigan veb API’lar yaratish uchun mo‘ljallangan. U kodni aniq ajratish, texnik xizmat ko‘rsatish osonligi va ma’lumotlar bazasi bilan ishlashda eng yaxshi amaliyotlarga e’tibor qaratadi.

**Asosiy Texnologiyalar:**

* **FastAPI:** Python 3.7+ uchun zamonaviy, yuqori samarali API framework, standart Python type hints asosida.
* **SQLAlchemy (Async):** Python uchun kuchli va moslashuvchan SQL vositasi va ORM, asinxron ma’lumotlar bazasi operatsiyalariga moslashtirilgan.
* **Alembic:** SQLAlchemy uchun engil migratsiya vositasi, ma’lumotlar bazasi sxemasi o‘zgarishlarini tizimli boshqarish imkonini beradi.
* **`asyncpg` (yoki `aiosqlite`):** PostgreSQL uchun (yoki tezkor testlashda SQLite) asinxron ma’lumotlar bazasi drayverlari.
* **Pydantic:** Ma’lumotlarni tekshirish va sozlamalarni boshqarish uchun Python type hints’dan foydalanadi.

## 📁 Loyiha Tuzilishi

Loyiha kodni tartibli va kengaytiriladigan holda saqlash uchun modulga asoslangan qatlamli arxitekturadan foydalanadi.

```
.
├── main.py                     # FastAPI ilova ishga tushirish nuqtasi
├── app/
│   ├── __init__.py             # 'app'ni Python paketi qiladi
│   ├── core/
│   │   ├── config.py           # Ilova sozlamalari (Pydantic BaseSettings)
│   │   └── database.py         # SQLAlchemy engine, session, base va dependency
│   ├── api/
│   │   ├── v1/                 # API versiyalash (masalan, /api/v1)
│   │   │   ├── endpoints/      # API endpointlari (masalan, users.py)
│   │   │   └── api.py          # v1 uchun asosiy API router
│   ├── crud/                   # CRUD amaliyotlari (Create, Read, Update, Delete)
│   │   ├── base.py             # Umumiy CRUDBase qayta foydalanish uchun
│   │   └── user.py             # User modeliga oid CRUD amallar
│   ├── models/                 # SQLAlchemy ORM modellari (jadval ta’riflari)
│   │   └── user.py             # User modeli
│   └── schemas/                # Pydantic modellar (so‘rov/javobni tekshirish)
│       └── user.py             # User sxemalari (Base, Create, Update, InDB)
├── alembic/                    # Alembic migratsiya katalogi
│   ├── versions/               # Yaratilgan migratsiya skriptlari
│   └── env.py                  # Alembic muhit fayli (async bilan sozlangan)
├── alembic.ini                 # Alembic konfiguratsiya fayli
├── requirements.txt            # Loyiha bog‘liqliklari
└── .env                        # Muhit o‘zgaruvchilari (masalan, DATABASE_URL)
```

### Asosiy katalog va fayllar izohi:

* **`main.py`**: FastAPI ilovasini ishga tushiruvchi fayl. Ilovani va API routerlarini yuklaydi.
* **`app/core/`**: Asosiy komponentlar, konfiguratsiya (`config.py`) va ma’lumotlar bazasi sozlamalari (`database.py`).
* **`app/api/`**: API endpointlari, versiya bo‘yicha tashkil etilgan (`v1/`).

  * `endpoints/`: Har bir fayl ma’lum bir resurs yo‘llarini belgilaydi (masalan, `users.py`).
  * `api.py`: Ushbu versiya uchun barcha routerlarni birlashtiradi.
* **`app/crud/`**: Ma’lumotlar bazasi bilan ishlash uchun mantiq.

  * `base.py`: Umumiy CRUDBase klassi, asosiy CRUD operatsiyalarini takroriy kodsiz amalga oshirish uchun.
  * `user.py`: User modeli uchun maxsus CRUD amallar.
* **`app/models/`**: SQLAlchemy ORM modellarini, ya’ni ma’lumotlar bazasi jadvallarini belgilaydi.
* **`app/schemas/`**: Pydantic modellar:

  * **So‘rovlarni tekshirish:** Kelayotgan ma’lumotlar turlari va strukturasi to‘g‘riligini tekshiradi.
  * **Javoblarni serializatsiya qilish:** API qaytaradigan ma’lumotlar tuzilishini belgilaydi.
  * **Ma’lumotlar bazasi bilan ishlash:** Yangi yozuvlar yaratish yoki yangilash uchun ma’lumotlar strukturasini belgilaydi.
* **`alembic/`**: Ma’lumotlar bazasi migratsiyalari uchun katalog.

  * `env.py`: Alembic’ni SQLAlchemy bilan ishlashga moslashtiradi, ayniqsa async operatsiyalar va `app` modulini aniqlash uchun muhim.
* **`.env`**: Muhitga xos ma’lumotlar (masalan, DB ulanish satri). **Bu faylni Git’ga qo‘shmang!**

---

## 🚀 Ishga Tushirish Bo‘yicha Qo‘llanma

### 1. Talablar

* Python 3.8+
* `pip` (Python paket o‘rnatish vositasi)
* PostgreSQL ma’lumotlar bazasi (yoki SQLite tezkor test uchun)

### 2. Repozitoriyani klonlash

```bash
git clone <your-repo-url>
cd <your-project-directory>
```

### 3. Virtual muhit yaratish

```bash
python -m venv .venv
source .venv/bin/activate  # Windows’da: .venv\Scripts\activate
```

### 4. Bog‘liqliklarni o‘rnatish

```bash
pip install -r requirements.txt
# Agar requirements.txt yo‘q bo‘lsa:
# pip install fastapi uvicorn "sqlalchemy[asyncio]" "asyncpg" alembic pydantic-settings
# keyin:
# pip freeze > requirements.txt
```

### 5. `.env` faylni sozlash

**PostgreSQL uchun:**

```
DATABASE_URL="postgresql+asyncpg://user:password@host:port/dbname"
```

**SQLite uchun (tezkor test):**

```
DATABASE_URL="sqlite+aiosqlite:///./sql_app.db"
```

---

### 6. Alembicni boshlang‘ich sozlash

```bash
alembic init alembic
```

So‘ng `alembic/env.py` faylini loyihadagi async konfiguratsiya bilan almashtiring.

---

### 7. Migratsiyalarni ishga tushirish

Yangi migratsiya yaratish:

```bash
alembic revision --autogenerate -m "Add initial tables"
```

Migratsiyani qo‘llash:

```bash
alembic upgrade head
```

---

### 8. FastAPI ilovasini ishga tushirish

```bash
uvicorn main:app --reload
```

API odatda `http://127.0.0.1:8000` da ishlaydi.

---

### 9. API hujjatlarini ko‘rish

* Swagger UI: `http://127.0.0.1:8000/api/v1/docs`
* ReDoc: `http://127.0.0.1:8000/api/v1/redoc`

---

## 💡 Muhim tushunchalar

* **Asinxron dasturlash (`async`/`await`):** FastAPI asinxron arxitekturaga asoslangan. Ma’lumotlar bazasi amallari va boshqa I/O vazifalar `await` bilan bajarilishi kerak.
* **Dependency Injection:** `Depends` yordamida DB sessiya (`get_db`), autentifikatsiya va qayta ishlatiladigan komponentlarni boshqarish.
* **Pydantic:** So‘rov va javoblar uchun ma’lumotlarni tekshirish va serializatsiya qilish.
* **SQLAlchemy ORM:** Ma’lumotlar bazasi bilan Python obyektlari orqali ishlash, xatolarni kamaytiradi.
* **Generic CRUD (`app/crud/base.py`):** Yangi model qo‘shishda CRUDBase’dan foydalanish kodni kamaytiradi.

---

## 🛠️ Kengaytirish

* **Yangi model qo‘shish:**

  1. `app/models/` ichida yangi model yarating.
  2. `app/schemas/` ichida sxemalar yarating.
  3. `app/crud/` ichida CRUD fayl yarating.
  4. `app/api/v1/endpoints/` ichida endpoint yarating.
  5. Routerni `app/api/v1/api.py`ga qo‘shing.
  6. Migratsiya yaratib, qo‘llang.

* **Autentifikatsiya qo‘shish:** OAuth2, JWT kabi xavfsizlik xususiyatlarini qo‘shing.

* **Xatolarni boshqarish:** Maxsus exception handlerlar qo‘shing.

* **Loglash:** Debug va monitoring uchun loglar qo‘shing.

---

## 📚 Qo‘shimcha manbalar

* [FastAPI Hujjatlari](https://fastapi.tiangolo.com/)
* [SQLAlchemy Hujjatlari](https://docs.sqlalchemy.org/en/20/)
* [Alembic Hujjatlari](https://alembic.sqlalchemy.org/en/latest/)
* [Pydantic Hujjatlari](https://docs.pydantic.dev/latest/)

---

Ushbu hujjat sizga FastAPI, SQLAlchemy va Alembic bilan ishlash uchun mustahkam asos beradi.
