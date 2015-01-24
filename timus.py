#!/usr/bin/env python

import sys, os, requests
from lxml import etree
from lxml.cssselect import CSSSelector

def main():
	problem_id = sys.argv[1]
	sel = CSSSelector('.sample')
	os.system("xdg-open http://acm.timus.ru/problem.aspx?space=1&num="+problem_id)
	if not os.path.exists(problem_id):
		os.makedirs(problem_id)
	res = requests.get("http://acm.timus.ru/problem.aspx?space=1&num="+problem_id)
	root = etree.fromstring(res.content, etree.HTMLParser())
	cnt = 0
	# for i in .getchildren()[1:]:
	
	for i in root.xpath('//table[last()]/tr[position()>1]/td/pre/text()'):
		if cnt%2==0:
			f = open(problem_id+"/in"+str(cnt/2),'w+')
			f.write(i)
			f.close()
		else:
			f = open(problem_id+"/out"+str(cnt/2), 'w+')
			f.write(i)
			f.close()
		cnt +=1
	f = open(problem_id+"/test.sh", "w+")
	f.write("#!/usr/bin/env bash \n")
	
	for i in range(cnt/2):
		f.write("./src < in"+str(i)+" > tempout\n")
		f.write("diff --strip-trailing-cr tempout out"+str(i)+"\n")
	f.close()
	
if __name__ == '__main__':
	main()