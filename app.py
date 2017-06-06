from flask import Flask, jsonify
from config import DARK_SKY_KEY
import requests

app = Flask(__name__)

@app.route('/weather')
def index():
    r = requests.get('https://api.darksky.net/forecast/'+ DARK_SKY_KEY + '/41.6362,70.9342')
    print(r.json());
    return jsonify(results=r.json())

if __name__ == '__main__':
  app.run(debug=True)
