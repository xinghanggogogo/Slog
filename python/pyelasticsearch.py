from pyelasticsearch import ElasticSearch

es = ElasticSearch('http://localhost:9200')

# es.delete_index('test')
# es.create_index(index='test')
# 建立映射出错,采用终端映射
# mapping = {"mappings":{
#                 "test":{
#                     "properties": {
#                         "title": {"type": "text"},
#                         "name": {"type": "text"},
#                         "age": {"type": "integer"},
#                         "id": {"type": "integer"}
#                     }
#                 }
#             }
#         }

# curl -X PUT http://localhost:9200/test -d'{
# "mappings": {
#      "test": {
#           "properties": {
#             "id": {
#                   "index": "analyzed",
#                   "type": "integer"
#               },
#             "name": {
#                 "index": "analyzed",
#                 "type": "string"
#               },
#             "title": {
#                 "index": "analyzed",
#                 "type": "string"
#               },
#             "age": {
#                   "index": "analyzed",
#                   "type": "integer"
#               },
#             "suggest" : {
#                 "type" : "completion",
#                 "analyzer" : "simple", 这里指定了分词方式
#                 "search_analyzer" : "simple",
#                 "payloads" : true
#             }
#           }
#     }
# }
# }'

settings = es.get_settings('test')
mappings = es.get_mapping(index='test', doc_type='test')

print('settings:', settings)
print('mappings:', mappings)

docs = [{'id': 1, 'name': '李干', 'age': 32, 'title': '抽象tv Coder'},
        {'id': 2, 'name': 'Jessica Coder', 'age': 31, 'title': 'Programmer'},
        {'id': 3, 'name': 'Freddy Coder抽', 'age': 29, 'title': 'Office Assistant'}]

es.bulk((es.index_op(doc, id=doc.pop('id')) for doc in docs), index='test', doc_type='test')

es.refresh('test')

res1 = es.get('test', 'test', 1)

# 全文匹配, 注意中英文的分词方式.
# https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html

res8 = es.search(index='test',
                 size=2,
                 query={
                    "query": {
                        "query_string": {
                            "query": "抽"
                        }
                    }
                 })

# 前缀匹配查询,只接受小写.
res12 = es.search(index='test',
                  query={
                    "query": {
                        "prefix": {"title": "p"}
                    }
                  })

# search, 先must_match, filter
res2 = es.search(index='test',
                 query={
                    "query": {
                        "bool": {
                            "must": [{"match": {"name": 'Jessica'}}],
                            "filter": [{"term": {"age": 31}}]
                        }
                    }
                 })

# match_all
res3 = es.search(index='test',
                 doc_type='test',
                 query={"query": {
                            "match_all": {}
                        }
                 })


# search, match, 不完全匹配
res6 = es.search(query={"query": {
                            "match": {"name": 'Jessica'}
                        }
                 })

# Co 因为设置的分词方式导致没有搜索结果
res7 = es.search(index='xing',
                 query={
                    "query": {
                        "query_string" : {
                            "default_field": "_all",
                            "query": "Coder"
                        }
                    }
                 })

# 指定字段查询,并不区分大小写
res9 = es.search(index='test',
                 query={
                    "query": {
                        "query_string": {
                            "fields": ["name", "title"],
                            "query": "Coder",
                        }
                    }
                 })

# 指定字段查询
res10 = es.search(index="test",
                  query={
                      "query": {
                          "multi_match": {
                              "fields": ["name", "title"],
                              "query": "coder"
                          }
                      }
                  })

# 不识别大写,仅仅识别小写
res11 = es.search(index="test",
                  query={
                      "query": {
                          "term": {"name": "coder"}
                      }
                  })

# 跨索引查询:
res14 = es.search(query={
    "query": {
        "indices": {
            "indices": ["test", "xing"],
            "query": {"term": {"name": "coder"}},
        }
    }
})

# 指定分词器查询,指定whitespage分词方式,分词为coder,所以此例无法查询到结果
res15 = es.search(index="test",
                  query={
                      "query": {
                          "match_phrase": {
                              "name": {
                                  "query": "Coder",
                                  "analyzer": "whitespace"
                              }
                          }
                      }
                  })

# 模糊查询,并没有什么用
res16 = es.search(index="test",
                  query={
                        "query": {
                            "fuzzy": {"name": "Jessi"},
                        }
                  })

# 通配符查询于正则表达式查询,并没有什么用
res17 = es.search(index="test",
                  query={
                        "query": {
                            "wildcard": {"name": "Jessi*a"},
                        }
                  })

res18 = es.search(index="test",
                  query={
                      "query": {
                          "regexp": {"name": "J.*a"},
                      }
                  })

print(res18)
