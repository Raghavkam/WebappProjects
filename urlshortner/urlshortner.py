from flask import Flask, render_template, request, redirect

import random

app = Flask(__name__)


urls_dict = {}


@app.route('/',  methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        short_id = ''.join(random.choices('0123456789ABCDEF', k=6))
        urls_dict[short_id] = request.form.get('url')
        return redirect(f'/short/{short_id}')
    return render_template('form.html')


@app.route('/short/')
def create(short_id):
    if urls_dict.get(short_id):
        return render_template('urltemplate.html', short_url=request.host_url + short_id)
    return 'URL not found', 404


@app.route('/<short_id>')
def redirect_to_original(short_id):
    if urls_dict.get(short_id):
        return redirect(urls_dict.get(short_id))
    return 'URL not found', 404

if __name__ == '__main__':
    app.run(debug=True)