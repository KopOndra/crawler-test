FROM python:3.8

# Install
RUN pip install scrapy
RUN pip install psycopg2
RUN pip install django

# Copy the crawler
COPY . /sreality_crawler
COPY . /crawl_result

# Set the working directory
WORKDIR /sreality_crawler/sreality_crawler