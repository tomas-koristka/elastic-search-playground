import os

from elasticsearch import Elasticsearch

INDEX_NAME = 'my-fabulous-index'

def get_client():
    username = 'elastic'
    password = 'XIc_5cSGiT89OUpwao-6'
    host = 'https://localhost:9200'
    certificate = os.path.join(os.path.expanduser("~"), 'http_ca.crt')

    return Elasticsearch(host, ca_certs=certificate, basic_auth=(username, password))
