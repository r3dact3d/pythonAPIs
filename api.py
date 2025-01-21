# written by brady [r3dact3d]
import requests


        
headers = {
'Authorization': f'Bearer <token>',
'Accept': 'application/json'
}

data = {
    "model": "tinyllama:latest",
    "messages": [{"role": "user", "content": question}],
    "stream": False
}
        
url = "https://0ri0n.blinker19.com/api/chat/completions"
response = requests.post(url,json=data,headers=headers)
response_json = json.loads(response.text)
    ai_reply = response_json['choices'][0]['message']['content']
    print(ai_reply)
    question_number += 1
