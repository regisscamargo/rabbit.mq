#!/usr/bin/env python
import pika
import random

credentials = pika.PlainCredentials("abcBolinhas", "abcBolinhas")  # 'guest', 'guest'
parameters = pika.ConnectionParameters("192.168.56.1", 3306, "/", credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue="filaTeste")  # declara a fila
strEnviar = "Mensagem " + str(random.randrange(0, 100, 1))
# roteia para a fila
channel.basic_publish(exchange="", routing_key="filaTeste", body=strEnviar)

print("Enviada: " + strEnviar)
connection.close()
