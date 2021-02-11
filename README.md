## Login ~ FastAPI, SQLAlchemy
---
### To run the app
-- `pip install pipenv`

-- `pipenv shell`

-- `pipenv install`

-- `uvicorn main:app --reload`

---

### API Testing
-- After running the app:
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc
---

### .env.py
-- Contains `PG_DB_URL` , `MONGO_DB_URL`

---

### Alembic
-- Create a new migration: `alembic revision --autogenerate -m "<message>"`

-- Run migrations: `alembic upgrade head`

-- Check out the documentation: https://alembic.sqlalchemy.org/en/latest/tutorial.html

---