#usr/bin/python

# NLPiffy-CLI - Version 0.00
import click

# Misc Packages
import json
import time
from pyfiglet import Figlet

# NLP packages
import spacy
from textblob import TextBlob 
nlp = spacy.load('en')


# Save to file as text
def save_to_file(x):
	timestr = time.strftime("%Y%m%d-%H%M%S")
	filename = 'result' + timestr + '.txt'
	with click.open_file(filename, 'wb') as f:
		 f.write(x)


# Save to file as json
def sav