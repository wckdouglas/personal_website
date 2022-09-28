#!/usr/bin/env python

import matplotlib.pyplot as plt
import string
import re
import glob
import wordcloud
import pdftotext
import nltk
import string
from calendar import month_name
from nltk.corpus import stopwords
ENGLISH_STOP = set(stopwords.words('english'))

class research_wordcloud():
    '''
    Make word cloud from all PDF under a folder

    Usage:
    rs = research_wordcloud(paper_path)
    rs.extract_text()
    rs.filter_text()
    rs.generate_wordcloud(figurename)
    '''
    def __init__(self, paper_path):
        '''
        find all pdf under paper_path
        '''
        self.paper_path = paper_path
        self.PDFs = glob.glob(paper_path + '/*pdf')
        self.texts = ''
        self.tokens = None
        self.words = None
        self.paper_stop = ['fig','figure','supplementary', 'author','press',
                            'PubMed', 'manuscript','nt','et','al', 'laboratory',
                            'article','cold','spring','habor','harbor','Re',
                            'additional', 'additionalfile','additiona file']
        months = [month_name[i].lower() for i in range(1,13)]
        self.paper_stop.extend(months)
        self.paper_stop.extend(list(string.ascii_lowercase))
        self.paper_stop.extend(list(map(lambda x: x.capitalize(), self.paper_stop)))
        self.paper_stop = set(self.paper_stop)

    def extract_text(self):
        '''
        read pdf text
        '''
        for pdf_file in self.PDFs:
            with open(pdf_file, 'rb') as paper:
                pdf = pdftotext.PDF(paper)
                self.texts += "\n\n".join(pdf)

    def filter_text(self):
        '''
        remove stop words and punctuations
        '''
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        self.tokens = tokenizer.tokenize(self.texts)
        self.tokens =  nltk.pos_tag(self.tokens) #(tag the nature of each word, verb? noun?)

        self.words = []
        num_regex = re.compile('[0-9]+')
        for word, tag in self.tokens:
            IS_VERB = tag.startswith('V')
            IS_NOUN = tag.startswith('N') 
            IS_STOP = word in set(string.punctuation)
            IS_ENGLISH_STOP = word in set(ENGLISH_STOP)
            IS_WORDCLOUD_STOP = word in wordcloud.STOPWORDS
            IS_NUMBER = num_regex.search(word)
            IS_PAPER_STOP = word in self.paper_stop
            condition = [IS_VERB, IS_STOP, IS_ENGLISH_STOP, IS_WORDCLOUD_STOP, 
                    IS_NUMBER, IS_PAPER_STOP]
            if not any(condition) and IS_NOUN:
                if word == "coli":
                    self.words.append('E. coli')
                else:
                    self.words.append(word)
        self.words = ' '.join(self.words)

    def generate_wordcloud(self, figurename):
        '''
        plot
        '''
        wc = wordcloud.WordCloud(  
                collocations=False,
                background_color='white',
                max_words=200,
                max_font_size=40, 
                scale=3
        )
        try:
            wc.generate(self.words)
            fig = plt.figure(figsize=(10,8))
            ax = fig.add_subplot(111)
            ax.imshow(wc, interpolation="bilinear")
            ax.axis('off')
            fig.savefig(figurename, bbox_inches='tight', transparent=True)
            print('Written %s' %figurename)
        except ValueError:
            print(self.words)


if __name__ == '__main__':
    PAPER_PATH = '../paper'
    FIGURE_PATH = '../research_images'
    AREAS = glob.glob(PAPER_PATH + '/*')
    for area in AREAS:
        figure_name = FIGURE_PATH + '/' + area.split('/')[-1] + '.png'
        wc = research_wordcloud(area)
        wc.extract_text()
        wc.filter_text()
        print('Start plotting')
        wc.generate_wordcloud(figure_name)
