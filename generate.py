import pickle
from numpy import random
#ставим библиотеки

def load_model(model_dir):
    with open('models/' + model_dir + '.pickle', 'rb') as f:
        find_word = pickle.load(f)
    return find_word
#открываем наш текст

def generate(prefix='', length=10, n_word=None, ran_seed=23):
    random.seed(ran_seed) # считывем сид
    seed = len(list(n_word.keys())[0])# определяем длину н-грамм
    text_ans = []

    if prefix == '':
        for i in list(n_word.keys())[int(random.choice(len(list(n_word.keys()))))]:
            text_ans.append(i)#если пользователь не ввел начальные слова то выбираем их случайно исходя из сида
     #иначе разделяем введенные слова пробелом
    else:
        for w in prefix.split():
            text_ans.append(w.lower())
    for i in range(length):
        try:
            # список возможных последующих слов
            next_words = n_word[tuple(text_ans[i:i + seed])]
            """ выбираем рандомно слово из возможных для данной n-граммы
                учитываем вероятность каждого с помощью параметра p в np.random.choice"""
            text_ans.append(next_words[int(random.choice(len(next_words), 1,
                                                         p=list(map(lambda x: x[1], next_words))))][0])
        # если нет последующих слов, то завершаем с тем, что есть
        except Exception:
            print('нет подходящих слов')
            break

    print(*text_ans)
