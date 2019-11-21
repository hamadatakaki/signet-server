# signet - Webページを開きすぎてしまう人のためのWebアプリ

## How to start server 

1. CLIでdockerコンテナを起動し、コンテナ内でWebサーバを立ち上げる.

```
> docker-compose up -d app
> docker-compose exec app /bin/bash
>> python3 app.py
```
