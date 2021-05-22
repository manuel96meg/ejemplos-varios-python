from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def notas():
    return render_template('requestStudents.html')

@app.route('/result', methods = ['POST','GET'])
def result():
    if request.method == 'POST':
        #el form (que proviene del requestStudents.html) se guarda en esta variable para luego enviarse a requestResultado.html
        resultPy = request.form
        #result es una variable de diccionaro
        return render_template('requestResult.html', result = resultPy)


if __name__ == '__main__':
    app.run(debug=True) #para actualizar cambios en el momento