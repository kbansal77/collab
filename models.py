from pydantic import BaseModel, AnyUrl, EmailStr
from typing import Optional, List, Literal
from datetime import date


class Post(BaseModel):
    post_id: Optional[str]
    post_title: Optional[str]
    post_cover: Optional[AnyUrl]
    post_description: Optional[str]
    last_date: Optional[date]
    tech_stack: Optional[List[str]]
    roles: Optional[List[str]]
    event: Optional[Literal["project", "internship", "hackathon"]]
    eligible_years: Optional[List[int]]
    responses: Optional[List[str]]
    created_by: Optional[str]
    archive: Optional[bool]
    qualifications: Optional[List[str]]
    responsibilities: Optional[List[str]]
    duration: Optional[str]


class User(BaseModel):
    uid: str
    name: Optional[str]
    linkedin: Optional[AnyUrl]
    github: Optional[AnyUrl]
    website: Optional[AnyUrl]
    year: Optional[int]
    email: Optional[EmailStr]
    posts_created: Optional[List[str]]
    posts_applied: Optional[List[str]]
    posts_saved: Optional[List[str]]
    resume: Optional[AnyUrl]
