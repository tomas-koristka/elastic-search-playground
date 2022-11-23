from util import get_client, INDEX_NAME

client = get_client()

SEARCHED_FIELD = 'short_description'

fuzzy_query = {'fuzzy': {SEARCHED_FIELD:
                             {'value': 'big'}
                         }
               }

highlight = {'fields': {SEARCHED_FIELD: {}}}

resp = client.search(index=INDEX_NAME, query=fuzzy_query, highlight=highlight
                     )

print(f'Got {resp["hits"]["total"]["value"]} Hits:')

for hit in resp['hits']['hits']:
    doc = hit['_source']
    score = hit['_score']
    print('Score', score, '| Headline:', doc['headline'], 'Description\n\t', hit['highlight'])
