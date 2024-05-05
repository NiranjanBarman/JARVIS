Fileopen = open("data\\api.txt","r")
API = Fileopen.read()
Fileopen.close()

import openai
from dotenv import load_dotenv

openai.api_key = API
load_dotenv()
completion = openai.Completion()

def replybrain(question,chat_log = None ):
    Filelog = open("database\\chat_log.txt","r")
    chat_log_template = Filelog.read()
    Filelog.close()

    if chat_log is None: 
        chat_log = chat_log_template

    prompt = f'{chat_log}You : {question}\nJarvis :'
    response = completion.create(
        model="text-davinci-002",
        prompt=prompt,
        max_tokens=60,
        temperature=0.5,
        top_p=0.3, 
        frequency_penalty=0.5, 
        presence_penalty=0)
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template+ f"\nYou : {question}\nJarvis : {answer}"
    Filelog = open("database\\chat_log.txt","w")
    Filelog.write(chat_log_template_update)
    Filelog.close()
    return answer
