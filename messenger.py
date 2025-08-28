from models import Notifications
from storage import add_forwarded

def forward(notification: Notifications) -> None:
    add_forwarded(notification)