from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

PORT_NUM = 8000

@app.route('/')
def index():
  return redirect(url_for('welcome'))

@app.route('/level5/welcome')
def welcome():
  r = make_response(render_template('welcome.html'))
  # CSP 1.0
  r.headers.set('Content-Security-Policy', "connect-src 'self'")
  # CSP 2.0
  # r.headers.set('Content-Security-Policy', "form-action 'self'")
  return r

@app.route('/level5/signup')
def signup():
  r = make_response(render_template('signup.html'))
  # CSP 1.0
  r.headers.set('Content-Security-Policy', "connect-src 'self'")
  # CSP 2.0
  # r.headers.set('Content-Security-Policy', "form-action 'self'")
  return r

@app.route('/level5/confirm')
def confirm():
  r = make_response(render_template('confirm.html'))
  # CSP 1.0
  r.headers.set('Content-Security-Policy', "connect-src 'self'")
  # CSP 2.0
  # r.headers.set('Content-Security-Policy', "form-action 'self'")
  return r

if __name__ == '__main__':
  socketio.run(app, debug=True, port=PORT_NUM)