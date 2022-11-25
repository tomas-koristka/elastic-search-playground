# Elastic search sandbox

## Getting Elastic

I'm running Elastic in Docker - follow installation instructions in
the [official guide](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html).

## Data

I have used news articles data from [kaggle](https://www.kaggle.com/datasets/rmisra/news-category-dataset), the data is
in this repository in `data\News_Category_Dataset_v3.json`.

## Running

Create a virtual environment and install dependencies from `requirements.txt`.

After starting docker, firstly run `create_index.py`, then populate it with `insert_data.py` - you may want to limit the
number of items added as there are 210k entries in the dataset.

You can do so for example by sampling the loaded dataset:

```python
n = 10000
df = pd.read_json('data/News_Category_Dataset_v3.json', lines=True).sample(n, random_state=1)
```

## Querying

I have been exploring the elastic search querying, various queries are located in `query/`.