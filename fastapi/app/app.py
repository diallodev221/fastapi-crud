from fastapi import FastAPI

app = FastAPI()

# Get request for testing
@app.get("/", tags=["ROOT"])
async def root() -> dict:
  return {"Hello": "world"}


# Get --> Read todo
@app.get("/todos", tags=["todos"])
async def get_todos() -> dict:
  return {"data": todos}


# Post --> Create todo
@app.post("/todos", tags=["todos"])
async def add_todo(todo: dict):
  todos.append(todo)
  return {
    "data": "Todo has been added"
  }

# Put --> Edit todo
@app.put("/todos/{todo_id}", tags=["todos"])
async def update_todo(id: int, body: dict) -> dict:
  for todo in todos:
    if todo['id'] == id:
      todo['activity'] = body['activity']
      return {
        "data": f"Todo with id {id} has been updated"
      }
  return {
        "data": f"Todo with this id {id} was not found"
      }
  


# Delete --> Delete todo
@app.delete("/todos/{todo_id}", tags=["todos"])
async def update_todo(id: int) -> dict:
  for todo in todos:
    if todo['id'] == id:
      todos.remove(todo)
      return {
        "data": f"Todo withid {id} has been deleted"
      }
  return {
        "data": f"Todo with this id {id} was not found"
      }





todos = [
  {
    "id": 1,
    "activity":"Jogging for 3 hours at 5:00 PM"
  },
  {
    "id": 2,
    "activity":"Coding for 1 hours"
  }
]