from mongoengine import connect
import ssl
import os

from mongoengine import Document, StringField, ListField, DictField, DateTimeField,ComplexDateTimeField


class BlogPostModel(Document):
    name = StringField( unique=True)


# ssl_certfile = os.getenv('SSL_SERTFILE', 'rds-combined-ca-bundle.pem')
ssl_cert_reqs = ssl.CERT_REQUIRED
ssl_ca_certs = os.getenv('SSL_CA_CERTS', 'rds-combined-ca-bundle.pem')
ssl_config = {
    'ssl': True,
    'ssl_certfile': ssl_ca_certs,
    'ssl_cert_reqs': ssl_cert_reqs,
    'ssl_ca_certs': ssl_ca_certs
}


HOST = 'docdb-2020-08-24-12-23-56.cluster-cldrmceq6qdo.us-east-2.docdb.amazonaws.com'
PORT = 27017

connect(
    name='test_db',
    host=HOST,
    port=PORT,
    username='mongo',
    password='iLC4LYFE',
    **ssl_config
)


post = BlogPostModel(name="test")
post.save()

def main():
    pass


if __name__ == "__main__":
    main()
