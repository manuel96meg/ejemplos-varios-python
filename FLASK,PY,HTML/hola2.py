from flask import Flask,render_template

app = Flask(__name__)

@app.route('/htmlfont')
def index():
    HtmlStr="""
<html>
<body>
    <h1> Hello World!!! </h1>
</body>
</html>
"""
    return HtmlStr


"""
#Para abrir un archivo html(o template) hay que importar 'render_template'
#Dicho archivo debe estar en una carpeta en el directorio del .py llamada 'templates'
@app.route('/pagina')
def page():
    return render_template('hola.html')
"""
@app.route('/')
def principal():
    return render_template("holaJS.html")

#-------------------------------------------
#Esto ejecuta la app desde el codigo sin necesitar una terminal externa
if __name__ == '__main__':
    app.run(debug=True) #para actualizar cambios en el momento