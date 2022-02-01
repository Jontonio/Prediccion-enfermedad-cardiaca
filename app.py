
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from methods import prediction

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apiPrediction', methods=['POST'])
def apiPrediction():
    
    tipo = request.form['tipo_algoritmo']
    
    data = [[
        request.form['Edad'],
        request.form['Sexo'],
        request.form['Tipo_DolorP'],
        request.form['PA_Reposo'],
        request.form['Colesterol'],
        request.form['Glucemia_Ayunas'],
        request.form['ECG_Reposo'],
        request.form['FC_MaxHR'],
        request.form['Angina_Ejercicio'],
        request.form['ST_Oldpeak'],
        request.form['IntensidadP_Frecuencia']
    ]]
    
    return  render_template('prediction.html', result = prediction(tipo, data) )

if __name__ == '__main__':
    app.run(debug=True)