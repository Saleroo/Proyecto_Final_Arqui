
import requests
import os
from flask import Flask


app = Flask(__name__)


@app.route('/')
def Dolar():
    env = os.environ.get('other_pod')
    env = str(env)
    r= requests.get(env)

    data = r.text
    print(data)
    return data

app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 4444)),debug=True)






