from flask import Flask, render_template, request, redirect
import logging
import random

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

urls_dict = {}

@app.route('/', methods=['GET', 'POST'])
def submit_url():
    if request.method == 'POST':
        original_url = request.form.get('url')
        short_id = ''.join(random.choices('0123456789ABCDEF', k=6))
        urls_dict[short_id] = original_url
        return redirect(f'/display/{short_id}')
    return render_template('submit_url.html')

@app.route('/display/<short_id>')
def display_url(short_id):
    original_url = urls_dict.get(short_id)
    if original_url:
        return render_template('display_url.html', short_url=request.host_url + short_id)
    return 'URL not found', 404

@app.route('/<short_id>')
def redirect_to_original(short_id):
    original_url = urls_dict.get(short_id)
    if original_url:
        return redirect(original_url)
    return 'URL not found', 404

if __name__ == '__main__':
    app.run(debug=True)
