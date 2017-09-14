=========================
RabbitMQ Python connector
=========================
.. image:: http://ci.eionet.europa.eu/job/eea/job/eea.rabbitmq.client/job/master/badge/icon
  :target: http://ci.eionet.europa.eu/job/eea/job/eea.rabbitmq.client/job/master/display/redirect

Basic RabbitMQ Python connector.

Contents
========

.. contents::

Introduction
============

eea.rabbitmq.client is a connector for a RabbitMQ_ server.

.. _RabbitMQ: https://www.rabbitmq.com

API
===

Usage example::

    from eea.rabbitmq.client import RabbitMQConnector

    rabbit_config = {
        'rabbit_host': "10.0.0.1",
        'rabbit_port': "8080",
        'rabbit_username': "admin",
        'rabbit_password': "admin"
    }
    queue_name = "QUEUE_NAME"

    rabbit = RabbitMQConnector(**rabbit_config)
    rabbit.open_connection()
    rabbit.declare_queue(queue_name)
    rabbit.send_message(queue_name, "body text")
    rabbit.close_connection()
