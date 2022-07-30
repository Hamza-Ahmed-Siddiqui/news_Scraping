
from newspaper import Article
import nltk



url = "https://www.bolnews.com/pakistan/2022/07/money-laundering-case-shehbaz-sharif-hamza-summoned-next-hearing/"

a = Article(url)

a.download()
a.parse()

a.nlp()
print(a.title)

print("\n \n \n\n\n\n\n\n\n")

print(a.keywords)

print(a.summary)


print(a.publish_date)