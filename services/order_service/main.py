
from fastapi import FastAPI

app = FastAPI(
    title="NEXUS Order Service",
    description="Order management microservice",
    version="1.0.0"
)

orders = [
    {"order_id": 101, "user_id": 1, "product": "Laptop", "amount": 55000},
    {"order_id": 102, "user_id": 2, "product": "Headphones", "amount": 2500}
]


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "order-service"
    }


@app.get("/orders")
def get_orders():
    return {"orders": orders}


@app.get("/orders/{order_id}")
def get_order(order_id: int):
    for order in orders:
        if order["order_id"] == order_id:
            return order

    return {"error": "Order not found"}
