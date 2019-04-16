from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

PORT_NUM = 8000

@app.route('/')
def index():
  return redirect(url_for('level4'))

@app.route('/level4')
def level4():

  if not request.args.get('timer'):
    r = make_response(render_template('index.html'))
    
    # CSP 1.0
    r.headers.set('Content-Security-Policy', "connect-src 'self'")
    # CSP 2.0
    # r.headers.set('Content-Security-Policy', "form-action 'self'")
    
    # Show main timer page
    return r
  
  else:
    t = request.args.get('timer', 0)
    # make sure t is a positive number
    if is_number(t) == False:
      t = "0"
    else:
      if float(t) <= 0:
        t = "0"

    r = make_response(render_template('timer.html', timer=t))

    # CSP 1.0
    r.headers.set('Content-Security-Policy', "connect-src 'self'")
    # CSP 2.0
    # r.headers.set('Content-Security-Policy', "form-action 'self'")
    
    # Show results page
    return r

def is_number(s):
  try:
      float(s)
      return True
  except ValueError:
      return False

if __name__ == '__main__':
  socketio.run(app, debug=True, port=PORT_NUM) 