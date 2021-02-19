import requests
BASE_URI = 'http://localhost:8000/v1/address/'

#yogesh -- 2875404c355d3c6ca80ef79e0756b94793e5a836
#yogymax - b8b170aec7d30a8c6e8c34a6d370572450083405


def get_entities():
    response = requests.get(BASE_URI)
    print(response.status_code)
    print(response.json())

def add_entity(city,pin,st):
    adr_dict = {
        "city": city,
        "pincode": pin,
        "state": st
    }
    response = requests.post(BASE_URI,json=adr_dict)
    print(response.status_code)
    print(response.json())



def delete_entity(aid):
    response = requests.delete(BASE_URI+"{}/".format(aid))
    print(response.status_code)



if __name__ == '__main__':
    get_entities()
    #add_entity('Bglore',223344,'MH')
    #delete_entity(1)