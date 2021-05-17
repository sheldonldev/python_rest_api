import pika

AMQP_URL = 'amqps://akpuvzcs:D474MrduFSaxw19PzP4z_8uhWbGqwGXv@baboon.rmq.cloudamqp.com/akpuvzcs'
params = pika.URLParameters(AMQP_URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
	print('recieve in admin')
	print(body)

channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()
