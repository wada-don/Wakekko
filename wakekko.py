import random
import sys

argv = sys.argv

class CountryModel:
    def __init__(self):
        self.countries = [('アルゼンチン',17),('インドネシア',17),('イタリア',5),('オーストラリア',4),('ニッポン',3),('チュウゴク',3),('ドイツ',2),('モンゴル',2),('エジプト',2),('カナダ',2),('ギリシャ',2),('ブラジル',2),('アメリカ',1),('イギリス',1),('カンコク',1)]

    def get_prob_sum(self):
        prob_sum = 0
        for c in self.countries:
            prob_sum += c[1]
        return prob_sum

    def get_country(self):
        rand = random.randint(0,self.get_prob_sum()-1)
        count = 0
        prob = self.countries[0][1]
        while True:
            prob = self.countries[count][1]
            rand -= prob
            if rand<=0:
                break
            count+=1
        return self.countries[count][0]

class TextModel:
    def chop_text(self,text):
        length = len(text)
        rand = random.randint(1,length-1)
        return text[0:rand]

    def check(self,question,answer,countries):
        answer = question+answer
        for c in countries:
            if c[0] == answer:
                print('ええやん！')
                return

        print('全然あかんやん！')
        return

def main():
    countryModel = CountryModel()
    textModel = TextModel()
    country = countryModel.get_country()
    question = textModel.chop_text(country)
    print(question)
    answer = input('>>>  ')
    textModel.check(question,answer,countryModel.countries)

if __name__ == '__main__':
    main()