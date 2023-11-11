# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from typing import Optional

import psycopg2

class SrealityCrawlerPipeline:
    """Class that takes care of storing the parsed data into database."""

    def __init__(self):
        self.connection: Optional[psycopg2.connection] = None
        self.cur: Optional[psycopg2.cursor] = None

    def open_spider(self, spider):  # pylint: disable=unused-argument
        """Create a connection to the database."""
        hostname = "postgresql"
        username = "django"
        password = "django"
        database = "flats_db"
        self.connection = psycopg2.connect(
            host=hostname, user=username, password=password, dbname=database
        )
        self.cur = self.connection.cursor()

    def close_spider(self, spider):  # pylint: disable=unused-argument
        """Close connection to the database."""
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):  # pylint: disable=unused-argument
        """Store the parsed items into database."""
        self.cur.execute(
            f"INSERT INTO flats (title, image_url) VALUES ('{item['name']}', '{item['url']}');"
        )
        self.connection.commit()
        return item
