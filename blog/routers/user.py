from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..hashing import Hash


router = APIRouter()

# Create an user
@router.post('/user', response_model = schemas.ShowUser, tags=['Users'])
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    new_user = models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# Find a specific user
@router.get('/user', response_model = schemas.ShowUser, tags=['Users'])
def get_user(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with the id {id} is not available")
    
    return user