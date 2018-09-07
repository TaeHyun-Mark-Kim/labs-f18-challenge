from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/pokemon/<query>', methods=['GET'])
def printNameOrID(query):
	r = requests.get('http://pokeapi.co/api/v2/pokemon/' + query)
	json_object = r.json()

	if query.isdigit():
		pokemonName = json_object['forms'][0]['name']
		return render_template('showName.html', id = query, name = pokemonName)
	else:
		pokemonID = json_object['id']
		return render_template('showID.html', id = pokemonID, name = query)



if __name__ == '__main__':
    app.run()
