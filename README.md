#はじめに
$ git clone git@github.com:hm-tlab/reisenBot.git
$ cd reisenBot
リポジトリをローカルにクローン、リポジトリに移動

#パッケージの環境を合わせる
$ pip install -r requirements.txt

#.envに自分のローカルでのtokenを貼り付ける
$ vi .env
DISCORD_TOKEN=この部分にペースト
#.env にローカルでのcommand prefixを書く（他人や本番用となるべく被らないように）
COMMAND_PREFIX=!

#以下コマンドを実行してbotIDやらがコンソールに出たら起動成功
$ python3.8 run.py

#終了方法
現状だとターミナルで ^C を打って強制終了

#機能実装の進め方
feature/casinoroulette のように機能がわかるブランチを作成する
実装ができたら $ mypy filename.py を走らせて型チェック
例：
$ mypy src/ReisenBot.py 
Success: no issues found in 1 source file

通ったら feature/xxx -> masterへのプルリクを出す
