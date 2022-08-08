from fastapi import FastAPI
import uvicorn
from routers import chinese, english
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__)))

app = FastAPI()

app.include_router(chinese.router)
app.include_router(english.router)


@app.get('/', tags=['首页'])
def index():
    return {'msg': '进入 /docs 查看文档'}


if __name__ == '__main__':
    uvicorn.run(app='main:app', host='0.0.0.0', port=1234, reload=True, debug=True)
