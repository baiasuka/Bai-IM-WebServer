import pika

def hello_world():
    credentials = pika.PlainCredentials('guest', 'guest')
    conn = pika.BlockingConnection(pika.ConnectionParameters(host='116.62.37.5', port=5672))

    channel = conn.channel()

    channel.queue_declare(queue='Hello')

    channel.basic_publish(exchange='', routing_key='Hello', body=b'hello world')
    print(" [x] Sent 'Hello World!'")
    conn.close()


if __name__ == '__main__':
    hello_world()