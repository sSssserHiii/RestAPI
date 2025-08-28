from fastapi import FastAPI
from models import Notifications
from storage import add_recieved, get_all
from messenger import forward


app = FastAPI(title="NotificationApi", version="1.0")

@app.post("/notifications")
def recive_notification(notification: Notifications):
    
    add_recieved(notification)

    if notification.Type.lower() == "warning":
        forward(notification)
        return {"status": "forwarded", "notification" : notification}
    if notification.Type.lower() == "info":
        return {"status": "ignored", "notification" : notification}
    
    return {"status" : "received", "notification" : notification}
    
@app.get("/notifications")
def list_notifications():
    return get_all()

