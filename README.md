# crawler-test
testing crawling web page with scrapy in docker

## installation
To install clone the repo to your desired folder.

In the folder, start the server with:
`docker-compose up`

When started, the result is visible at: 
`http://127.0.0.1:8080/`


## overview
There are 3 folders. 
- `crawl_result`: contains the django server that shows the results.
- `db_init`: contains the init script for the database.
- `sreality_crawler`: contains the crawler to scrape the data from webpage.