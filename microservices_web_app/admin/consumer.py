import pika, json, django, os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

AMQP_URL = 'amqps://akpuvzcs:D474MrduFSaxw19PzP4z_8uhWbGqwGXv@baboon.rmq.cloudamqp.com/akpuvzcs'
params = pika.URLParameters(AMQP_URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print("Recieve userid in admin")
    try:
        id = json.loads(body)
        print(id)
    except: return

    if properties.content_type == 'product_liked':
        product = Product.objects.get(id=id)
        product.likes = product.likes + 1
        print(product.likes)
        product.save()
        print("Product likes increased")


channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started Consuming')
channel.start_consuming()

channel.close()
