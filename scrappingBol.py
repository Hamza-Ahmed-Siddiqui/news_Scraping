from helperFunction import fetchMenuLinks, fetchLinks
from newspaper import Article

bolArticles = []

links = fetchLinks('https://www.bolnews.com/?s=imran+khan', 'div', 'post-box sty27 mb-20')

article = Article(links[0])
article.download()
article.parse()
    
print(article.authors)
print(article.publish_date)
print(article.title)
print(article.summary)
print(article.top_image)

# for link in links:
#     article = Article(link)
#     article.download()
#     article.parse()
    
#     print(article.authors)
#     print(article.publish_date)
#     print(article.title)
#     print(article.text)
#     print(article.top_image)

print(bolArticles)


# fflex topmenu
# h6
# title