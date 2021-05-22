from flask import Flask,render_template,request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('cokiSetCookie.html')

@app.route('/setcookie', methods = ['POST','GET'])
#en Flask, las cookies se setean en un objeto response
#cookies: dictionary object of all cookie variables and corresponding values that client has transmitted
#they also store its expiry time, path and domain name of site
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        #make_response : get response object from return value of a view function
        respuesta = make_response(render_template('cokiReadCookie.html'))
        #set_cookie : stores a cookie
        respuesta.set_cookie('userID', user)
        return respuesta

@app.route
def getCookie():
    name = request.cookies.get('userID')
    return  '<h1> Welcome ' + name +'<h1>'


if __name__ == '__main__':
    app.run(debug=True) #para actualizar cambios en el momento