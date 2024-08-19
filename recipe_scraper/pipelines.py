# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import json
import logging

class RecipescraperPipeline:
    def open_spider(self, spider):
        self.file = open('new_recipes.json', 'w', encoding='utf-8')
        logging.info("Opened new_recipes.json") 

    def close_spider(self, spider):
        self.file.close()
        logging.info("Closed new_recipes.json")

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        logging.info(f"Processed item: {item['recipe_name']}")
        return item
