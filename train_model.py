import re
import pickle
import os


def fit(seed=2, data_dir='data', model=''):
    text = ''
    # обьединяем все файлы в один большой текст
    for filename in os.listdir(data_dir):
        with open(os.path.join(data_dir, filename), 'r', encoding='UTF-8') as f:
            text += ' ' + f.read().lower()
    # вычленяем только слова
    text = [i for i in re.findall(r'\w+', text)]

    print('---Number of words:', len(text))
    find_word = {}

    for i in range(len(text) - seed):
        next_words = find_word[tuple(text[i:i + seed])]
        # если n-грамы нет в словаре, добавляем её
        if not find_word.__contains__(tuple(text[i:i + seed])):
            next_words = [1, {text[i + seed]: 1}]
        else:
            # иначе добавляем, если следующего слова нет в словаре,
            # добавляем в словарь и увеличиваем количество всех слов
            if text[i + seed] in find_word[tuple(text[i:i + seed])][1]:
                next_words[1][text[i + seed]] += 1
            else:
                # если след словов есть, то увеличиваем количество этих слов и кол-во общих слов
                next_words[1][text[i + seed]] = 1
            next_words[0] += 1

    for pref in find_word.keys():
        probs = []
        for i in find_word[pref][1].keys():
            # вычисляем вероятность всех след слов: (кол-во таких слов/кол-во всех слов, идущих после этой n-граммы)
            probs.append([i, find_word[pref][1][i] / find_word[pref][0]])
        find_word[pref] = probs

    with open('models/'+model+'.pickle', 'wb') as f:
        pickle.dump(find_word, f)
