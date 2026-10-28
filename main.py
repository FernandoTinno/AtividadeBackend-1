from fastapi import FastAPI
from routes import router


app = FastAPI()

#como eu separei o codigo em arquivos diferentes(por questões de legibilidade) eu utilizei o include router para puxar as rotas apartir de outro arquivo(routes.py)
app.include_router(router)





