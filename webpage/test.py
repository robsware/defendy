import os
from flask import Flask
app = Flask(__name__)

@app.route("/test.py")  # consider to use more elegant URL in your JS
def get_x():
    x = 2
    os.mkdir("yo")
    print ("yo")
    return x

if __name__ == "__main__":
    # here is starting of the development HTTP server
    app.run()

