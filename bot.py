EMAIL = "email"
PASSWORD = "password"

from fbchat import Client
from fbchat.models import *
import time
import sys

def get_message():
    return "MESSAGE"

while 1:
    client = Client(EMAIL, PASSWORD)
    if not client.isLoggedIn():
        sys.exit()

    users = client.searchForUsers("Firstname Lastname")
    user_id = users[0].uid
    message = get_message()

    client.send(Message(text=message), thread_id=user_id, thread_type=ThreadType.USER)
    client.logout()

    # sleep for a day
    time.sleep(86400) 
