# 删除index
curl -XDELETE localhost:9200/btsong

# 查看当前所有的index
curl 106.75.97.4:9200/_cat/indices?v

# 查看某index mapping
curl -XGET 106.75.97.4:9200/song/_mapping?pretty

# 创建index song 和 type song
curl -X PUT http://localhost:9200/song -d'{
"mappings": {
    	 "song": {
          	"properties": {
                "id": {
                  	"index": "analyzed",
                  	"type": "integer"
              },
            	"title": {
                	"index": "analyzed",
                	"type": "keyword"
              },
            	"name": {
                  	"index": "analyzed",
                  	"type": "keyword"
              },
              "artist": {
                  	"index": "analyzed",
                  	"type": "keyword"
              },
              "artist_id": {
                  	"index": "analyzed",
                  	"type": "integer"
              },
              "remark": {
                  	"index": "analyzed",
                  	"type": "string"
              },
              "duration": {
                  	"index": "analyzed",
                  	"type": "integer"
              },
              "krc": {
                  	"index": "analyzed",
                  	"type": "string"
              },
              "bitrate": {
                  	"index": "analyzed",
                  	"type": "integer"
              },
              "size": {
                  	"index": "analyzed",
                  	"type": "integer"
              },
              "hash": {
                  	"index": "analyzed",
                  	"type": "string"
              },
              "hash320": {
                  	"index": "analyzed",
                  	"type": "string"
              },
              "bthash": {
                  	"index": "analyzed",
                  	"type": "string"
              },
              "btname": {
                  	"index": "analyzed",
                  	"type": "string"
              },
              "source": {
                  	"index": "analyzed",
                  	"type": "string"
              },
              "source_id": {
                  	"index": "analyzed",
                  	"type": "string"
              },
              "label": {
                  	"index": "analyzed",
                  	"type": "keyword"
              },
              "state": {
                  	"index": "analyzed",
                  	"type": "integer"
              },
              "create_time": {
                  	"index": "analyzed",
                  	"type": "string"
              },
              "update_time": {
                  	"index": "analyzed",
                  	"type": "string"
              },
              "suggest" : {
	              "type" : "completion",
	              "analyzer" : "simple",
	              "search_analyzer" : "simple"
            }
          }
    }
}
}'

curl -X PUT http://localhost:9200/btsong -d'{
"mappings": {
    	 "btsong": {
          	"properties": {
            	"id": {
                  	"index": "analyzed",
                  	"type": "integer"
              },
            	"title": {
                	"index": "analyzed",
                	"type": "keyword"
              },
            	"name": {
                  	"index": "analyzed",
                  	"type": "keyword"
              },
              "artist": {
                  	"index": "analyzed",
                  	"type": "keyword"
              },
              "artist_id": {
                  	"index": "analyzed",
                  	"type": "integer"
              },
              "remark": {
                  	"index": "analyzed",
                  	"type": "string"
              },
              "duration": {
                  	"index": "analyzed",
                  	"type": "integer"
              },
              "bitrate": {
                  	"index": "analyzed",
                  	"type": "integer"
              },
              "size": {
                  	"index": "analyzed",
                  	"type": "integer"
              },
              "hash": {
                  	"index": "analyzed",
                  	"type": "string"
              },
              "hash320": {
                  	"index": "analyzed",
                  	"type": "string"
              },
              "source": {
                  	"index": "analyzed",
                  	"type": "string"
              },
              "source_id": {
                  	"index": "analyzed",
                  	"type": "string"
              },
              "label": {
                  	"index": "analyzed",
                  	"type": "keyword"
              },
              "state": {
                  	"index": "analyzed",
                  	"type": "integer"
              },
              "create_time": {
                  	"index": "analyzed",
                  	"type": "string"
              },
              "update_time": {
                  	"index": "analyzed",
                  	"type": "string"
              },
              "suggest" : {
	              "type" : "completion",
	              "analyzer" : "simple",
	              "search_analyzer" : "simple"
            }
          }
    }
}
}'

# search: query string as a parameter的形式
curl -XGET 'localhost:9200/song/song/_search?q=name:nana'
curl -XGET 'localhost:9200/_search?q=name:nana'
curl -XGET 'http://localhost:9200/song/song/1'

# search: request body的形式
curl -XGET 'localhost:9200/song/song/_search?pretty' -H 'Content-Type: application/json' -d'
{
    "query" : {
        "term" : { "name" : "nana" }
    }
}
'

# 关于from和size参数:
# the from parameter defines the offset from the first result you want to fetch
# The size parameter allows you to configure the maximum amount of hits to be returned
curl -XGET 'localhost:9200/_search?pretty' -H 'Content-Type: application/json' -d'
{
    "from" : 0, "size" : 10,
    "query" : {
        "term" : { "name" : "nana" }
    }
}
'

# 关于sort: sort list里是排序的优先级, 上级相等时比较下级
curl -XGET 'localhost:9200/song/song/_search?pretty' -H 'Content-Type: application/json' -d'
{
    "sort" : [
        "_score",
        { "duration" : "desc" }
    ],
    "query" : {
        "term" : { "name" : "apple" }
    }
}
'

# 关于source参数, source参数默认是true, 设置为false时es只会返回id而不会返回hits的详细内容, 当然你也可以制定参数
curl -XGET 'localhost:9200/song/song/_search?pretty' -H 'Content-Type: application/json' -d'
{
    "_source": false,
    "query" : {
        "term" : { "name" : "nana" }
    }
}
'
curl -XGET 'localhost:9200/song/song/_search?pretty' -H 'Content-Type: application/json' -d'
{
    "_source": [ "name", "artist"],
    "query" : {
        "term" : { "name" : "nana" }
    }
}
'

# 关于script, 会返回test1字段
curl -XGET 'localhost:9200/song/song/_search?pretty' -H 'Content-Type: application/json' -d'
{
    "query" : {
        "term" : { "name" : "nana" }
    },
    "script_fields" : {
        "test1" : {
            "script" : {
                "lang": "painless",
                "inline": "doc[\"duration\"].value * 2"
            }
        }
    }
}
'

# 返回指定字段doc_value
curl -XGET 'localhost:9200/_search?pretty' -H 'Content-Type: application/json' -d'
{
    "query" : {
        "term" : { "name" : "nana" }
    },
    "docvalue_fields" : ["duration"]
}
'

# post filter and insert data
curl -XPUT 'localhost:9200/shirts?pretty' -H 'Content-Type: application/json' -d'
{
    "mappings": {
        "item": {
            "properties": {
                "brand": { "type": "keyword"},
                "color": { "type": "keyword"},
                "model": { "type": "keyword"}
            }
        }
    }
}
'
curl -XPUT 'localhost:9200/shirts/item/1?refresh&pretty' -H 'Content-Type: application/json' -d'
{
    "brand": "gucci",
    "color": "red",
    "model": "slim"
}
'

# 关于highlight
curl -XGET 'localhost:9200/song/song/_search?pretty' -H 'Content-Type: application/json' -d'
{
    "query" : {
        "match": { "name": "nana" }
    },
    "highlight" : {
        "fields" : {
            "name" : {}
        }
    }
}
'

# 关于re, 这里并不是很清楚.
curl -XPOST 'localhost:9200/song/song/_search?pretty' -H 'Content-Type: application/json' -d'
{
   "query" : {
      "match" : {
         "name" : {
            "operator" : "or",
            "query" : "the quick brown"
         }
      }
   },
   "rescore" : {
      "window_size" : 50,
      "query" : {
         "rescore_query" : {
            "match_phrase" : {
               "name" : {
                  "query" : "the quick brown",
                  "slop" : 2
               }
            }
         },
         "query_weight" : 0.7,
         "rescore_query_weight" : 1.2
      }
   }
}
'
curl -XPOST 'localhost:9200/song/song/_search?pretty' -H 'Content-Type: application/json' -d'
{
   "query" : {
      "match" : {
         "name" : {
            "operator" : "or",
            "query" : "the quick brown"
         }
      }
   },
}
'

# an example of query clauses being used in query and filter context in the search API
# https://www.elastic.co/guide/en/elasticsearch/reference/current/query-filter-context.html
GET /_search
{
  "query": {
    "bool": {
      "must": [
        { "match": { "title":   "Search"        }},
        { "match": { "content": "Elasticsearch" }}
      ],
      "filter": [
        { "term":  { "status": "published" }},
        { "range": { "publish_date": { "gte": "2015-01-01" }}}
      ]
    }
  }
}

# Match All Query
# The most simple query, which matches all documents, giving them all a _score of 1.0.
GET /_search
{
    "query": {
        "match_all": {}
    }
}
# The _score can be changed with the boost parameter:
GET /_search
{
    "query": {
        "match_all": { "boost" : 1.2 }
    }
}


# Match Queryedit
# match queries accept text/numerics/dates, analyzes them, and constructs a query. For example:
GET /_search
{
    "query": {
        "match": {
            "message": "this is a test"
        }
    }
}

# The multi_match query builds on the match query to allow multi-field queries:
GET /_search
{
  "query": {
    "multi_match" : {
      "query": "this is a test",
      "fields": [ "subject", "message" ]
    }
  }
}

# A query that uses a query parser in order to parse its content. Here is an example:
GET /_search
{
    "query": {
        "query_string" : {
            "default_field" : "content",
            "query" : "this AND that OR thus"
        }
    }
}

{
  "song" : {
    "mappings" : {
      "song" : {
        "properties" : {
          "artist" : {
            "type" : "text",
            "boost" : 8.0,
            "analyzer" : "ik_smart",
            "include_in_all" : true
          },
          "name" : {
            "type" : "text",
            "boost" : 8.0,
            "analyzer" : "ik_smart",
            "include_in_all" : true
          },
          "title" : {
            "type" : "text",
            "boost" : 8.0,
            "analyzer" : "ik_smart",
            "include_in_all" : true
          }
        }
      }
    }
  }
}

#一个合适的中文分词mapping
curl -X PUT http://localhost:9200/aim_song -d'{
"mappings": {
    "aim_song": {
          	"properties": {
                "artist" : {
                    "type" : "text",
                    "boost" : 8.0,
                    "analyzer" : "ik_smart",
                    "include_in_all" : true
                },
                "name" : {
                    "type" : "text",
                    "boost" : 8.0,
                    "analyzer" : "ik_smart",
                    "include_in_all" : true
                },
                "title" : {
                    "type" : "text",
                    "boost" : 8.0,
                    "analyzer" : "ik_smart",
                    "include_in_all" : true
                }
           }
    }
}
}'
