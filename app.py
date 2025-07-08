from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import users, tasks, categories
app = FastAPI(title="Task App API", 
              version="1.0.1",
              redoc_url='/',
                description="Task App API is a restful API used for task management. With All the CRUD operations on tasks using SQLITE database",               
               )

app.add_middleware(CORSMiddleware,allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'],)

app.include_router(users.router)
app.include_router(tasks.router)
app.include_router(categories.router)


     


