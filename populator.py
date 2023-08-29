import pika
from pix_generator import PixGenerator

LIMIT = 50
amount_to_insert = int(
    input('Amount of Pix QRCodes that you want to insert: (Limit of 50) '))
if amount_to_insert > LIMIT:
    raise ValueError('Limit of Pix QRCodes exceeded.')

connection_parameters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest"
    )
)

channel = pika.BlockingConnection(connection_parameters).channel()

generator = PixGenerator()
properties = pika.BasicProperties(
    delivery_mode=2
)

for i in range(0, amount_to_insert):
    qr_code = generator.generate()
    channel.basic_publish(
        exchange="qr_code_exchanges",
        body=qr_code,
        routing_key="",
        properties=properties,
    )

print(f'Queue populated with {amount_to_insert} Pix QRCodes.')
