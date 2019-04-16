from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

PORT_NUM = 8000

@app.route('/')
def index():
  return redirect(url_for('level6'))

@app.route('/level6')
def level6():
  r = make_response(render_template('index.html'))
  # CSP 1.0
  # r.headers.set('Content-Security-Policy', "connect-src 'self'")
  # CSP 2.0
  r.headers.set('Content-Security-Policy', "frame-ancestors 'self'")
  return r

if __name__ == '__main__':
    socketio.run(app, debug=True, port=PORT_NUM)