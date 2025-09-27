from flask import Flask
app = Flask('')
from threading import Thread
def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()