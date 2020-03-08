from vmcjp.utils import dbutils
from vmcjp.utils import constant

def event_handler(event):
    text = event.get("text").lower()
    
