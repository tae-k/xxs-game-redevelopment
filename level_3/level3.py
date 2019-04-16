from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

PORT_NUM = 8000

@app.route('/')
def index():
  return redirect(url_for('level3'))

@app.route('/level3')
def level3():
  r = make_response(render_template('index.html'))
  # CSP 1.0
  r.headers.set('Content-Security-Policy', "connect-src 'self'")
  # CSP 2.0
  # r.headers.set('Content-Security-Policy', "form-action 'self'")

  return r

if __name__ == '__main__':
    socketio.run(app, debug=True, port=PORT_NUM)