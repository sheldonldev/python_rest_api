import pika, json

from main import Product, db

AMQP_URL = 'amqps://akpuvzcs:D474MrduFSaxw19PzP4z_8uhWbGqwGXv@baboon.rmq.cloudamqp.com/akpuvzcs'
params = pika.URLParameters(AMQP_URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('recieve in main')
    try:
        data = json.loads(body)
        print(data)
    except: return

    if properties.content_type == 'product_created':
        print("Creating...")
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()
        print("Product created")

    elif properties.content_type == 'product_updated':
        print("Updating...")
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()
        print("Product updated")

    elif properties.content_type == 'product_deleted':
        print("Deleting...")
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()
        print("Product deleted")

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')
channel.start_consuming()

channel.close()
