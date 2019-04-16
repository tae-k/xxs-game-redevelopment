from flask import Flask, render_template_string, request, redirect, url_for, make_response
from flask_socketio import SocketIO

page_header = """
<!DOCTYPE html>
<html>
  <head>
    <!-- Internal game scripts/styles, mostly boring stuff -->
    <script type="text/javascript" src="/static/game-frame.js"></script>
    <link type="text/css" rel="stylesheet" href="/static/game-frame-styles.css" />
  </head>
 
  <body id="level1">
    <img src="/static/logos/level1.png">
      <div>
"""
page_footer = """
    </div>
  </body>
</html>
"""
main_page_markup = """
<form action="" method="GET">
  <input id="query" name="query" value="Enter query here..."
    onfocus="this.value=''">
  <input id="button" type="submit" value="Search">
</form>
"""


app = Flask(__name__)
socketio = SocketIO(app)

PORT_NUM = 8000

@app.route('/')
def index():
  return redirect(url_for('level1'))

@app.route('/level1')
def level1():

  if not request.args.get('query'):
    r = make_response(render_template_string(page_header + main_page_markup + page_footer))
    # CSP 1.0
    # r.headers.set('Content-Security-Policy', "script-src 'self'")
    # CSP 2.0
    r.headers.set('Content-Security-Policy', "form-action 'self'")

    # Show main search page
    return r
  else:
    query = request.args.get('query', '[empty]')
    query = escapeHtml(query)

    # Our search engine broke, we found no results :-(
    message = "Sorry, no results were found for <b>" + query + "</b>."
    message += " <a href='?'>Try again</a>."

    r = make_response(render_template_string(page_header + message + page_footer))
    # CSP 1.0
    r.headers.set('Content-Security-Policy', "script-src 'self'")
    # CSP 2.0
    # r.headers.set('Content-Security-Policy', "form-action 'self'")

    # Display the results page
    return r

def escapeHtml(s):
  htmlDict = {
    '<': '&lt;',
    '>': '&gt;',
    '&': '&amp;',
    "'": '&#39;',
    '"': '&quot;',
    '`': '&#x60;',
    '/': '&#x2F;',
    '=': '&#x3D;'
  }
  for key in htmlDict:
    s = s.replace(key, htmlDict[key])
  return s

if __name__ == '__main__':
  socketio.run(app, debug=True, port=PORT_NUM) 