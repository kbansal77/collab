from fastapi import APIRouter, HTTPException
import psycopg2
from models import User


router = APIRouter()

'''
Easy Reference

uid: col 0
name: col 1
linkedin: col 2
github: col 3
website: col 4
year: col 5
email: col 6
posts_created: col 7
posts_applied: col 8
posts_saved: col 9
resume: col 10
'''


@router.get("/")
def get_all_users():
    conn = psycopg2.connect(
        host="localhost",
        database="collab",
        user="postgres",
        password="password",
        port=5432
    )

    cur = conn.cursor()

    try:
        cur.execute("select * from users")
        rows = cur.fetchall()
        users = []
        for row in rows:
            users.append({
                "uid": row[0],
                "name": row[1],
                "linkedin": row[2],
                "github": row[3],
                "website": row[4],
                "year": row[5],
                "email": row[6],
                "posts_created": row[7],
                "posts_applied": row[8],
                "posts_saved": row[9],
                "resume": row[10]
            })

        return users

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))

    finally:
        cur.close()
        conn.close()


@router.get("/{user_id}")
def get_user(user_id):
    conn = psycopg2.connect(
        host="localhost",
        database="collab",
        user="postgres",
        password="password",
        port=5432
    )
    cur = conn.cursor()

    try:
        cur.execute("select * from users where uid = %s", (user_id,))
        row = cur.fetchone()
        user = {
            "uid": row[0],
            "name": row[1],
            "linkedin": row[2],
            "github": row[3],
            "website": row[4],
            "year": row[5],
            "email": row[6],
            "posts_created": row[7],
            "posts_applied": row[8],
            "posts_saved": row[9],
            "resume": row[10]
        }

        return user

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))

    finally:
        cur.close()
        conn.close()


@router.post("/add/{user_id}")
def add_user(user_id, user: User):
    conn = psycopg2.connect(
        host="localhost",
        database="collab",
        user="postgres",
        password="password",
        port=5432
    )
    cur = conn.cursor()

    try:

        cur.execute(
            "insert into users values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (user_id, user.name, user.linkedin, user.github,
             user.website, user.year, user.email, user.posts_created,
             user.posts_applied, user.posts_saved, user.resume)
        )

        conn.commit()

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))

    finally:
        cur.close()
        conn.close()


@router.delete("/{user_id}")
def delete_user(user_id):
    conn = psycopg2.connect(
        host="localhost",
        database="collab",
        user="postgres",
        password="password",
        port=5432
    )
    cur = conn.cursor()

    try:

        cur.execute("delete from users where uid = (%s)", (user_id,))

        conn.commit()

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))

    finally:
        cur.close()
        conn.close()
