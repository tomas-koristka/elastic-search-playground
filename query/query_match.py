from util import get_client, INDEX_NAME

client = get_client()

resp = client.search(index=INDEX_NAME, query={
    "match": {"short_description": "money"}
})

print(f'Got {resp["hits"]["total"]["value"]} Hits:')

for hit in resp['hits']['hits']:
    doc = hit['_source']
    score = hit['_score']
    print('Score', score, '| Headline:', doc['headline'], 'Description\n\t', doc['short_description'])
