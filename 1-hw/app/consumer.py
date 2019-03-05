#!/usr/bin/env python
import pika

from connector import logging, connection, channel

logging.info("Waiting for messages. To exit press CTRL+C")

def callback(ch, method, properties, body):
    logging.info('Received message: %s', str(body))

channel.queue_declare(queue="hello")
channel.basic_consume(callback, 
                      queue="hello", 
                      no_ack=True)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
    logging.info("GoodBye!")
except Exception:
    channel.stop_consuming()
    logging.error("An error has happened!")
