<h1>マジカルバナナ</h1>
AIを用いた無限連想ゲームです☆

<h1>使い方</h1>
1. docker-compose up -d　でコンテナ起動できます．自動的にrunserverも起動します．

コンテナ動かす前にポート80番が使用されていると，ビルドエラーになります．

2．ブラウザでlocalhostに接続すると利用できます．

word2vecのモデルは![日本語Wikipediaエンティティモデル](http://www.cl.ecei.tohoku.ac.jp/~m-suzuki/jawiki_vector/)を使用しています．
./data/entity_vectorに入れたら動きます．

![メイン画面]()