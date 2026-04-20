import pickle
import sys
sys.path.append(r"C:\Users\yazan\AppData\Local\Programs\Python\Python311\Lib\site-packages")

with open('ml_model.pkl', 'rb') as file:
    classifier = pickle.load(file)

from flask import Flask, render_template, request, redirect  # , jsonify
import numpy as np

app = Flask(__name__)

# @app.errorhandler(404)
# def not_found(e):
#     return render_template("404.html")

@app.route('/')
def home():
    return render_template('Predictor.html')  # home_active='active'


@app.route('/Type', methods=['POST'])
def predict():
        age = int(request.form['1'])
        insuline = int(request.form['2'])
        pcos = int(request.form['3'])
        obesity = int(request.form['4'])
        smoke = int(request.form['5'])
        breathing = int(request.form['6'])
        an = int(request.form['7'])
        coma = int(request.form['8'])
        Confusion = int(request.form['9'])
        Mumps = int(request.form['10'])
        prediction = classifier.predict([[age, insuline, pcos, obesity, smoke, breathing, an, coma, Confusion, Mumps]])
        output = round(prediction[0])
        resultHtml = ''

        if output == 0:
            resultHtml += ' Type 1\nBe healthy\ndo some workout train, Running, walking, Go to GYM...'
        elif output == 1:
            resultHtml += ' Type 2\nEat Healthy Food, be Careful about yourself....'

        return render_template('Predictor.html', diabetic_type=resultHtml)
    #     if result[0] == 0:
    #         diabetic_type = 'Type 1'
    #     elif result[0] == 1 :
    #         diabetic_type = 'Type 2'
    #
    #     return render_template('Type.html', diabetic_type=diabetic_type)
    #
    # else :
    #     return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)


# from waitress import serve
#
# if __name__ == "__main__":
#     serve(app, host="0.0.0.0", port=5000, threads=4)