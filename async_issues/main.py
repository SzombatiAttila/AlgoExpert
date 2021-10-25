import time
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/ping")
def ping():
    return {"Successful ping": 200}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/email/{email}")
def get_user_data_by_email(email: str):
    if email[0] in ['a', 'b', 'c', 'd']:
        print(f'The process is heavy, more time needed to the send the response for the email : {email}')
        time.sleep(5)
    return {f"Job seeker with the email: {email} is": "OK"}