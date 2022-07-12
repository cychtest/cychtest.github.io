from flask import Flask, render_template,request
app = Flask(__name__)

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/patientlist")
def patientlist():
    return render_template('patientlist.html')

@app.route("/patientprofile")
def patientprofile():
    return render_template('patientprofile.html')

@app.route("/NF")
def NF():
    return render_template('NF.html')

@app.route("/sepsis")
def sepsis():
    return render_template('sepsis.html')

if __name__ == '__main__':
    app.run(port=5000,debug = True)