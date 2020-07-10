import crochet
from flask import Flask, render_template, jsonify
from scrapy import signals
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher
import time
from stack.stack.spiders.stack_spider import StackSpider
from stack.stack.spiders.tag_spider import TagSpider
from pymongo import MongoClient

crochet.setup()
app = Flask(__name__)

output_data = []  # last 50 questions
input_data = []  # all tags from last 50 questions
output_data2 = []  # tags that have more than 11 characters from last 50 questions

crawl_runner = CrawlerRunner()
URL_to_scrape = 'http://stackoverflow.com/questions?pagesize=50&sort=newest'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/scraped_data')
def scrape_question():
    global output_data
    output_data = []
    crochet_scrape_q(URL_to_scrape=URL_to_scrape)

    time.sleep(7)  # Time which spider scrapes data

    return jsonify(output_data)  # list -> json


@crochet.run_in_reactor
def crochet_scrape_q(URL_to_scrape):
    dispatcher.connect(question_result, signal=signals.item_scraped)
    scraped_data = crawl_runner.crawl(StackSpider, category=URL_to_scrape)

    return scraped_data


def question_result(item):
    conn = MongoClient('localhost', 27017)  # mongodb server
    db = conn['Questions']
    collection = db['questions']
    if 'name' in item:
        item['name'].pop()
    collection.insert(dict(item))
    output_data.append(dict(item))


@app.route('/scraped_tags')
def scrape_tag():
    global output_data2
    output_data2 = []
    crochet_scrape_t(URL_to_scrape=URL_to_scrape)

    time.sleep(7)

    return jsonify(output_data2)


@crochet.run_in_reactor
def crochet_scrape_t(URL_to_scrape):
    dispatcher.connect(tag_result, signal=signals.item_scraped)
    scraped_data = crawl_runner.crawl(TagSpider, category=URL_to_scrape)

    return scraped_data


def tag_result(item):
    conn = MongoClient('localhost', 27017)  # mongodb server
    db = conn['Questions']
    collection = db['tags']
    if len(item['name']) > 15:
        collection.insert(dict(item))
        output_data2.append(item['name'])
       


if __name__ == "__main__":
    app.run(debug=True)
