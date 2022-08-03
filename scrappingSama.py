from helperFunction import fetchMenuLinks, fetchLinks
from newspaper import Article

samaLinks = fetchMenuLinks('https://www.samaaenglish.tv/', 'nav', 'relative font-sans container whitespace-nowrap flex')
samaArticles = []



# for i in range(0, len(samaLinks)):
#     if i == 0:
#         samaArticles.append(fetchLinks(samaLinks[i], 'h2', 'story_title'))
    # else:   
     #    samaArticles.append(fetchLinks(samaLinks[i], 'h3', 'entry-title td-module-title'))
    
# for articleLinks in samaArticles:
#     for articlee in articleLinks:
        
#         b = Article(articlee)
        
#         b.download()
#         b.parse()
#         b.nlp()
#         print(b.title)
#         print(b.keywords)
#         print(b.summary)
#         print(b.publish_date)

print(samaLinks)
print(samaArticles)