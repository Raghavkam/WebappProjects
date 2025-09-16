from flask import Flask, jsonify, render_template, request
app = Flask(__name__)


pokemon_choices = ['Geodude','Bidoof','Grubbin','Stunfish','Lickilicky','Throh','Scyther','Raichu','Mankey','Koffing','Cryogonal','Ekans']
shundos_added_list = []

@app.route('/')
def home():
  return render_template('home.html', pokes=pokemon_choices)

@app.route('/add_shundo', methods=['POST'])
def add_shundo():

	pokemon_type = request.form.get('pokemon_type')
	pokemon_cp = request.form.get('pokemon_cp')
	print(pokemon_type)
	print(pokemon_cp)

	if (pokemon_cp == '') : 
		# IF EMPTY CP WAS SUBMITTED, IT'S NOT OK
		return jsonify( {'ok_status': False})
	else :
		# ELSE, APPEND TO LIST
		shundos_added_list.append(
			{
				'pokemon' : pokemon_type,
				'cp' : pokemon_cp
			}
		)
		return jsonify( {'ok_status': True})



@app.route('/get_all')
def get_all():

  foo = {
    'shundos' : shundos_added_list
  }
  return jsonify(foo)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)