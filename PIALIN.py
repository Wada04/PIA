
import requests, json, time

if __name__ == "__main__":
    url = "https://pokeapi.co/api/v2/pokemon-form/1"
    r = requests.get(url)
    if r.status_code == 200:
        datos = json.loads(r.text)
        #print(datos)
        pokemon= datos.get("pokemon",[])
        for x,y in pokemon.items():
            if "http" in y and x=="url":
                r2=requests.get(y)
                infoextra = json.loads(r2.text)
                for x,y in infoextra.items():
                    if x=="abilities":
                        for habilidad in y:
                            print(type(habilidad))
                            #print(habilidad[0])
                #print(infoextra,type(infoextra))
            if x!="created" and x !="edited" and x!="url":
                print(x+":",y) 
