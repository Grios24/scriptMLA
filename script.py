import requests
import logging


id_seller=input('Ingrese el ID del vendedor: ')

logname='SELLER_'+id_seller+'.log'
id_cat=''

logging.basicConfig(filename=logname, level=logging.INFO, filemode='w')

url = "https://api.mercadolibre.com/sites/MLA/search?seller_id=% s" %(id_seller)
r = requests.get(url)

dic=r.json()

for i in dic:
	if i=='results':
		val=dic[i]

elementos={}

for j in val:
	for h in j:
		if h=='id':
			elementos[h]=j[h]
		if h=='title':
			elementos[h]=j[h]
		if h=='category_id':
			elementos[h]=j[h]
			id_cat=j[h]
			urlcat= 'https://api.mercadolibre.com/categories/% s' %(id_cat)
			r2= requests.get(urlcat)
			dic2=r2.json()
			for k in dic2:
				if k=='name':
					elementos[k]=dic2[k]
					logging.info(elementos)