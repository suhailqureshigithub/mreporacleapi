from datetime import date
from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import Date, String,Integer


class Emp(BaseModel):
    EMPNO:str
    ENAME:str
    JOB:str
    MGR:str
    HIREDATE:date
    SAL:int
    COMM:int
    DEPTNO:int


class EmpHireDate(BaseModel):
    HIREDATE:date


