from flask import Flask, render_template, request
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import matplotlib.pyplot as plt
import os,shutil
import xlsxwriter
import numpy as np


class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''

    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'L4ROQj8rhzrJ269XOfdUlSh43'
        consumer_secret = 'WWReiZIgd8QwgPdiHZHMb84r4rulcVOw4uhUAOyotTC36DlAXu'
        access_token = '1163443965988724737-ivY7BvxXUiGf9ShpRCuIEvh3JIJsWD'
        access_token_secret = '46KVcnVm8zZ4XCASebwYNbVkDsrYVI1RRu9jm4Pg0I6dm'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q=query, count=count)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

                    # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))


def drawing():
    global all_figs
    print("\n")
    labels = ['Positive', 'Negative', 'Neutral']
    colors = ['yellowgreen', 'lightcoral', 'gold']
    for one_fig in all_figs:
        all_total = 0
        sentiments = {}
        sentiments["Positive"] = one_fig[0]
        sentiments["Negative"] = one_fig[1]
        sentiments["Neutral"] = one_fig[2]
        all_total = one_fig[0] + one_fig[1] + one_fig[2]
        sizes = []

        sizes = [sentiments['Positive'] / float(all_total), sentiments['Negative'] / float(all_total),
                 sentiments['Neutral'] / float(all_total)]

        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True)
        plt.axis('equal')

        plt.title('Sentiment for the word - ' + str(one_fig[3]) + "\n\n")
        fig_name = "pie_" + str(one_fig[3]) + ".png"
        # Save the figures
        plt.savefig(fig_name)
        plt.savefig('C:\\Users\\P.Harish Kumar\\Desktop\\Project twitter\\static\\pie_images\\'+fig_name)
        plt.close()
        
def drawing1():
    global all_figs
    print("\n")
    objects = ('Positive', 'Negative', 'Neutral')
    for one_fig in all_figs:
        all_total = one_fig[0] + one_fig[1] + one_fig[2]
        sentiments = []
        sentiments.append(100*one_fig[0]//all_total)
        sentiments.append(100*one_fig[1]//all_total)
        sentiments.append(100*one_fig[2]//all_total)
        y_pos = np.arange(len(objects))

        plt.bar(y_pos, sentiments, align='center', alpha=0.5) 
        plt.xticks(y_pos, objects)
        plt.ylabel('Percentage %')
        

        plt.title('Sentiment for the word - ' + str(one_fig[3]) + "\n\n")
        fig_name = "bar_" + str(one_fig[3]) + ".png"
        # Save the figures
        plt.savefig(fig_name)
        plt.close()


def zippy():
    dest='C:\\Users\\P.Harish Kumar\\Desktop\\Project twitter\\t_ana'

    shutil.make_archive(dest, 'zip', dest)


def movef(word):
    source='C:\\Users\\P.Harish Kumar\\Desktop\\Project twitter\\'
    directory = 'C:\\Users\\P.Harish Kumar\\Desktop\\Project twitter\\t_ana\\'+word
    os.mkdir(directory)
    files = os.listdir(source)
    for f in files:
        if word+'.png' in f or word+'.txt' in f or word+'.xlsx' in f:
            shutil.move(source+f, directory)
        




def xlchart(i, a, b, c, d):
    # Workbook() takes one, non-optional, argument
    # which is the filename that we want to create.
    workbook = xlsxwriter.Workbook('pie_' + i + '.xlsx')

    # The workbook object is then used to add new
    # worksheet via the add_worksheet() method.
    worksheet = workbook.add_worksheet()

    # Create a new Format object to formats cells
    # in worksheets using add_format() method .

    # here we create bold format object .
    bold = workbook.add_format({'bold': 1})

    # create a data list .
    headings = ['Tweet :-', i]

    data = [
        ['Postive% :-', 'Negative% :-', 'Neutral% :-'],
        [a, b, c],
    ]

    # Write a row of data starting from 'A1'
    # with bold format .
    worksheet.write_row('A1', headings, bold)

    # Write a column of data starting from
    # A2, B2, C2 respectively.
    worksheet.write_column('A2', data[0], bold)
    worksheet.write_column('B2', data[1])

    # Create a chart object that can be added
    # to a worksheet using add_chart() method.

    # here we create a pie chart object
    chart2 = workbook.add_chart({'type': 'pie'})

    # Add a data series to a chart
    # using add_series method.

    # Configure the first series.
    # = Sheet1 !$A$1 is equivalent to ['Sheet1', 0, 0].
    chart2.add_series({
        'name': 'Sentimental Ananlysis for ' + i,
        'categories': ['Sheet1', 1, 0, 3, 0],
        'values': ['Sheet1', 1, 1, 3, 1],
        'points': [
            {'fill': {'color': '#5ABA10'}},
            {'fill': {'color': '#FE110E'}},
            {'fill': {'color': '#FFFF00'}},
        ],
    })

    # Add a chart title.
    chart2.set_title({'name': 'Sentimental Ananlysis for-' + i + ' in last ' + str(d) + ' tweets'})

    # Insert the chart into the worksheet (with an offset)
    # the top-left corner of a chart is anchored to cell C2.
    worksheet.insert_chart('C2', chart2, {'x_offset': 50, 'y_offset': 15})

    workbook.close()


def delete():
    directory = 'C:\\Users\\P.Harish Kumar\\Desktop\\Project twitter\\t_ana\\'
    file_paths = os.listdir(directory)
    for file in file_paths: 
        shutil.rmtree(directory+file)
        
def delete1():
    directory = 'C:\\Users\\P.Harish Kumar\\Desktop\\Project twitter\\static\\pie_images\\'
    file_paths = os.listdir(directory)
    for file in file_paths: 
        os.remove(directory+file)


def textw(word):
    global ptweets, ntweets, tweets
    new_path = 'C:\\Users\\P.Harish Kumar\\Desktop\\Project twitter\\' + word + '.txt'
    tw = open(new_path, 'w', encoding="utf-8")

    tw.write("\n\nPositive tweets percentage: " + str(100 * len(ptweets) / len(tweets)))
    tw.write("\nNegative tweets percentage: " + str(100 * len(ntweets) / len(tweets)))
    tw.write("\nNeutral tweets percentage: " + str(100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets)))

    tw.write("\n\nPositive tweets:\n\n")
    for tweet in ptweets[:10]:
        tw.write("->" + str(tweet['text']) + "\n\n")

    tw.write("\n\nNegative tweets:\n\n")
    for tweet in ntweets[:10]:
        tw.write("->" + str(tweet['text']) + "\n\n")

    tw.write("\n\nNeutral tweets:\n\n")
    tweetr = [tweet for tweet in tweets if tweet['sentiment'] != 'positive' and tweet['sentiment'] != 'negative']
    for tweet in tweetr[:10]:
        tw.write("->" + str(tweet['text']) + "\n\n")

    tw.close()


def main_fun(astr, icnt):
    global all_figs, ptweets, ntweets, tweets
    details=[]
    # creating object of TwitterClient Class
    api = TwitterClient()
    search_words = astr
    k=0
    Total_tweet_count = icnt
    total=[]
    # print search_words
    search_words_list = search_words.split(",")
    for i in search_words_list:
        print("\nFor Tweet of \"", i, "\" :- \n")
        tweets = api.get_tweets(query=i, count=Total_tweet_count)

        # picking positive tweets from tweets
        ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
        # percentage of positive tweets
        print("Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets)))
        # picking negative tweets from tweets
        ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
        # percentage of negative tweets
        print("Negative tweets percentage: {} %".format(100 * len(ntweets) / len(tweets)))
        # percentage of neutral tweets
        print("Neutral tweets percentage: {} %".format(100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets)))

        # printing first 5 positive tweets
        xlchart(i, (100 * len(ptweets) / len(tweets)), (100 * len(ntweets) / len(tweets)),
                (100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets)), Total_tweet_count)
        draw_helper = []
        draw_helper.append(len(ptweets))
        draw_helper.append(len(ntweets))
        draw_helper.append(len(tweets) - len(ntweets) - len(ptweets))
        draw_helper.append(i)
        details.append([i,k,(len(ptweets)),(len(ntweets)),((len(tweets) - len(ntweets) - len(ptweets)))])
        all_figs = [draw_helper]
        total.append(len(tweets))
        drawing()
        drawing1()
        # for writing into a text file
        textw(i)
        movef(i)
        k=k+1
    zippy()
    delete()
    return(details,len(details),total)


app = Flask(__name__)


@app.route('/')
def index():
    delete1()
    return render_template('index.html')


@app.route('/main_p')
def main_p():
    tweet = request.args.get('tweet_w')
    details,length,total=main_fun(str(tweet), 100)
    #time.sleep(3)
    return render_template('main_p.html', details=details,length=length,total=total)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('sorry.html'), 404


if __name__ == '__main__':
    app.run(debug=True)



