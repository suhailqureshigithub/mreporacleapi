
from datetime import date, datetime
from fastapi import FastAPI
from.routers import routEmp

app=FastAPI()
app.include_router(routEmp.router)

@app.get('/')
def wellcome():
    return 'wellcome...'

