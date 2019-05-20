<h1>マジカルバナナ</h1>
AIを用いた無限連想ゲームです☆

<h1>使い方</h1>
1. docker-compose up -d　でコンテナ起動できます．自動的にrunserverも起動します．

コンテナを動かす前にポート80番が使用されていると，ビルドエラーになります．

2．ブラウザでlocalhostに接続すると利用できます．

word2vecのモデルは[日本語Wikipediaエンティティモデル](http://www.cl.ecei.tohoku.ac.jp/~m-suzuki/jawiki_vector)を使用しています．

デフォルトでは，./data/entity_vector/entity_vector.model.binが使用されます．

フォルダを作ってね．

ps．my_site.confはデフォルトのものと同じだと思います．

[メイン画面](https://github.com/shoot16625/magical_banana/blob/master/image.png)