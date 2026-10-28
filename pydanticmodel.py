
from pydantic import BaseModel

# pydantic serve para definir a estrutura(taskbase),validação(taskcreate) e retorno(taskresponse) dos dados que seram inseridos e exibidos pela api
class TaskBase(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False

# Este é o modelo para criação/atualização, e como não tem nada a acrescentar, utilizei somente o Taskbase.
class TaskCreate(TaskBase):
    pass

# Modelo para a saída de dados usando a taskbase em conjunto com o id, para que o uruario tenha conhecimento de qual id está referenciando a tarefa que foi criada
class TaskResponse(TaskBase):
    id: int