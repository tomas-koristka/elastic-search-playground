import pandas as pd
from tqdm import tqdm

from util import get_client, INDEX_NAME

client = get_client()
df = pd.read_json('data/News_Category_Dataset_v3.json', lines=True)

for i, row in tqdm(df.iterrows()):
    client.index(index=INDEX_NAME, id=i, document=row.to_dict())
