from datetime import datetime
from elasticsearch_dsl import DocType, Date, Nested, Boolean, \
    analyzer, InnerObjectWrapper, Completion, Keyword, Text, Integer

from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer

from elasticsearch_dsl.connections import connections
connections.create_connection(hosts=["localhost"])

class CustomAnalyzer(_CustomAnalyzer):
    def get_analysis_definition(self):
        return {}


ik_analyzer = CustomAnalyzer("ik_max_word", filter=["lowercase"])

class ArticleType(DocType):
    url = Keyword()
    imge = Keyword()
    ''''分词 Completion支持搜索建议 ，因为直接指定分词器会报错不知道现在修改了没，
    所以现在需要自定义CustomAnalyzer， 本字段存储搜索建议'''
    suggest = Completion(analyzer=ik_analyzer)
    '''不加搜索建议的分词器'''
    content = Text(analyzer="ik_max_word")

    class Meta:
        index = "jobbole"
        doc_type = "article"

if __name__ == "__main__":
    ArticleType.init()
