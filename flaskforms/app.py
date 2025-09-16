from flask import Flask, render_template, request

app = Flask(__name__)

# Prices for different meal types
prices = {
    'breakfast': 10,
    'lunch': 15,
    'dinner': 20
}

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/result', methods=['GET'])
def result():
    meal_type = request.args.get('meal_type')
    quantity = int(request.args.get('quantity', 1))
    senior_discount = 'senior_discount' in request.args

    base_price = prices[meal_type] * quantity


    if senior_discount:
        discount = base_price * 0.1 
        base_price -= discount

    return render_template('result.html', total_price=base_price)

if __name__ == '__main__':
    app.run(debug=True)