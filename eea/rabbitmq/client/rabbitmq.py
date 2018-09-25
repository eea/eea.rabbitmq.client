""" RabbitMQ connector - methods to work with the RabbitMQ service
"""

import logging
import pika

logger = logging.getLogger("eea.rabbitmq.client")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "%(asctime)s - "
    "%(name)s/%(filename)s/%(funcName)s - "
    "%(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)


class RabbitMQConnector(object):
    """ RabbitMQ connector
    """

    def __init__(self, rabbit_host, rabbit_port, rabbit_username,
                 rabbit_password):
        """ """
        self.__rabbit_connection = None
        self.__rabbit_channel = None
        self.__rabbit_host = rabbit_host
        self.__rabbit_port = rabbit_port
        self.__rabbit_credentials = pika.PlainCredentials(rabbit_username,
                                                          rabbit_password)

    def open_connection(self):
        """ Connect to service and open a channel
        """
        try:
            self.__rabbit_connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host=self.__rabbit_host,
                    port=self.__rabbit_port,
                    credentials=self.__rabbit_credentials,
                    heartbeat_interval=0))
            self.__rabbit_channel = self.__rabbit_connection.channel()
        except Exception, err:
            logger.error(
                'CONNECTING to RabbitMQ at %s:%s FAILED with error: %s',
                self.__rabbit_host,
                self.__rabbit_port,
                err)
        else:
            logger.info(
                'CONNECTING to RabbitMQ at %s:%s OK',
                self.__rabbit_host,
                self.__rabbit_port)

    def close_connection(self):
        """ Disconnect from service and kill the channel
        """
        try:
            self.__rabbit_connection.close()
            self.__rabbit_connection = None
            self.__rabbit_channel = None
        except Exception, err:
            logger.error(
                'DISCONNECTING from RabbitMQ at %s:%s FAILED with error: %s',
                self.__rabbit_host,
                self.__rabbit_port,
                err)
        else:
            logger.info(
                'DISCONNECTING from RabbitMQ at %s:%s OK',
                self.__rabbit_host,
                self.__rabbit_port)

    def get_channel(self):
        """ get_channel
        """
        return self.__rabbit_channel

    def get_queue_status(self, queue_name):
        """ Get the specified queue status
        """
        return self.__rabbit_channel.queue_declare(
            queue=queue_name, passive=True)

    def is_queue_empty(self, queue_name):
        """ Check is the specified queue is empty
        """
        status = self.get_queue_status(queue_name)
        is_empty = status.method.message_count == 0
        logger.info(
            'QUEUE %s is empty = %s',
            queue_name,
            is_empty)
        return is_empty

    def declare_queue(self, queue_name):
        """ Declares the specified queue before take any action.
        """
        self.__rabbit_channel.queue_declare(
            queue=queue_name,
            durable=True,
            exclusive=False,
            auto_delete=False)
        logger.info(
            'DECLARE QUEUE \'%s\'',
            queue_name)

    def start_consuming(self, queue_name, callback):
        """ Start consuming message from the queue.
            It may be interrupted by stopping the script (CTRL+C).
        """
        self.declare_queue(queue_name)
        self.__rabbit_channel.basic_consume(callback, queue=queue_name)
        logger.info(
            'WAITING for messages \'%s\'. To exit press CTRL+C',
            queue_name)
        self.__rabbit_channel.start_consuming()

    def get_message(self, queue_name):
        """ Get a single message from the queue
        """
        return self.__rabbit_channel.basic_get(queue=queue_name, no_ack=False)

    def send_message(self, queue_name, body):
        """ Send a message to the queue.
            We use the default exchange and route through
            the queue name.
        """
        self.__rabbit_channel.basic_publish(exchange='',
                                            routing_key=queue_name,
                                            body=body,
                                            properties=pika.BasicProperties(
                                                delivery_mode=2))
        # make message persistent

        logger.info(
            'SENT \'%s\' in \'%s\'',
            body,
            queue_name)
