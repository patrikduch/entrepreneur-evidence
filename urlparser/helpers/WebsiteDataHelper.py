from xml.etree import ElementTree
from xml.etree.ElementTree import fromstring, ElementTree
from bs4 import BeautifulSoup


class WebsiteDataHelper:

	@staticmethod
	def get_description(soup): # Get description from meta content
		import re
		desc = soup.findAll(attrs={"name": re.compile(r"description", re.I)}) 
		return desc[0]['content'] if desc else None

	@staticmethod
	def get_title(soup): # Get classic title from HTML not from meta content.
		title = soup.title.string
		return title if title else None

	@staticmethod
	def get_meta_title(soup): # Get title from meta content
		title = soup.find("meta",  property="og:title")
		return title["content"] if title else None

	@staticmethod 
	def process_url(url):

		import json
		import requests

		# Request processing
		headers = {'Content-Type': 'application/json'} # set what your server accepts
		response = requests.get('https://daomaker.com', headers=headers).text

		# HTML processing
		soup = BeautifulSoup(response)

		d = dict();
		d['title'] = WebsiteDataHelper.get_title(soup)
		d['metaTitle'] = WebsiteDataHelper.get_meta_title(soup)
		d['description'] = WebsiteDataHelper.get_description(soup)
		return d