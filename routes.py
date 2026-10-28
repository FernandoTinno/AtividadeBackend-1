from fastapi import APIRouter, HTTPException
from pydanticmodel import TaskCreate, TaskResponse
import arraydb 

# Crie um roteador em vez de usar o app principal, já que eu fiz em arquivos separados
router = APIRouter()


@router.post("/tasks/", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate):
    new_task = TaskResponse(id=arraydb.current_id, **task.model_dump())
    arraydb.tasks_db[arraydb.current_id] = new_task
    arraydb.current_id += 1
    return new_task

    # baseando na documentação do fastapi, eu criei essa logica usando o model_dump para transformar o objeto do pydantic e atribuindo um id a task que foi criada e depois faço o incremento do current id para manter a logica eu eu expliquei no arquivo arraydb.py

@router.get("/tasks/", response_model=list[TaskResponse])
def read_tasks(skip: int = 0, limit: int = 10):
    tasks_list = list(arraydb.tasks_db.values())
    return tasks_list[skip : skip + limit]

    # esse get serve para listar todos as tarefas que voce possue no momento, podendo ignorar alguma tarefa(alterando a variavel skip) ou aumentar o limite de quantas tarefas seram exibidas(mudando a variavel limit)

@router.get("/tasks/{task_id}", response_model=TaskResponse)
def read_task(task_id: int):
    if task_id not in arraydb.tasks_db:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return arraydb.tasks_db[task_id]

    # aqui basicamente ele faz uma busca no "banco de dados", baseando-se no id que o usuario colocar, se não achar o id que o usuario colocou, é gerado uma mensagem de erro

@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskCreate):
    if task_id not in arraydb.tasks_db:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
         
    updated_task = TaskResponse(id=task_id, **task.model_dump())
    arraydb.tasks_db[task_id] = updated_task
    return updated_task

    # por meio do Id, ele identifica uma tarefa, e permite mudar o titulo, descrição e o booleano(True ou False) se está concluido ou não

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in arraydb.tasks_db:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
         
    del arraydb.tasks_db[task_id]
    return {"message": "Tarefa excluída com sucesso"}

    # deleta a tarefa pelo id, caso não encontrar o id, ele retorna o status_code 404 e a mensagem de erro avisando que tem