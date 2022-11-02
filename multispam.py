import requests, threading

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
        data = {'question':self.random_question()}
        r = requests.post(self.url, data=data)
        spam_count+=1
        print(f'({spam_count})->[{r.status_code}]')


if(__name__=="__main__"):
    url = input('Enter target ngl url: ')
    amnt = int(input('Spam amount: '))
    spam = MultiSpam(url)
    for i in range(amnt):
        print(f'({i})->threads started!')
        threading.Thread(target=spam.ngl_spam).start()


