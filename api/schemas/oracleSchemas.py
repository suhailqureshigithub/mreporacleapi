from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel
from pydantic.fields import Field
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.sqltypes import INT, Date, String,Integer

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

class MrepSasData(BaseModel):
    INVOICEDATE:date
    INVOICE:int
    PRODCODE:str
    BATCH:str
    TRADEPRICE:float
    UNITS:int
    BONUS:int
    DISCOUNT:float
    NETVALUE:float
    FLAG:str
    CUSTOMERCODE:str
    CUSTOMERNAME:str
    ADDRESS1:str
    ADDRESS2:str
    PHONE:str
    LICENSE:str
    AREACODE:str
    AREANAME:str

    class Config():
        orm_mode=True

#

class MrepCustomer(BaseModel):
    CUSTOMERCODE:str=Field(alias='Customer Code')
    CUSTOMERNAME:str=Field(alias='Customer Name')
    ADDRESS1:str=Field(alias='Address1')
    ADDRESS2:Optional[str]=Field(alias='Address2')
    PHONE:str=Field(alias='Phone')
    LICENSE:Optional[str]=Field(alias='License')
    AREACODE:Optional[str]=Field(alias='Area Code')
    AREANAME:Optional[str]=Field(alias='Area Name')
    class Config():
        orm_mode=True
        allow_population_by_field_name = True





