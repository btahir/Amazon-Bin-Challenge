# Amazon-Bin-Challenge
Count Number Of Bins In Amazon Pods Using Deep Learning

This project is based on the Amazon Bin Datasets Challenge: https://registry.opendata.aws/amazon-bin-imagery/

I have focused on the first problem i.e. counting number of items in a pod from the images. I used the fastai library for my Image Classification: https://github.com/fastai/fastai

## Getting The Data

Amazon has provided us with 500,000 images with metadata for this challenge. They are all available in a public S3 bucket.
Getting the data for your Deep Learning project is often the hardest part.I have a script called download_data.py that will go through the Amazon dataset and download the images and metadata files in folders called 'images' and 'metadata' (these should be created first in the directory you run the python script from. 

The script is setup to take a start, stop and interval number to iterate through the data. Since there are 500,000 images you probably just want a sample of them to start with. I have set it up initially to pick every 100th image from a subset of the data. The reason you probably don't want to grab a whole block is that the data seems to be orderded with the same number of items grouped together e.g. images 500-599 will all have 2 items. Grabbing every nth item will give you a more varied training dataset.

The default settings are start=500, stop=50000, interval=100 which will grab files ending with 500,600....49900.jpg.
You can change these settings to grab a different slice of the data.

![alt text](https://github.com/btahir/Amazon-Bin-Challenge/blob/master/show_batch.jpg)

The script will also create a 'labels.csv' file with the relevant labels for this challenge i.e. the number of items in each image.

![alt text](https://github.com/btahir/Amazon-Bin-Challenge/blob/master/labels.jpg)

Please note you will need to have installed awscli (and boto) for this script. You need to also provide an access and secret access key for awscli to be able to use s3. 
You can generate these from IAM on your AWS account and either pass them directly in the script or run 'aws' configure' and pass them to you awscli locally.
DO NOT commit or share any code that includes your access keys!

## The NoteBook
You can then run through the Jupyter notebook to train your model on this data.

![alt text](https://github.com/btahir/Amazon-Bin-Challenge/blob/master/prediction.jpg)


