from flask import Flask, request, jsonify, abort
from math import sqrt, pow

app = Flask(__name__)

@app.route('/hipotenusa', methods=['GET'])
def calcular_hipotenusa():
    try:
        cateto1 = float(request.args.get('cateto1'))
        cateto2 = float(request.args.get('cateto2'))
        hipotenusa = sqrt(pow(cateto1,2) + pow(cateto2, 2))
        resultado = {"resultado": hipotenusa}
        return jsonify(resultado)  
    except:
        return jsonify({"erro":"dados inseridos invalido"})


if __name__ == "__main__":
    app.run(port=5000, host='localhost', debug=True)


'''
# Parâmetros
    -Path:
    /hipotenusa

    -Query:
    cateto1
    cateto2
'''