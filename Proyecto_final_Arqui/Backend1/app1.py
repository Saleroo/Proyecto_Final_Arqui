from flask import Flask






app= Flask(__name__)

@app.route('/dolar')    
def getDolar():
    print("¿Backend2 me podrias decir cual es el valor del dolar actual?")
    print("\n")
    #ObtenerDolar()
    return "<p> Succes </p>"

app.run(host='0.0.0.0',port=8080,debug=True)

