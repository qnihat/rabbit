#before everythin install Erlang and rabbit exe files.
#pip install pika
import pika

txt_to_send='salam necesen'
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body=txt_to_send)
print(" [x] Sent")
connection.close()