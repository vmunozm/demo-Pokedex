import requests
import json 
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
app = Flask(__name__)


@app.route("/")
def server_info():
    cors = CORS(app, resources={"/*": {"origins": "*"}})
    idpok = request.args.get("id")
    url = "https://pokeapi.co/api/v2/pokemon/"+idpok
    headers={}
    response=requests.request("GET",url,headers=headers)
    json_object=json.loads(str((response.text)))
    name = json_object["name"]
    img= json_object["sprites"]
    urlima=img.get("front_default")
    ot= img.get("other")
    dream=ot.get("dream_world")
    imagen=dream.get("front_default")
    print("el nombre es", name)
    print("la dirección de la imagen es", imagen)
    var2={"nombre_pokemon":name,"imagen":imagen}
    return(var2)

if __name__=="__main__":
    app.run()