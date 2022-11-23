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

df = pd.read_json('data/News_Category_Dataset_v3.json', lines=True).sample(1000, random_state=1)
print(df.columns)

for i, row in tqdm(df.iterrows()):
    client.index(index=INDEX_NAME, id=i, document=row.to_dict())
