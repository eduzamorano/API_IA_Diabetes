# Dependencias
from flask import Flask, request, jsonify
import joblib
import traceback
import pandas as pd
import numpy as np

# Definición de API
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if lr:
        try:
            json_ = request.json
            print(json_)
            json_scaler = sc.transform(json_)
            print(json_scaler)
            query = pd.get_dummies(pd.DataFrame(json_scaler))
           # query = query.reindex(columns=model_columns, fill_value=0)

            prediction = list(lr.predict(query))
            print(prediction)
            if (prediction == [0]):
                text = "Sin Diabetes"
            else:
                text = "Con Diabetes"

            return jsonify({'prediction': text})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Entrene modelo antes')
        return ('No existe modelo')

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 12345 # If you don't provide any port the port will be set to 12345

    lr = joblib.load("model/model_log_regv3.pkl") # Load "model.pkl"
    sc = joblib.load("model/scalerv3.pkl") # Load "scaler.pkl"
    print ('Modelo Cargado')
   # model_columns = joblib.load("model_columns.pkl") # Load "model_columns.pkl"
    #print ('Model columns loaded')

    app.run(port=port, debug=True)