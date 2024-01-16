from typing import List
from fastapi import APIRouter, Depends, status, Response
from .. import schemas, database, oauth2
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)


# Search all blogs created by an user
@router.get('/', response_model = List[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

# Created a blog and storage in the database
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    blog.create(request, db)

#Delete a blog
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int,db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)


# Update blog
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)


# Search a blog
# @app.get('/blog', response_model = List[schemas.ShowBlog], tags=['Blogs'])
# def all(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs


# Find a specific blog by id
@router.get('/{id}', status_code=200, response_model = schemas.ShowBlog)
def show(id: int, response: Response, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)
