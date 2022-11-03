import requests, threading, random

spam_count = 0

class MultiSpam():
    random_question_api = "https://opentdb.com/api.php?amount=1&category=31&difficulty=easy&type=boolean"
    def __init__(self, namze):
        self.namze = namze


    def random_question(self):
        r = requests.get(self.random_question_api)
        question = r.json()['results'][0]['question']
        return question

    def secret_me_spam(self):
        url = 'https://storyzink.com/message_h.php'
        global spam_count
        spam_count+=1

        f = open('uheaderz.txt','r').read().splitlines()
        x = ''.join(random.choices(f))
        header = {"User-Agent": x}
        data = {'name':self.namze,'ans1':self.random_question()}

        r = requests.post(url, headers=header,data=data)
        print(f'({spam_count})->[{r.status_code}]')


    def ngl_spam(self):
        global spam_count
        spam_count+=1

        f = open('uheaderz.txt','r').read().splitlines()
        x = ''.join(random.choices(f))
        header = {"User-Agent": x}
        data = {'question':self.random_question()}
        url = 'https://ngl.link/'
        r = requests.post(url+self.namze, headers=header, data=data)
        if(r.status_code == 429):
            print('retrying 429 response')
            while True:
                timeout = r.headers['Retry-after']
                r = requests.post(url+self.namze, timeout=int(timeout),headers=header, data=data)
                if(r.status_code == 200):
                    print('429 is now 200 success!')
                    break

        print(f'({spam_count})->[{r.status_code}]')


if(__name__=="__main__"):
    name = input('Enter target name: ')
    amnt = int(input('Spam amount: '))
    que = input('(s)ecretm|(n)gl link: ')
    #amnt = 30
    for i in range(amnt):
        print(f'({i})->threads started!')
        if(que == 's'):
            threading.Thread(target=MultiSpam(name).secret_me_spam).start()
        elif(que == 'n'):
            threading.Thread(target=MultiSpam(name).ngl_spam).start()
        else:
            print('ERROR!')
            break

