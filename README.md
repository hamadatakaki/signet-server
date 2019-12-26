# signet - Webページを開きすぎてしまう人のためのWebアプリ

## How to start server 

1. CLIでdockerコンテナを起動し、コンテナ内でWebサーバを立ち上げる.

```
> docker-compose up -d db
> docker-compose up -d app
> docker-compose exec app /bin/bash
>> python3 seed.py
>> python3 app.py
```

2. APIへアクセス.

[localhost:8000/hello](http://localhost:8000/hello)にブラウザからアクセスし動作を確認する.

