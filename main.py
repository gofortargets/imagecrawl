from icrawler.builtin import BaiduImageCrawler, BingImageCrawler, GoogleImageCrawler
ROOT_DIR ='./downloads'
import os
def Query(query, verb, google=True,google_year=1, bing=True, baidu=True):
    SAVE_DIR = os.path.join(ROOT_DIR, verb)
    # SAVE_DIR = os.path.join(ROOT_DIR, query)
    if google:
        google_crawler = GoogleImageCrawler(
            feeder_threads=1,
            parser_threads=1,
            downloader_threads=4,
            storage={'root_dir': os.path.join(SAVE_DIR, 'Google')})
        now_year = 2018
        for past_year in range(google_year):
            from_year = now_year - past_year
            filters = dict(
                license='noncommercial,modify',
                date=((from_year, 1, 1), (from_year, 12, 30)))
            google_crawler.crawl(keyword=query,
                                 filters=filters,
                                 max_num=1000,
                                 file_idx_offset='auto')

    if bing:
        bing_crawler = BingImageCrawler(downloader_threads=4,
                                        storage={'root_dir': os.path.join(SAVE_DIR, 'Bing')})
        filters_bing = dict(
            # size='large',
            # color='orange',
            license='noncommercial,modify')
        bing_crawler.crawl(keyword=query, filters=filters_bing, offset=0, max_num=1000)

    if baidu:
        baidu_crawler = BaiduImageCrawler(storage={'root_dir': os.path.join(SAVE_DIR, 'Baidu')})
        baidu_crawler.crawl(keyword=query, offset=0, max_num=1000)

places = ['restaurant', 'pub', '', 'coffee shop', 'public', 'home']
verbs = ["Serving", "Cutting", "Cooking", "Drinking", "Eating", "Riding ", "Playing", "Singing", "Reading", "Writing", "Using ", "Showing ", "Raising ", "Photographing", "Speaking", "Planting", "Shovelling", "Examining", "Operating", "Hitting", "Kicking", "Throwing", "Bouncing"]

for verb in verbs:
    verb = verb.lower()
    print ('Now querying', verb, '...')
    for place in places:
        query = 'people ' + verb + ' ' + place
        print ('Query =', query)
        Query(query, verb, google_year=3, bing=False, baidu=False)