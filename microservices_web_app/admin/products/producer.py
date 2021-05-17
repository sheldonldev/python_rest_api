import pika

AMQP_URL = 'amqps://akpuvzcs:D474MrduFSaxw19PzP4z_8uhWbGqwGXv@baboon.rmq.cloudamqp.com/akpuvzcs'
params = pika.URLParameters(AMQP_URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish():
	channel.basic_publish(exchange='', routing_key='main', body='hello')
