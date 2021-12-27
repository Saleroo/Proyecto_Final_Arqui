import http.client
from flask import Flask


app= Flask(__name__)


@app.route('/')
def ObtenerDolar():
    conn = http.client.HTTPSConnection("mindicador.cl")
    payload = ''
    headers = {}
    conn.request("GET", "/api/dolar", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

    return data.decode("utf-8")

app.run(host='0.0.0.0',port=8080,debug=True)