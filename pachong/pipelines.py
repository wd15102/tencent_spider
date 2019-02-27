import json
class PachongPipeline(object):
    def __init__(self):
        self.filename = open('tencentJobs.csv','wb+')
    def process_item(self, item, spider):
        text = json.dumps(dict(item),ensure_ascii=False)+',\n'
        self.filename.write(text.encode('utf-8-sig'))
        return item
    def close_spider(self,spider):
        self.filename.close()
