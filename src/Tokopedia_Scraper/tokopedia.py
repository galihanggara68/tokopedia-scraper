import json

class LinkedInScraper:
    def __init__(self, driver, finder, cookie_path):
        self.driver = driver
        self.finder = finder
        self._load_cookie(cookie_path)
        
    def _load_cookie(self, path):
        with open(path, 'r') as cookiesfile:
            self.cookies = json.load(cookiesfile)
            
    def _apply_cookie(self):
        for cookie in self.cookies:
            self.driver.add_cookie(cookie)
        
    def exec_scraper(self):
        self.finder.load_mapping("json_scheme.json")
        
        self.driver.get("https://www.tokopedia.com")
        self.driver.maximize_window()
        self._apply_cookie()
        self.driver.refresh()
        self.finder.by_json_scheme()
        
    def get_data(self):
        return self.finder.get_mapped_data()