from flask import Flask, render_template, redirect, request, url_for, render_template_string

app = Flask(__name__)

import pickle

model = pickle.load(open('Liver_Disease_Model.pkl' , 'rb'))

@app.route('/')
def home():
    return render_template("prediction.html")

@app.route('/login' , methods=['POST','GET'])
def login():
    
    a = request.form['Age']
    b = request.form["Gender"]
    c = request.form["Total_Bilirubin"]
    d = request.form["Direct_Bilirubin"]
    e = request.form["Alkaline_Phosphotase"]
    f = request.form["Alamine_Aminotransferas"]
    g = request.form["Aspartate_Aminotransferas"]
    h = request.form["Total_Proteins"]
    i = request.form["Albumin"]
    j = request.form["Albumin_and_Globulin_Ratio"]
    
    t = [[int(a),int(b),int(c),int(d),int(e),int(f),int(g),int(h),int(i),int(j)]]
    output = model.predict(t)
    #return str(output[0])
    
    return render_template('result.html', y =str(output[0]))

@app.route('/admin')
def admin():
    return "Hello admin"


if __name__ =='__main__':
    app.run(debug = True)
