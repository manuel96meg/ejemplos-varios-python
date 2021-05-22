#Hola flask
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def pelotudo():
    return 'Helloooooooooooooooooooooo'

@app.route('/welcome/<name>')
def welcome(name):
    return f'Bienvenidx {name}!'

@app.route("/login", methods=['POST','GET'])
def login():
    if request.method=='POST':
        user = request.form['nm']
        return redirect(url_for('welcome', name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('welcome', name = user))

#-------------------------------------------
#Esto ejecuta la app desde el codigo sin necesitar una terminal externa
if __name__ == '__main__':
    app.run(debug=True) #para actualizar cambios en el momento