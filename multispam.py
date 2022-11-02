import requests, threading, random

spam_count = 0

class MultiSpam():
    random_question_api = "https://opentdb.com/api.php?amount=1&category=31&difficulty=easy&type=boolean"
    def __init__(self, url):
        self.url = url


    def random_question(self):
        r = requests.get(self.random_question_api)
        question = r.json()['results'][0]['question']
        return question


    def ngl_spam(self):
        global spam_count
        spam_count+=1

        f = open('uheaderz.txt','r').read().splitlines()
        x = ''.join(random.choices(f))
        header = {"User-Agent": x}
        data = {'question':self.random_question()}
        r = requests.post(self.url, headers=header, data=data)
        if(r.status_code == 429):
            print('retrying 429 response')
            while True:
                timeout = r.headers['Retry-after']
                r = requests.post(self.url, timeout=int(timeout),headers=header, data=data)
                if(r.status_code == 200):
                    print('429 is now 200 success!')
                    break

        print(f'({spam_count})->[{r.status_code}]')


if(__name__=="__main__"):
    url = input('Enter target ngl url: ')
    amnt = int(input('Spam amount: '))
    #amnt = 30
    for i in range(amnt):
        print(f'({i})->threads started!')
        threading.Thread(target=MultiSpam(url).ngl_spam).start()

