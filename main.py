import train_model
import generate


# клас модели
class NGramModel():
    seed = 2
    model_dir = ''
    n_word = {}

    def load_model(self, model_dir):
        self.model_dir = model_dir
        self.n_word = generate.load_model(model_dir)

    def fit(self, texts_dir='', seed=2, model=''):
        train.fit(seed, texts_dir, model)

    def generate(self, prefix, length=20, ran_seed=23):
        generate.generate(prefix, length, self.n_word, ran_seed)
        return self


if __name__ == '__main__':
    inp = ''
    print('------Comands: fit(training), generate(text generation), exit', sep='\n')
    model = NGramModel()
    while inp != 'exit':
        inp = input('---Enter comand: ')
        if inp == 'fit':
            seed = int(input('------Enter seed (number of words):'))
            data = input('------Enter data folder name:')
            model_dir = input('------Enter model name:')
            print('Происходит  магия')
            model.fit(data, seed, model_dir)
            print('--------model is fitted and saved-------')

        elif inp == 'generate':
            model_path = input('Enter model name:')
            model.find_word = generate.load_model(model_path)
            ran_seed = int(input('Enter random seed:'))
            pref = input(f'Enter start words {len(list(model.find_word.keys())[0])} (leave blank to use randomly generated):')
            length = int(input('Enter length of the generated text:'))
            model.generate(pref, length, ran_seed)
        else:
            print('((((')
