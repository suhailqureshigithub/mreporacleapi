from datetime import date
from pydantic.main import BaseModel
from sqlalchemy.sql.expression import _True, column, true
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Float
from database.database import Base,oracleSessionLocal
from sqlalchemy import Integer,String,Date


class MrepSasData(Base):
    __tablename__ = 'sas_mrep_data'
    IND=Column(String, primary_key=True)
    BR_CD=Column(String)
    BILL_NO=Column(Integer)
    BILL_DT=Column(Date, index=True)
    EBS_CUST=Column(Integer)
    CUSTOMER_NAME=Column(String)
    ADD1=Column(String)
    ADD2=Column(String)
    ADD3=Column(String)
    CH_CD=Column(String)
    ITEM_CODE=Column(String)
    description=Column(String)
    BATCH_NO=Column(String)
    price=Column(Float)
    SOLD_QTY=Column(Integer)
    BON_QTY = Column(Integer)
    disc_amt=Column(Float)
    NET_amt=Column(Float)
    GROSS_VALUE=Column(Float)
    discounted_rate=Column(Float)
    reason = Column(String)

# class MrepSasData(Base):
#     __tablename__='sas_mrep_data'
#     IND=Column(String,primary_key=True)
#     INVOICE=Column(Integer, index=True)
#     INVOICEDATE=Column(Date,index=True)
#     PRODCODE=Column(String)
#     BATCH=Column(String)
#     TRADEPRICE=Column(Float)
#     UNITS=Column(Integer)
#     BONUS=Column(Integer)
#     DISCOUNT=Column(Float)
#     NETVALUE=Column(Float)
#     FLAG=Column(String)
#     CUSTOMERCODE=Column(String)
#     CUSTOMERNAME=Column(String)
#     ADDRESS1=Column(String)
#     ADDRESS2=Column(String)
#     PHONE=Column(String)
#     LICENSE=Column(String)
#     AREACODE=Column(String)
#     AREANAME=Column(String)
