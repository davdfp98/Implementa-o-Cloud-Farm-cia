import boto3

def upload_file():
    s3 = boto3.client('s3')

    file_name = 'pedido.json'
    bucket = 'abstergo-data-bucket'

    try:
        s3.upload_file(file_name, bucket, file_name)
        print("Upload realizado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar arquivo: {e}")

if __name__ == "__main__":
    upload_file()