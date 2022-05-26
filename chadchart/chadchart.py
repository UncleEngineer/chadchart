# matichon.py

from urllib.request import urlopen
from bs4 import BeautifulSoup


class Policy:
	'''
	--------------Example--------------
	from chadchart import Policy
	policy = Policy()
	policy.show_all()
	print('All policy:',policy.all)
	print('-----')
	print('Number 1 (dictionary):', policy.number(1))
	print('Number 1 (thai):',policy.number(1)['thai'])
	print('Number 1 (english):',policy.number(1)['english'])
	print('Number 1 (tag):', policy.number(1)['tag'])
	print(policy.all_tag)
	print(policy.all_tag['เรียนดี'])
	policy.show_category()
	policy.category('ปลอดภัยดี')
	policy.credit()
	policy.developer()
	-----------------------------------
	'''

	def __init__(self):
		self.all = {}
		self.base_url = 'https://www.chadchart.com'
		self.all_tag = {}
		self.get_policy()
		self.gen_category()
		

	def get_policy(self):
		url = self.base_url + '/policy'

		webopen = urlopen(url)
		pagehtml = webopen.read().decode('utf-8')
		webopen.close()

		data = BeautifulSoup(pagehtml,'html.parser')
		title = data.find('div',{'class':'list-card-wrap mt-20px'}) #หลายหัวข้อออกมาเป็นลิสต์
		link = title.find_all('a')

		for i,l in enumerate(link,start=1):

			th = l.find_all('div')[1].text.strip()
			en = l.find_all('div')[2].text.strip()

			tag = []
			taglist = l.find_all('div')[3].text.strip().split(' ')
			for t in taglist:
				#print('T',[t])
				if t != '' and t != '\n':
					tag.append(t.strip())
			
			self.all[i] = {'id':i, 'thai':th, 'english':en, 'tag':tag}


	def number(self,number,show=False):
		try:
			if show:
				print(self.all[number])
			return self.all[number]
		except:
			print('Not found number:',number)
			print('Number range: 1-214')

	def gen_category(self):
		res = {}
		for pol in self.all.values():
			for t in pol['tag']:
				if t not in res and t != '+1':
					res[t] = [pol]
				elif t == '+1':
					res['เดินทางดี'] = [pol]
				else:
					if t == '+1':
						res['เดินทางดี'].append(pol)
					else:
						res[t].append(pol)
		self.all_tag = res
	

	def show_category(self):
		print('-----tag-----')
		for c in self.all_tag:
			print(c)
		print('-------------')

	def category(self,tag,showall=False,show_cat=False):
		if show_cat:
			self.show_category()

		if tag in self.all_tag:
			print('-------นโยบายด้าน: {}-------'.format(tag))
			for c in self.all_tag[tag]:
				if showall:
					print(c)
				else:
					print(c['id'], c['thai'])
		else:
			print('Not found: ',tag)


	def show_all(self,showall=False):
		print('---------นโยบายทั้งหมด 214 ข้อ---------')
		for a in self.all.values():
			if showall:
				print(a)
			else:
				print('{} : {}'.format(a['id'],a['thai']))

	def credit(self):
		print('Data from: {}'.format(self.base_url))

	def developer(self):
		print('developer: https://www.facebook.com/UncleEngineer')

if __name__ == '__main__':
	policy = Policy()
	policy.show_all()
	print('All policy:',policy.all)
	print('-----')
	print('Number 1 (dictionary):', policy.number(1))
	print('Number 1 (thai):',policy.number(1)['thai'])
	print('Number 1 (english):',policy.number(1)['english'])
	print('Number 1 (tag):', policy.number(1)['tag'])
	print(policy.all_tag)
	print(policy.all_tag['เรียนดี'])
	policy.show_category()
	policy.category('ปลอดภัยดี')
	policy.credit()
	policy.developer()
	
	
	