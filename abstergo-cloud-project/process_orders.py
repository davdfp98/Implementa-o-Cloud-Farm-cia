import json

#Lambda

def lambda_handler(event, context):
    print("Processando pedido...")

    pedido = event.get("pedido", "Sem pedido")

    return {
        'statusCode': 200,
        'body': json.dumps(f'Pedido recebido: {pedido}')
    }