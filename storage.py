from typing import List
from models import Notifications

recieved_notifications : List[Notifications] = []

forwarded_notifications : List[Notifications] = []

def add_recieved(notification: Notifications) -> None:
    recieved_notifications.append(notification)

def add_forwarded(notification: Notifications) -> None:
    forwarded_notifications.append(notification)


def get_all() -> dict:
    return {
        "recieved": recieved_notifications,
        "forwarded": forwarded_notifications
    }

def clear_storage() -> None:
    recieved_notifications.clear()
    forwarded_notifications.clear()