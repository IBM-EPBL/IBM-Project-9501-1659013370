import numpy as np
import flask
from flask import Flask, request, jsonify, render_template
import pickle
import script 

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def predict1():
    return render_template('index.html')


@app.route('/predict')
def predict():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    url = request.form['URL']
    checkprediction = script.main(url)
    prediction = model.predict(checkprediction)
    print(prediction)
    output=prediction[0]
    if(output==1):
        pred="Your are safe!!  This is a Legitimate Website."
        
    else:
        pred="You are on the wrong site. Be cautious!"
    return render_template('index.html', prediction_text='{}'.format(pred),url=url)

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.y_predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)
if __name__=='__main__':
    app.run(debug=False)