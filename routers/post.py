from fastapi import APIRouter, HTTPException, Request
from models import Post
import psycopg2
import uuid


router = APIRouter()


'''
Easy Reference

post_id: col 0
post_title: col 1
post_cover: col 2
post_description: col 3
last_date: col 4
tech_stack: col 5
roles: col 6
event: col 7
eligible_years: col 8
responses: col 9
created_by: col 10
archive: col 11
qualifications: col 12
responsibilities: col 13
duration: col 14
'''


@router.get("/")
def get_all_posts():
    conn = psycopg2.connect(
        host="localhost",
        database="collab",
        user="postgres",
        password="password",
        port=5432
    )

    cur = conn.cursor()

    try:
        cur.execute("select * from posts")
        rows = cur.fetchall()
        posts = []
        for row in rows:
            posts.append({
                "post_id": row[0],
                "post_title": row[1],
                "post_cover": row[2],
                "post_description": row[3],
                "last_date": row[4],
                "tech_stack": row[5],
                "roles": row[6],
                "event": row[7],
                "eligible_years": row[8],
                "responses": row[9],
                "created_by": row[10],
                "archive": row[11],
                "qualifications": row[12],
                "responsibilities": row[13],
                "duration": row[14]
            })

        return posts

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))

    finally:
        cur.close()
        conn.close()


@router.get("/{post_id}")
def get_post(post_id):
    conn = psycopg2.connect(
        host="localhost",
        database="collab",
        user="postgres",
        password="password",
        port=5432
    )
    cur = conn.cursor()

    try:
        cur.execute("select * from posts where post_id = %s", (post_id,))
        row = cur.fetchone()
        post = {
            "post_id": row[0],
            "post_title": row[1],
            "post_cover": row[2],
            "post_description": row[3],
            "last_date": row[4],
            "tech_stack": row[5],
            "roles": row[6],
            "event": row[7],
            "eligible_years": row[8],
            "responses": row[9],
            "created_by": row[10],
            "archive": row[11],
            "qualifications": row[12],
            "responsibilities": row[13],
            "duration": row[14]
        }

        return post

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))

    finally:
        cur.close()
        conn.close()


@router.post("/add")
def add_post(post: Post, request: Request):
    conn = psycopg2.connect(
        host="localhost",
        database="collab",
        user="postgres",
        password="password",
        port=5432
    )
    cur = conn.cursor()

    uid = request.headers.get("uid")

    try:

        cur.execute("insert into posts values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (str(uuid.uuid4()), post.post_title, post.post_cover,
                     post.post_description, post.last_date, post.tech_stack,
                     post.roles, post.event, post.eligible_years,
                     post.responses, uid, post.archive,
                     post.qualifications, post.responsibilities, post.duration)
                    )

        conn.commit()

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))

    finally:
        cur.close()
        conn.close()


@router.delete("/{post_id}")
def delete_post(post_id):
    conn = psycopg2.connect(
        host="localhost",
        database="collab",
        user="postgres",
        password="password",
        port=5432
    )
    cur = conn.cursor()

    try:

        cur.execute("delete from posts where post_id = (%s)", (post_id,))

        conn.commit()

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))

    finally:
        cur.close()
        conn.close()


@router.post("/register/{post_id}")
def register_for_post(post_id, request: Request):
    conn = psycopg2.connect(
        host="localhost",
        database="collab",
        user="postgres",
        password="password",
        port=5432
    )
    cur = conn.cursor()
    uid = request.headers.get("uid")

    try:

        cur.execute(
            "select responses from posts where post_id = (%s)", (post_id,))
        row = cur.fetchone()
        responses = row[0]
        if uid not in responses:
            responses.append(uid)
            cur.execute(
                "update posts set responses = (%s) where post_id = (%s)",
                (responses, post_id))
            cur.execute("select posts_applied from users where uid = (%s)",
                        (uid,))
            row = cur.fetchone()
            posts_applied = row[0]
            if post_id not in posts_applied:
                posts_applied.append(post_id)
                cur.execute(
                    "update users set posts_applied = (%s) where uid = (%s)",
                    (posts_applied, uid))
            else:
                raise Exception("Post already applied for")
        else:
            raise Exception("User already registered")

        conn.commit()

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))

    finally:
        cur.close()
        conn.close()


@router.post("/save/{post_id}")
def save_post(post_id, request: Request):
    conn = psycopg2.connect(
        host="localhost",
        database="collab",
        user="postgres",
        password="password",
        port=5432
    )
    cur = conn.cursor()

    uid = request.headers.get("uid")

    try:

        cur.execute("select posts_saved from users where uid = (%s)", (uid,))
        row = cur.fetchone()
        posts_saved = row[0]
        if post_id not in posts_saved:
            posts_saved.append(post_id)
            cur.execute(
                "update users set posts_saved = (%s) where uid = (%s)",
                (posts_saved, uid))
        else:
            raise Exception("Post already saved")

        conn.commit()

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))

    finally:
        cur.close()
        conn.close()
