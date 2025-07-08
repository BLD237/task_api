from fastapi import Depends, HTTPException, status as s, APIRouter
import logging
from database import get_db
from models import Category, User
from auth import get_current_user
from datetime import datetime
from base import  CategoryCreate, CategoryResponse, CategoryFetch

router = APIRouter()
logging.basicConfig(level=logging.INFO)



@router.post("/api/categories/", response_model=CategoryResponse)
def create_category(category: CategoryCreate, current_user: User = Depends(get_current_user), db = Depends(get_db) ):
    new_category = Category(title = category.title, description = category.description, user_id =  current_user.user_id)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return {"status":"success", "message":"Category created successfully", "data": None}
 

@router.get("/api/categories/", response_model= CategoryFetch)
def read_category(current_user: User = Depends(get_current_user), db= Depends(get_db)):
     category = db.query(Category).filter(Category.user_id == current_user.user_id).all()
     if category:            
            return {"status":"success", "data":category, "message":"Data fetched successfully"}
     else:
            return {"status":"success", "data": None, "message":"No category found."}




    

@router.put("/api/categories/{category_id}")
def update_category(category_id):
    pass
@router.delete("/api/categories/{category_id}")
def delete_category(category_id, current_user: User = Depends(get_current_user), db = Depends(get_db)):
         category = db.query(Category).filter(Category.id == category_id).first()
         if category is None:
             raise HTTPException(status_code=s.HTTP_404_NOT_FOUND, detail={"status":"failed", "data":None, "message":"Category not found"})
         if category.user_id != current_user.user_id:
          raise HTTPException(status_code=s.HTTP_403_FORBIDDEN, detail={"status":"failed", "data":None, "message":"You are not authorized to access this category"})
         db.delete(category)
         db.commit()
         return {"status":"success", "data":None, "message":"Category Deleted Successfuly"}