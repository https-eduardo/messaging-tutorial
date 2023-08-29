import pika
import pyqrcode

QUEUE = 'qr_code_queue'
EXCHANGE = 'pix_exchanges'

connection_parameters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
)

channel = pika.BlockingConnection(connection_parameters).channel()


def get_qrcode_text(pix_key):
    qr_code = pyqrcode.create(pix_key)
    return qr_code.text()


def get_pix_email(pix_key):
    CODE_PREFIX = '00020126440014BR.GOV.BCB.PIX0122'
    CODE_MIDDLE = '5204000053039865802BR5913'

    splittedStr = pix_key.split(CODE_PREFIX)[1]
    email = splittedStr.split(CODE_MIDDLE)[0]

    return email


def save_qr_code(ch, method, props, body):
    pix_key = bytes.decode(body, encoding='utf-8')

    qr_code_text = get_qrcode_text(pix_key)
    email = get_pix_email(pix_key)

    properties = pika.BasicProperties(delivery_mode=2)
    channel.basic_publish(
        exchange=EXCHANGE,
        body=qr_code_text,
        routing_key="",
        properties=properties
    )
    with open("logs.txt", "a+", encoding="utf-8") as logs_file:
        logs_file.write(f'{email} - {pix_key}\n')
        logs_file.close()


channel.basic_consume(
    queue=QUEUE,
    auto_ack=True,
    on_message_callback=save_qr_code
)

print(f'Consumindo dados da fila {QUEUE}:')
channel.start_consuming()
