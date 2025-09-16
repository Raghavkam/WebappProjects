from flask import Flask, render_template, request
import logging
app = Flask(__name__)

# Suppress INFO level messages from Flask
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


# PARAMETRIC (DYNAMIC) ROUTE
@app.route('/<value>')
def parametric_route(value):
  print(value)
  return 'dummy string'	


app.debug = True
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)