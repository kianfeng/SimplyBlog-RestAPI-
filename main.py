from fastapi import FastAPI, status, Response, HTTPException
import uvicorn

app = FastAPI()


@app.get("/")
async def main():
    return "hello world"


item_list = {"foo": "Hi foo"}


# path parameter
@app.get("/items/{item_id}", status_code=status.HTTP_200_OK)
async def get_item(item_id: str):
    if item_id not in item_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"item id: {item_id} not found")
    return item_list[item_id]


# Response Status Code
@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(item_id: str, item_body: str):
    if item_id in item_list:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"item id: {item_id} already exists")
    item_list[item_id] = item_body
    return item_list[item_id]

tasks = {"foo": "Hi foo"}


@app.put("/get-or-create-task/{task_id}", status_code=status.HTTP_200_OK)
async def get_or_create_task(task_id: str, response: Response):
    if task_id not in tasks:
        tasks[task_id] = "This didn't exist before"
        response.status_code = status.HTTP_201_CREATED
    return tasks[task_id]


@app.get("/get-task/{task_id}", status_code=status.HTTP_200_OK)
async def get_task(task_id: str, response: Response):
    if task_id not in tasks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"task id {task_id} not exist")
    return tasks[task_id]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)