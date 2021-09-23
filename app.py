# importing the necessary dependencies
import pickle

from flask import Flask, render_template, request
from flask_cors import cross_origin
import flasgger

app = Flask(__name__)  # initializing a flask app


@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])  # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            CRIM = float(request.form['CRIM'])
            ZN = float(request.form['ZN'])
            CHAS = float(request.form['CHAS'])
            NOX = float(request.form['NOX'])
            RM = float(request.form['RM'])
            AGE = float(request.form['RM'])
            DIS = float(request.form['DIS'])
            RAD = float(request.form['RAD'])
            B = float(request.form['B'])
            LSTAT = float(request.form['LSTAT'])
            PTRATIO = float(request.form['PTRATIO'])

            filename = 'model.pkl'
            loaded_model = pickle.load(open(filename, 'rb'))  # loading the model file from the storage
            # predictions using the loaded model file
            prediction = loaded_model.predict([CRIM,ZN,CHAS,NOX,RM,AGE,DIS,RAD,B,LSTAT,PTRATIO])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html', prediction=prediction)
        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')


if __name__ == "__main__":
    # app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(debug=True)  # running the app
