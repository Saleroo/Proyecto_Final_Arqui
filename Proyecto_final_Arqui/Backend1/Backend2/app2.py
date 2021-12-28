import http.client
from flask import Flask
# or configure to use ELASTIC_APM in your application's settings
from elasticapm.contrib.flask import ElasticAPM

app = Flask(__name__)
app.config['ELASTIC_APM'] = {
# Set the required service name. Allowed characters:
# a-z, A-Z, 0-9, -, _, and space
'SERVICE_NAME': 'App2',

# Use if APM Server requires a secret token
'SECRET_TOKEN': 'IRY8JxQCLhC9BYyh0G',

# Set the custom APM Server URL (default: http://localhost:8200)
'SERVER_URL': 'https://7293afe83bfb4660bd8419d7428e13b4.apm.eu-west-1.aws.cloud.es.io:443',

# Set the service environment
'ENVIRONMENT': 'production',

'DEBUG': True
}

apm = ElasticAPM(app)

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