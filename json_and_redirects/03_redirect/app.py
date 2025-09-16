from flask import Flask, render_template, request, redirect, url_for
import logging
app = Flask(__name__)

# Suppress INFO level messages from Flask
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


# REDIRECT TO AN EXTERNAL SITE
@app.route('/redirect_ext')
def redirect_route():
  print('you are being redirected')
  return redirect("https://ion.tjhsst.edu")

# REDIRECT TO AN INTERNAL ROUTE
@app.route('/redirect_int')
def internal_redirection():
  print('you are being redirected')
  return  redirect(url_for('hello_route'))


@app.route('/hello')
def hello_route() :
	return "hello"

app.debug = True
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)