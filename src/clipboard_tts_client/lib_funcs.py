#!/usr/bin/python3

from langdetect import detect
import requests

CONFIG_DEFAULT={
"host":"localhost",
"port":5000
}
################################################################################

def tts_remove_task(ID):
    if isinstance(ID,str) and ID!='':
        SERVER_URL = 'http://'+CONFIG_DEFAULT["host"]+':'+str(CONFIG_DEFAULT["port"]);
        print('Sending DELETE request of id:',ID)
        msg=remove_task(SERVER_URL,ID);
        return msg
    return ''

def remove_task(server_url,task_id):
    # Send DELETE request to server
    response = requests.delete(f'{server_url}/remove_task/{task_id}')

    if response.status_code == 200:
        print(response.json()["message"])
        return response.json()["message"]
    else:
        print("Error removing task:",task_id)
        return None


################################################################################
def tts_play(text):
    # Retorna uma string com base no texto passado
    if text.strip()=="":
        return "";
    
    SERVER_URL = 'http://'+CONFIG_DEFAULT["host"]+':'+str(CONFIG_DEFAULT["port"]);
    
    text=text.replace("\n", " ")
    
    DATA={
        "text": text, 
        "language": detectar_linguagem(text),
        "split_pattern": [". ","; ","\n\n","\n\r\n"], 
        "speed":1.25 
    }
        
    ret_str=send_json_from_dict(SERVER_URL,DATA);
    
    return ret_str;

def detectar_linguagem(texto):
    try:
        linguagem = detect(texto)
        return linguagem
    except Exception as e:
        return "en";


def send_json_from_dict(server_url,data):
    # Enviar solicitação POST ao servidor
    response = requests.post(f'{server_url}/add_task', json=data)

    if response.status_code == 200:
        print(f"Task sent successfully! ID: {response.json()['id']}")
        return response.json()['id'];
    else:
        print("Error submitting task.")
        return None
