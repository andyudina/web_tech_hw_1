#gunicorn --config=/home/nastya/helloworld/configs/hello-world-gunicorn.py helloworld-test:app -D
#gunicorn --config=/home/nastya/helloworld/configs/hello-world-gunicorn.py wsgi:application -D

import multiprocessing

bind = "127.0.0.1:8000"
workers = multiprocessing.cpu_count() * 2 + 1

