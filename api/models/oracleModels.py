from datetime import date
from pydantic.main import BaseModel
from sqlalchemy.sql.schema import Column
# from ..database import oracleSessionLocal
from ..database.database import Base,oracleSessionLocal
from sqlalchemy import Integer,String,Date

class Emp(Base):
    __tablename__='emp'
    EMPNO=Column(Integer,primary_key=True,index=True)
    ENAME=Column(String)
    JOB=Column(String)
    MGR=Column(String)
    HIREDATE=Column(Date)
    SAL=Column(Integer)
    COMM=Column(Integer)
    DEPTNO=Column(Integer)



