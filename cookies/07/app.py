from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Define a global variable to keep track of the count
count = 0

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/fetch_route')
def fetcher():
    global count
    count += 1
    print('The fetcher is fetching!')
    foo = {
        'count': count,
        'meal_choice': 'vegetarian'
    }
    return jsonify(foo)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
