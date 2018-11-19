# Amazon-Bin-Challenge
Count Number Of Bins In Amazon Pods Using Deep Learning

This project is based on the Amazon Bin Datasets Challenge: https://registry.opendata.aws/amazon-bin-imagery/

I have focused on the frist problem i.e. counting number of items in a pod from the images. I used the fastai library for my Image Classification.

## Getting The Data

Amazon has provided us with 500,000 images with metadata for this challenge. They are all available in public S3 bucket.
Getting the data for your Deep Learning project is often the hardest part.I have a script called download_data.py that will go through the Amazon dataset and download the images and metadata files in folders called 'images' and 'metadata' (these should be created first in the directory you run the python script from. 

The script is setup to take a start, stop and interval number to iterate through the data. Since there are 500,000 images you probably just want a sample of them to start with.
The default settings are start=500, stop=50000, interval=100 which will grab files ending with 500,600....49900.jpg.
You can change these settinsg to grab a different slice of the data.

The script will also create a 'labels.csv' file with the relevant labels for this challenge i.e. the number of items in each image.

Please note you will need to have installed awscli (and boto) for this script. You need to also provide an access and secret access key for awscli to be able to use s3. 
You can generate these from IAM on your AWS account and either pass them directly in the script or run 'aws' configure' and pass them to you awscli locally.
DO NOT commit or share any code that includes your access keys!

## The NoteBook
You can then run through the Jupyter notebook to train your model on this data.




