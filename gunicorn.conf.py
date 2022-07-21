workers = 4
accesslog = "-"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(q)s" "%(D)s"'
bind = "0.0.0.0:8000"
keepalive = 120
timeout = 120
worker_class = "gthread"
threads = 3