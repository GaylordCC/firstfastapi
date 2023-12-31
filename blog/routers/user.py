from fastapi import APIRouter, Depends
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import user


router = APIRouter(
    prefix="/user",
    tags=['Users']
)

# Create an user
@router.post('/', response_model = schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(request, db)


# Find a specific user
@router.get('/', response_model = schemas.ShowUser)
def get_user(id: int, db: Session = Depends(database.get_db)):
    return user.show(id, db)