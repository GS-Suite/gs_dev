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
-- Contains `GS_DATABASE_URL`

-- To load the variables:
- `pipenv run pip freeze > .\requirements.txt`
- `pipenv install`

---