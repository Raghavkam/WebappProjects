from flask import Flask, request, make_response, render_template
app = Flask(__name__)

@app.route('/')
def cookie_processor():

  # READ THE COOKIE (may or may not be present)
  string_cookie = request.cookies.get('number_count')

  print(string_cookie)

  # VALIDATE THAT THE COOKIE IS AN INTEGER 
  try:
    numeric_cookie = int(string_cookie)
  except:
    numeric_cookie = 0


  # GENERATE TEMPLATE
  resp = make_response( 
    render_template('display_number.html', cookie_value=numeric_cookie )
  )

  # COOKIE VALUE IS EXPECTED TO BE A STRING
  resp.set_cookie('number_count', str(numeric_cookie))

  return resp

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)