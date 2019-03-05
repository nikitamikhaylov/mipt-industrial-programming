#!/usr/bin/env python
import pika
import time
import random

from connector import logging, connection, channel

channel.queue_declare("hello")

while True:
    rand_msg = str(random.randint(10, 1000))
    channel.basic_publish(exchange='',
			              routing_key='hello',
			              body=rand_msg)
    logging.info('Sent message: %s', rand_msg)

    time_to_sleep = random.randint(1, 5)
    logging.info('Sleeping for %d', time_to_sleep)
    time.sleep(time_to_sleep)

connection.close()
