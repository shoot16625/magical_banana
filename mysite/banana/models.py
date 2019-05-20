from django.db import models
import MeCab
import re
import numpy as np
# Create your models here.

# 2回読み込まれる
print("load_model")

# 駄目なwordはフラグ1を返す
def input_confirm(input_word):
  flag = 0
  #入力が空
  if input_word == "":
    print("入力して下さい。それとも、諦めますか？諦めたらそこで終わりですよ！")
    flag = 1
    return flag

  #入力が名詞・形容詞以外
  I_part, flag, _ = part_confirm(input_word)
  # I_part = "名詞"
  if flag == 1:
    print("文章禁止！！")
    return flag

  if I_part != "名詞" and I_part != "形容詞":
    print("名詞か形容詞限定です！！")
    flag = 1
    return flag


def part_confirm(word):
  # word = re.sub('[.*]', '.*', word)
  mecab = MeCab.Tagger("-Ochasen")
  # mec = MeCab.Tagger("-Ochasen -d /usr/lib/mecab/dic/mecab-ipadic-neologd")
  info = mecab.parse(word).split("\t")
  print(info)
  if not re.search("EOS", info[5]):
    flag = 1
    info_part = info[3].split("-")
    print("文章を入力するな")
    return info_part[0], flag, flag

  info_part = info[3].split("-")
  if len(info_part) == 1:
    print("横棒がない")
    return info_part[0], info_part[0], info[1]
  return info_part[0], info_part[1], info[1]


# まけ判定
# 重複していないか
def losing_user1(input_word, previous_words_list):
  flag = 0
  for pre_word in previous_words_list:
    if pre_word == input_word:
      flag = 1
      print("重複した単語です！！\n")
      break
  return flag


#システム単語とユーザー単語の内積が小さめだったら表示
def losing_user2(model, input_word, previous_words_list):
  flag = 0
  thresh = 0.3
  try:
    similarity = model.similarity(input_word, previous_words_list[-1])
    if similarity < thresh:
      flag = 1
    return flag
  # 入力単語が辞書に乗っていない場合
  except:
    return flag


def output_word(model, word, previous_words_list):
  N = 100
  # 辞書登録があるかないか
  try:
    new_word_flag = 0
    pairs = model.wv.most_similar(word, topn=N)
    X = [0]*N
    for i, j in enumerate(pairs):
      X[i] = j[0]
    out_word = X[1:]
  except:
    new_word_flag = 1
    pairs = model.wv.most_similar(previous_words_list[-1], topn=N)
    X = [0]*N
    for i, j in enumerate(pairs):
      X[i] = j[0]
    out_word = X[1:]

  previous_words_list.append(word)
  out_word = [re.sub("\[","",word) for word in out_word]
  out_word = [re.sub("\]","",word) for word in out_word]
  print()
  print(out_word[0:10])
  print()
  flag = 1
  i = 0
  mecab = MeCab.Tagger("-Ochasen")
  for output_word in out_word:
    if output_word in previous_words_list:
      continue
      # かな変換して一致するものは排除
    if mecab.parse(output_word).split("\t")[1] == mecab.parse(word).split("\t")[1]:
      continue

    out_part, outpart2, _ = part_confirm(output_word)
    if out_part in ["名詞", "形容詞"] or outpart2 == "数":
      previous_words_list.append(output_word)
      print("「{0}」といったら >> {1}".format(word, output_word))
      return output_word, new_word_flag

  # もしも言い返しがなかったら，
  return "私の負けです(*^^*)", new_word_flag