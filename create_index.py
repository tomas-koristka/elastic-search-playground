import pandas as pd
from tqdm import tqdm

from util import get_client, INDEX_NAME

settings = {
    'number_of_shards': 1,
    'number_of_replicas': 0
}

mappings = {}

client = get_client()
client.indices.create(index=INDEX_NAME, settings=settings, mappings=mappings)