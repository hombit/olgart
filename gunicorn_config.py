import multiprocessing, os.path

command = '/usr/local/bin/gunicorn'
pythonpath = os.path.dirname( os.path.abspath(__file__) )
bind = '127.0.0.1:9000'
workers = multiprocessing.cpu_count() * 2 + 1
user = 'olgart'
