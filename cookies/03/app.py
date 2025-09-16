from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route('/')
def index():
    cookie_name = 'page_visits'
    visits = 0
    if cookie_name in request.cookies:
        visits = int(request.cookies[cookie_name])
    visits += 1

    resp = make_response(render_template('cookie_01.html', cookie_value=visits))
    resp.set_cookie(cookie_name, str(visits))
    return resp

if __name__ == '__main__':
    app.run(debug=True)
