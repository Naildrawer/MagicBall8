import random as r
answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай", "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет", "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет", "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Как вас зовут?')
k = input()
print('Привет', k,)
def game():
  while True:
    q = input('Какой у тебя вопрос? ')
    print(r.choice(answers))
    answ = input('Желаете задать еще вопрос?(Y/N)')
    if answ == "Y":
      continue
    else:
      print("Всего доброго!")
      break
game()      
      
