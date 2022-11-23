from util import get_client, INDEX_NAME

client = get_client()

SEARCHED_FIELD = 'short_description'

query_string = {'query_string': {
    'query': '(new york city) OR (big apple)',
    'default_field': SEARCHED_FIELD}
}
highlight = {'fields': {SEARCHED_FIELD: {}}}

resp = client.search(index=INDEX_NAME, query=query_string, highlight=highlight)

print(f'Got {resp["hits"]["total"]["value"]} Hits:')

for hit in resp['hits']['hits']:
    doc = hit['_source']
    score = hit['_score']
    print('Score', score, '| Headline:', doc['headline'], 'Description\n\t', hit['highlight'])
