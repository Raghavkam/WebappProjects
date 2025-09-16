
from flask import Flask, request, make_response, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    # READ THE COOKIE (may or may not be present)
    string_cookie = request.cookies.get('user_logged_in')

    # VALIDATE THE COOKIE
    if string_cookie == "True":
        logged_in = True
    else:
        logged_in = False

    # PREPARE PAGE
    if logged_in:
        resp = make_response(render_template('logged_in_true.html'))
    else:
        resp = make_response(render_template('logged_in_false.html'))

    # SET COOKIE
    resp.set_cookie('user_logged_in', str(logged_in))

    return resp


@app.route('/login')
def login_processor():
    resp = make_response(redirect(url_for('home')))
    resp.set_cookie('user_logged_in', 'True')
    return resp

@app.route('/logout')
def logout_processor():
    resp = make_response(redirect(url_for('home')))
    resp.set_cookie('user_logged_in', 'False')
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)



