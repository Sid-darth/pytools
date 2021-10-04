
from icecream import ic
from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/news"
response = requests.get(url)
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')

article_tag = soup.find(name="a", class_="storylink")
article_link = article_tag.get("href")
article_upvote = soup.find(name="span",class_="score").getText()    

# ic(article_tag,article_link,article_upvote)

# all tags
article_tags = soup.find_all(name="a", class_="storylink") 
# all upvotes
article_upvotes = [int(score.getText().split()[0])  for score in soup.find_all(name="span", class_="score")]
# all links
article_links = [tag.get("href") for tag in article_tags]
# ic(article_tags,article_upvotes,article_links)

max_index = article_upvotes.index(max(article_upvotes))
ic(max_index)
highest_article = {article_tags[max_index].getText():{'link':article_links[max_index], 'upvotes':article_upvotes[max_index]}}

ic(highest_article)


