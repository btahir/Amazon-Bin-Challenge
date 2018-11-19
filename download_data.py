import boto3
import botocore
import json
import pandas as pd
import pprint

def get_images(start, stop):

	missing_img = []

	for i in range(start,stop, 100):
		try:
		    s3.Bucket(BUCKET_NAME).download_file('bin-images/'+str(i)+'.jpg', 'images/'+str(i)+'.jpg')
		except botocore.exceptions.ClientError as e:
		    # print(str(i)+'.jpg' + ' does not exist.')
		    missing_img.append(str(i)+'.jpg')

	print("Missing Files: ", missing_img)
	print("Total Missing: ", len(missing_img))
	return missing_img		

def get_metadata(start, stop):

	missing_meta = []

	for i in range(start,stop, 100):
		try:
		    s3.Bucket(BUCKET_NAME).download_file('metadata/'+str(i)+'.json', 'metadata/'+str(i)+'.json')
		except botocore.exceptions.ClientError as e:
		    # print(str(i)+'.json' + ' does not exist.')
		    missing_meta.append(str(i)+'.json')

	print("Missing Files: ", missing_meta)
	print("Total Missing: ", len(missing_meta))
	return missing_meta		


def get_labels(start, stop):

	data_list = []
	labels = ['file', 'quantity']

	for i in range(start, stop, 100):
		try:
			with open('metadata/'+str(i)+'.json') as data_file:    
			    data = json.load(data_file)
			    quantity = data['EXPECTED_QUANTITY']
			data_list.append((str(i), quantity))
		except:
			"object not added to csv"

	df = pd.DataFrame.from_records(data_list, columns=labels)
	df.to_csv('labels.csv', index=False)


if __name__ == "__main__":

	s3 = boto3.resource('s3', aws_access_key_id='', aws_secret_access_key= '')
	BUCKET_NAME = 'aft-vbi-pds'
	start = 500
	stop = 50000

	# # get images
	#get_images(start, stop)

	# # get metadata
	#get_metadata(start, stop)

	# get labels
	get_labels(start, stop)

























