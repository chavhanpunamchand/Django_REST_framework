import requests

BASE_URI = 'http://localhost:8000/v2/emp/'

token_val = 'Token b8b170aec7d30a8c6e8c34a6d370572950083405'
final_token_dict = {'Authorization':token_val}

def get_entities():
    response = requests.get(BASE_URI)
    print(response.status_code)
    print(response.json())


def add_entity(name, age, role):
    emp_dict = {
          "name": name,
          "age": age,
          "role": role
        }
    response = requests.post(BASE_URI, json=emp_dict,headers=final_token_dict)
    print(response.status_code)
    print(response.json())


def delete_entity(aid):
    response = requests.delete(BASE_URI + "{}/".format(aid))
    print(response.status_code)


if __name__ == '__main__':
    #get_entities()
    add_entity('Mrs. VV',22,'SE')
    #delete_entity(2)