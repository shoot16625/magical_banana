from django.shortcuts import render
from banana import models
from gensim.models import KeyedVectors


initial_word = "パソコン"
previous_words = [initial_word]
FILE = "/var/www/html/data/entity_vector/entity_vector.model.bin"
# FILE = "../data/entity_vector/entity_vector.model.bin"
model = KeyedVectors.load_word2vec_format(FILE, binary=True)
print("load_view")

def index(request):
  # 初期表示用
  if request.GET.get('input_word') is None:
    d = {
        'input_flag': 1,
        'initial': initial_word,
      }
    return render(request, 'index.html', d)

  # 入力があった場合
  input_word = request.GET.get('input_word')
  print(previous_words)

  # 入力単語の確認
  if models.input_confirm(input_word):
    d = {
        'input_none': 1,
        'output_word': previous_words[-1],
        'input_word': previous_words[-2],
        'previous_words': previous_words,
      }
    return render(request, 'index.html', d)

  # 入力が重複していないか
  if models.losing_user1(input_word, previous_words):
    d = {
        'losing_user1': 1,
        'output_word': previous_words[-1],
        'input_word': previous_words[-2],
        'previous_words': previous_words,
      }
    return render(request, 'index.html', d)

  losing_user_2 = models.losing_user2(model, input_word, previous_words)

  output_word, new_word_flag = models.output_word(model, input_word, previous_words)

  d = {
        'losing_user2': losing_user_2,
        'input_word': input_word,
        'output_word': output_word,
        'new_word': new_word_flag,
        'previous_words': previous_words,
    }

  return render(request, 'index.html', d)