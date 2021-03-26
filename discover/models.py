from db_setup.pg_setup import SessionLocal, Base
from user.models import User


db = SessionLocal()


async def search_user_name(query):    
    return db.query(User).filter(
        User.first_name.match(f"{query}") | User.last_name.match(f"{query}")
    ).all()


async def search_username(query):
    return db.query(User).filter(
        User.username.match(f"{query}")
    ).all()


async def search_email(query):
    return db.query(User).filter(
        User.email.match(f"{query}")
    ).all()



async def search(query, filter):
    print(query, filter)
    return False