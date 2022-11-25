from util import get_client, INDEX_NAME

client = get_client()

query = {
    'boosting': {
        'positive': {
            'term': {'short_description': 'money'}
        },
        'negative': {
            'term': {'short_description': 'bank donation robber'}
        },
        'negative_boost': 0.5
    },
}

resp = client.search(index=INDEX_NAME, query=query)

print(f'Got {resp["hits"]["total"]["value"]} Hits:')

for hit in resp['hits']['hits']:
    doc = hit['_source']
    score = hit['_score']
    print('Score', score, '| Headline:', doc['headline'], 'Description\n\t', doc['date'])
