import boto3


def list_buckets():
    s3 = boto3.client("s3")

    response = s3.list_buckets()

    for bucket in response['Buckets']:
        print(bucket)


def save_to_s3(file_to_save, bucket_id, bucket_tag):
    s3 = boto3.client("s3")

    try:
        s3.upload_file(file_to_save, bucket_id, bucket_tag)
        return True
    except Exception:
        raise


def main():
    pass


if __name__ == "__main__":
    save_to_s3(file_to_save='config.txt', bucket_id='cbaxter1988', bucket_tag='config.txt')
