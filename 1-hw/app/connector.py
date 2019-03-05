import pika
import time
import sys
import logging

logging.basicConfig(format='%(levelname)s %(message)s',
                    level=logging.INFO)

def try_connect(conn_params):
    try:
        return pika.BlockingConnection(conn_params)
    except Exception:
        logging.info("Trying to reconnect to RabbitMQ")
        time.sleep(5)
        return try_connect(conn_params)    

host, port = sys.argv[1:]

conn_params = pika.ConnectionParameters(host, port)
connection = try_connect(conn_params)
channel = connection.channel()