from util import get_client, INDEX_NAME


client = get_client()
client.indices.delete(index=INDEX_NAME)