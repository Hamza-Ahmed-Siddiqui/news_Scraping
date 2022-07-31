from helperFunction import fetchMenuLinks, fetchLinks
from newspaper import Article


links = fetchMenuLinks('https://arynews.tv/', 'ul', 'tdb-block-menu tdb-menu tdb-menu-items-visible')
articles = []

for i in range(0, len(links)):
    if i == 0:
        articles.append(fetchLinks(links[i], 'h4', 'entry-title td-module-title'))
    # else:   
    #     articles.append(fetchLinks(links[i], 'h3', 'entry-title td-module-title'))
    
for articleLinks in articles:
    for article in articleLinks:
        
        a = Article(article)
        
        a.download()
        a.parse()
        a.nlp()
        print(a.title)
        print(a.keywords)
        print(a.summary)
        print(a.publish_date)

print(links)
print(articles)