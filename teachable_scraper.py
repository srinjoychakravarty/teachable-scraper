# z0jgg5ruhx
# p6o181gqna
# j6jzy2wzv0
# 8epis4twlb
# xabpksl6ao
# fyjppx9n4g
# jq6sophhxz
# z9m2vuk8t3
# z48n09t7l7

import requests
from lxml import html
from bs4 import BeautifulSoup
import urllib.request

link_array = []
with open ('bitcoin.html', 'rt') as html_file:
	soup = BeautifulSoup(html_file, "lxml")
	for link in soup.findAll('a'):
	    link_array.append("https://ivanontech.teachable.com" + str(link.get('href')))
clean_list = link_array[12:]
r = urllib.request.urlopen(clean_list[9])
print(r)

with requests.Session() as s:
	login_url = "https://sso.teachable.com/secure/teachable_accounts/sign_in"
	headers = {'Host': 'sso.teachable.com', 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate, br', 'Content-Type': 'application/x-www-form-urlencoded', 'DNT': '1', 'Connection': 'keep-alive', 'Referer': 'https://sso.teachable.com/secure/teachable_accounts/sign_in', 'Cookie': '__cfduid=d2efd12d18090cd2b7ba4807ea4acca5d1564616531; __stripe_mid=1a23332a-3af7-4279-9a70-90d7a53582c1; ahoy_visitor=045e21a9-d182-47b3-bba9-2c3494f15c5c; ahoy_visit=7cf1afda-7d28-4ba4-a5cc-64fc75d903de; _session_id=cbae2ca8a08260053f13f5cddd54f5b8; ajs_user_id=25065448; ajs_group_id=null; ajs_anonymous_id=%22d6ce7f32-a7be-40f4-9a10-8605df7f5773%22; cf_clearance=4a664149d83cea9d35307468de73c5c95b648063-1564616662-31536000-150; __stripe_mid=1a23332a-3af7-4279-9a70-90d7a53582c1; __stripe_sid=18e3f1d1-46d3-40fd-83b3-54ec1e5df9e8; ahoy_events=%5B%7B%22id%22%3A%22164b9f7d-3ce1-46a5-8d39-f9b6dfe26915%22%2C%22name%22%3A%22%24view%22%2C%22properties%22%3A%7B%22url%22%3A%22https%3A//sso.teachable.com/secure/teachable_accounts/sign_in%22%2C%22title%22%3A%22myTeachable%22%2C%22page%22%3A%22/secure/teachable_accounts/sign_in%22%7D%2C%22time%22%3A1564620537.821%7D%5D', 'Upgrade-Insecure-Requests': '1', 'TE': 'Trailers'}
	r = s.get(login_url, headers=headers, verify=False)
	soup = BeautifulSoup(r.text, 'lxml')
	authenticity_token = soup.select_one('meta[name="csrf-token"]')['content']
	payload = {'utf8': '✓'} 
	payload.update({'authenticity_token' : authenticity_token})
	payload.update({'teachable_account[email]' : 'chakravarty.s@husky.neu.edu'})
	payload.update({'teachable_account[password]' : 'testing123'})
	payload.update({'commit' : 'Log+Into+myTeachable'})
	response = s.post(login_url, data=payload, headers=headers, verify=False)
	url = "https://sso.teachable.com/secure/teachable_accounts/profile"
	result = s.get(url, headers=headers, verify=False)
	print(result.content)
# session_requests = requests.session()


# headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}





# headers = {'host': 'sso.teachable.com',
# 'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
# 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
# 'accept-Language': 'en-US,en;q=0.5',
# 'accept-Encoding': 'gzip, deflate, br',
# 'content-Type': 'application/x-www-form-urlencoded',
# 'dnt': '1',
# 'connection': 'keep-alive',
# 'referer': 'https://sso.teachable.com/secure/teachable_accounts/sign_in',
# 'cookie': '__cfduid=d2efd12d18090cd2b7ba4807ea4acca5d1564616531; __stripe_mid=1a23332a-3af7-4279-9a70-90d7a53582c1; ahoy_visitor=045e21a9-d182-47b3-bba9-2c3494f15c5c; ahoy_visit=7cf1afda-7d28-4ba4-a5cc-64fc75d903de; _session_id=cbae2ca8a08260053f13f5cddd54f5b8; ajs_user_id=25065448; ajs_group_id=null; ajs_anonymous_id=%22d6ce7f32-a7be-40f4-9a10-8605df7f5773%22; cf_clearance=4a664149d83cea9d35307468de73c5c95b648063-1564616662-31536000-150; __stripe_mid=1a23332a-3af7-4279-9a70-90d7a53582c1; __stripe_sid=18e3f1d1-46d3-40fd-83b3-54ec1e5df9e8; ahoy_events=%5B%7B%22id%22%3A%22164b9f7d-3ce1-46a5-8d39-f9b6dfe26915%22%2C%22name%22%3A%22%24view%22%2C%22properties%22%3A%7B%22url%22%3A%22https%3A//sso.teachable.com/secure/teachable_accounts/sign_in%22%2C%22title%22%3A%22myTeachable%22%2C%22page%22%3A%22/secure/teachable_accounts/sign_in%22%7D%2C%22time%22%3A1564620537.821%7D%5D',
# 'upgrade-insecure-requests': '1',
# 'te': 'Trailers'}

#'Content-Length': '267' / '255',



# 
# "commit": "Log+Into+myTeachable"

# tree = html.fromstring(response.text)
# headers['cookie'] = '; '.join([x.name + '=' + x.value for x in response.cookies])
# headers['content-type'] = 'application/x-www-form-urlencoded'

# payload = {"utf8":"✓","teachable_account[email]":"chakravarty.s@husky.neu.edu","teachable_account[password]":"OnePlus92","commit":"Log+Into+myTeachable"}
# payload["authenticity_token"] = authenticity_token


# print(response.content)
# headers['cookie'] = '; '.join([x.name + '=' + x.value for x in response.cookies])

