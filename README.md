# Tokopedia Scraper

## Intro

This package is using [`Selenium Finder`](https://github.com/galihanggara68/selenium-finder) library as engine for scrape datas from Tokopedia webpage(Pre Login)

## Usage

### Clone or Install from pip

Clone this repo to your current directory

> git clone https://github.com/galihanggara68/tokopedia-scraper.git

or install using pip

> pip3 install git+https://github.com/galihanggara68/tokopedia-scraper.git@master

### Import library

First of all import Tokopedia class

```
from Tokopedia_Scraper.tokopedia import TokopediaScraper
```

### Using Finder class

`Tokopedia` class has 3 parameters `driver` the Selenium WebDriver, `finder` a Finder object, and `cookie_path` a path of cookie json for login to Tokopedia

```
from selenium import webdriver

driver = webdriver.Chrome()

# global_wait default 10 second
# iterable_each_wait default 1 second
options = {"global_wait": 10, "iterable_each_wait": 2}
finder = Finder(driver, options)

# create TokopediaScraper instance
ld = TokopediaScraper(driver, finder, "www.tokopedia.com.cookies.json")

# start scraping
ld.exec_scraper()

# get the result
print(ld.get_data())

```

## TokopediaScraper methods

### exec_scraper()

execute scraper

### get_data()

get scraped result
