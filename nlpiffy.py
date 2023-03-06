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
def save_to_json(x):
	timestr = time.strftime("%Y%m%d-%H%M%S")
	filename = 'result' + timestr + '.txt'
	with click.open_file(filename, 'wb') as f:
		json.dump(x, f, indent=4, sort_keys=True)



@click.group()
@click.version_option(version='0.00',prog_name='NLPiffy CLI')
def main():
	""" NLPiffy CLI """
	
	pass


# Tokenization 
@main.command()
@click.argument('text')
@click.option('--tokentype',help="Specify Type of Tokenization -Word Tokens or Sentence Tokens")
@click.option('--save','-s')
def tokens(text,tokentype,save):
	""" Tokenization Using TextBlob """
	raw_text = TextBlob(text)
	final_result = raw_text
	if tokentype == 'word' and save =='True':
		click.secho('Your text was: {}'.format(text),fg='yellow')
		click.secho('Word Tokens: {}'.format(final_result.words),fg='green')
		save_to_json(str(final_result.words))

	elif tokentype == 'sentence' and save =='True':
		click.secho('Your text was: {}'.format(text),fg='yellow')
		click.secho('Sentence Tokens : {}'.format(final_result.sentences),fg='green')
		save_to_json(str(final_result.sentences))
	else:
		if tokentype == 'word':
			click.secho('Your text was: {}'.format(text),fg='yellow')
			click.secho('Word Tokens: {}'.format(final_result.words),fg='green')
		elif tokentype == 'sentence':
			click.secho('Your text was: {}'.format(text),fg='yellow')
			click.secho('Sentence Tokens : {}'.format(final_result.sentences),fg='green')
		else:
			click.secho('Your text was: {}'.format(text),fg='yellow')
			click.secho('Word Tokens: {}'.format(final_result.words),fg='green')

			# To Be Refactored
	# if save == 'True':
	# 	if tokentype == 'word':
	# 		click.secho('Your text was: {}'.format(text),fg='yellow')
	# 		click.secho('Word Tokens: {}'.format(fina