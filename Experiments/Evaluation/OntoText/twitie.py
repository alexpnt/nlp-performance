#!/usr/bin/env python2
# -*- coding: utf-8 -*

from __future__ import division


import argparse,os,sys
import json
import requests

key = 's4l07b19v3tq'
secret = 'mll1unh9kh57erh'
endpoint = "https://text.s4.ontotext.com/v1" #service endpoint url
service = "/twitie" #name of the service 

def twitie_analytics(finput):

	with open(finput) as f:
		corpora = f.readlines()

	print "Pinging .."
	req = requests.get(endpoint, auth=(key, secret))
	print req.content.decode('utf-8')
	print ('Request Code: {}\n'.format(req.status_code))

	results=[]
	counter=0
	n_lines=len(corpora)
	for line in corpora:
		# Prepare the data
		annotations = [":Person",":Location",":Organization",":Token"]
		data = {
		    "document": line,
		    "documentType": "text/plain",
		    "annotationSelectors": annotations
		}
		json_Input = json.dumps(data)
		headers = {
			'Accept': "application/json",
			'Content-type': "application/json",
			'Accept-Encoding': "gzip",
		}

		#send request
		req = requests.post(endpoint+service, headers=headers,data=json_Input, auth=(key,secret))

		output=json.loads(req.content.decode('utf-8'))
		annotations=output[u'entities']
		pos = [[i[u'string'].encode('utf8', 'ignore'), i[u'category'].encode('utf8', 'ignore')] for i in annotations[u'Token']]
		
		entities=[False,False,False]
		try:
			entities[0] = [[line[i[u'indices'][0]:i[u'indices'][1]], i[u'type'].encode('utf8', 'ignore')] for i in annotations[u'Organization']]
			# print entities[0]
		except Exception, e:
			pass

		try:
			entities[1] = [[line[i[u'indices'][0]:i[u'indices'][1]], i[u'type'].encode('utf8', 'ignore')] for i in annotations[u'Location']]
			# print entities[1]
		except Exception, e:
			pass

		try:
			entities[2] = [[line[i[u'indices'][0]:i[u'indices'][1]], i[u'type'].encode('utf8', 'ignore')] for i in annotations[u'Person']]
			# print entities[2]
		except Exception, e:
			pass

		twitie_pos_results=open(finput.split("/")[-1]+"_pos_annotated.txt","a")
		twitie_ner_results=open(finput.split("/")[-1]+"_ner_annotated.txt","a")
		for token_pos in pos:
			twitie_pos_results.write(token_pos[0]+" "+token_pos[1]+"\n")
			tag_none=True
			for ent in entities:
				if ent and tag_none:
					for token_ner in ent:
						if token_ner[0]==token_pos[0]:
							if token_ner[1]=='Organization':
								twitie_ner_results.write(token_pos[0]+" ORG"+"\n")
							elif token_ner[1]=='Location':
								twitie_ner_results.write(token_pos[0]+" LOC"+"\n")
							else:
								twitie_ner_results.write(token_pos[0]+" PER"+"\n")
							tag_none=False
							break
			if tag_none:
				twitie_ner_results.write(token_pos[0]+" O"+"\n")


		twitie_pos_results.write("\n")
		twitie_ner_results.write("\n")
		twitie_pos_results.close()
		twitie_ner_results.close()



		counter+=1
		print "Progress: ",str(counter)+"/"+str(n_lines),str(float(counter/n_lines)*100)+" %"	
	

	 

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='TwitIE ',epilog="NLP with TwitIE.\n Each input file is a collection of sentences.\nEach line has a sentence or a set of sentences")
	parser.add_argument("-i","--input",nargs=1,help="Input filename",required=True)


	args=vars(parser.parse_args())
	finput=args['input'][0]

	if not os.path.isfile(finput): 
		print "File",freference,"not found"
		sys.exit() 

	twitie_analytics(finput)





