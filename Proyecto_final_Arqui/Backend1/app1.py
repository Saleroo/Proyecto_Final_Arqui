
import requests
import os
from flask import Flask
# or configure to use ELASTIC_APM in your application's settings
from elasticapm.contrib.flask import ElasticAPM

app = Flask(__name__)
app.config['ELASTIC_APM'] = {
# Set the required service name. Allowed characters:
# a-z, A-Z, 0-9, -, _, and space
'SERVICE_NAME': 'App1',

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
def Dolar():
    env = os.environ.get('other_pod')
    env = str(env)
    r= requests.get(env)

    data = r.text
    print(data)
    return data

app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 4444)),debug=True)






