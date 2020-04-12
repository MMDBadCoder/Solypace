from elasticsearch import Elasticsearch
import os

from searchEngine.pdf_search_engine.pdf2text import convert_pdf_to_txt

INDEX_NAME = 'solypace_pdfs'
PORT = 9200
DOC_TYPE = 'pdf_text'


def index_new_pdf(path, pdf_label, pdf_description, file_id):
    try:
        full_text = convert_pdf_to_txt(path)
        es = Elasticsearch([{'host': 'localhost', 'port': PORT}])
        body = {
            'label': pdf_label,
            'description': pdf_description,
            'full_text': full_text
        }
        res = es.index(index=INDEX_NAME, doc_type=DOC_TYPE, id=file_id, body=body)
        return res
    except Exception as e:
        print(str(e))
        return False


def delete_pdf(file_id):
    try:
        es = Elasticsearch([{'host': 'localhost', 'port': PORT}])
        res = es.delete(index=INDEX_NAME, doc_type=DOC_TYPE, id=file_id)
        print(res)
    except Exception as e:
        print(str(e))
        return False


def search_on_pdf_texts(query_text):
    try:
        es = Elasticsearch([{'host': 'localhost', 'port': PORT}])
        res = es.search(index='files', doc_type='file', body={
            "query": {
                "multi_match": {
                    "fields": ["name", 'description', "full_text"],
                    "query": query_text,
                    "fuzziness": "AUTO",
                    "prefix_length": 2,
                    "max_expansions": 1,
                }
            },
            "_source": ["id"],
        })
        return res
    except Exception as e:
        print(e)
        return False


def turn_on_DB():
    os.system('systemctl start elasticsearch.service')


def turn_of_DB():
    os.system('systemctl stop elasticsearch.service')
