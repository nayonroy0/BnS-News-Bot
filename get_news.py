#! usr/bin/env python3
import sys, requests, bs4, datetime, tomd, extras

def main():
	tmp = get_news()
	if tmp:
		print(tmp[0])
	else:
		print("no news returned")

def get_news():
	page = requests.get("https://www.bladeandsoul.com/uk/news/")
	soup = bs4.BeautifulSoup(page.text, 'html.parser')
	news_article_list = soup.find(class_="news-article-list").find_all('a')
	#for e in news_article_list:
	#	print(e.encode('utf-8'))

	for a in news_article_list:
		link = "https://www.bladeandsoul.com"+a['href']
		date_posted = a.find('span').get_text().split('|')[0].split(',')[0].strip()
		curr_day = str(datetime.datetime.now().day)
		if date_posted.split()[1] == (curr_day if len(curr_day) == 2 else '0' + curr_day):
			return [extract_news(link), link]
	return []

def extract_news(link):
	page = requests.get(link)
	soup = bs4.BeautifulSoup(page.text, 'html.parser')
	article_html = soup.select(".article")[0]
	article = str(article_html.encode('utf-8'))
	md = ''.join(tomd.convert(article).replace("\\n", "\n").replace("\\xc2", "").replace("\\xa0", "").replace("\n\n\n", "\n").replace("\n\n", "\n").replace("\\xe2\\x80\\x99", "'").split("|"))
	md = md.replace("\\xe2", "").replace("\\x86", "").replace("\\x92", "").replace("\\x80", "").replace("\\93", "")
	md = extras.get_links(md)

	return(md)

if __name__ == "__main__":
	main()