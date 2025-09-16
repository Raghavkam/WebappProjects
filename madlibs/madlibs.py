from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_form():
  return render_template('home.html')

@app.route('/gamestart')
def startgame():
    return render_template('input.html')

@app.route('/inputted',methods = ["POST"])
def finalScreen():
    if request.method == 'POST':

      thing= request.form.get('firstInp')
      name = request.form.get('secondInp')
      animal = request.form.get('thirdInp')
      date = request.form.get('fourthInp') 
      adjective = request.form.get('fifthInp') 


      return render_template("post.html",Thing = thing,Name = name, Animal = animal, Date = date, Adjective = adjective)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80)
