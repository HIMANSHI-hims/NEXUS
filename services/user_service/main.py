
from fastapi import FastAPI

app = FastAPI(
    title="NEXUS User Service",
    description="User management microservice",
    version="1.0.0"
)

users = [
    {"id": 1, "name": "Himanshi"},
    {"id": 2, "name": "Alex"}
]


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "user-service"}


@app.get("/users")
def get_users():
    return {"users": users}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user

    return {"error": "User not found"}
