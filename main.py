from fastapi import FastAPI
from routers import user, post


tags_metadata = [
    {
        "name": "User",
        "description": "Endpoints related to operations on the **Users**\
            table."
    },
    {
        "name": "Post",
        "description": "Endpoints related to operations on the **Posts**\
            table."
    }
]

app = FastAPI(
    title="Collab Backend",
    description="Backend for the Collab website",
    version="1.0",
    openapi_tags=tags_metadata
)

app.include_router(
    user.router,
    prefix="/user",
    tags=["User"]
)

app.include_router(
    post.router,
    prefix="/post",
    tags=["Post"]
)
