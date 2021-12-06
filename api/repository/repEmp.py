from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from ..database import database
from ..models import oracleModels
from datetime import date

def getByHireDate(hireDate, db: Session ):
    empList=db.query(oracleModels.Emp).filter(oracleModels.Emp.HIREDATE==hireDate).all()
    if not empList:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND
                            ,detail=f'Record not found with given date {hireDate}')
    return empList

def getAllEmp(db: Session ):
    empList=db.query(oracleModels.Emp).all()
    return empList