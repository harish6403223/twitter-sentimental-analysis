# twitter-sentimental-analysis
AIMS AND OBJECTIVES
Main aim of this project is to design a website in which a user can directly input his/her access keys of developer accounts and queries. The work of our website is to extract sentiments from twitter for users and express them in a very efficient way for social media monitoring, companies, etc to get the opinion of wider public.

SUMMARY
Sentiment analysis refers to the class of computational and natural language processing-based techniques used to identify, extract or characterize subjective information, such as opinions, expressed in a given piece of text. In this project, we had used flask(python) framework for a local hosting of a website and private details of the client local SQLalchemy database was used which is a  part of flask. For the extraction of the tweets TextBlob is used and for interaction with the client Jinja extensions, HTML, CSS templates are used. The half phase of the project is developed in such a way that many of the sentiments in terms of topics will be compared and output will be in the form of charts with the help of canvas and google charts and with downloadable content.


PROJECT DESCRIPTION
This project has been developed in Python (Flask-framework) on a local server. It has many phases which has been described below: -

1.	Extraction phase : For the extraction of the sentiments from twitter we had used tweepy API for authorisation of the keys and also for the extraction of the tweet texts and TextBlob which is used for NLP tasks for making polarities of the tweet texts and by regular expressions with the help of ‘re’ package.

2.	The Database: All the keys are private to respected clients. So, for storing the unique keys and for storing the account information related to the unique user id of the client from flask package, sqlalchemy module is used.

3.	Jinja extensions: Not only in the ‘py’ files but also to write code in HTML and CSS files, jinja extensions help in a great manner and to manipulate the tags with the python code.

4.	Xlswriter: In this project, xlswriter is one of the major parts in this project used for downloadable content files like xls, chart etc.

5.	The View of Outcome: In this project,the outcome compared sentiment topics will be displayed in the webpage using bar, pie and line graphs with the help of the canvas and google charts and a downloadable is also available in the proper zip folder.

6.	Polarities:  The sentiments extracted for a topic from twitter has been set to 100. This has been differentiated into 5 categories based on the polarities like (-infinity, -2, 0, 2, +infinity).




Methodology to be adopted

The development models used as part of the project development was the Evolutionary Development Model (Software Engineering and Development) when the requirements were fixed at the early stage of the development. Under this model, the application is divided into a set of features. All basic functionalities were released at first and gradually we were creating the features and adding it to the applications. As we proceed further with the development of the software based on the requirements, we will shift to the Agile Software Development Technique as the end-product is a having a very high-quality software. In this Agile software development, a group of software methodologies based on iterative and evolutionary models is invoked, where requirements and solutions evolve through collaboration between self-organizing cross-functional teams. Agile processes generally promote a disciplined project management process that encourages frequent inspection and adaptation, a leadership philosophy that encourages teamwork, self-organization and accountability, a set of engineering best practices intended to allow for rapid delivery of high-quality software, and a business approach that aligns development with customer needs and our goals. 

Expected Outcome

The Present project works on the Development server running on localhost at port no. 5000 with the help of flask app. When the code runs successfully the  following pages will be loaded :-
1. The client home page: The index page is to be served at first whenever a client wants to access our website by sending the request packets by connecting himself to the network. The functionalities provided here are the navigation bar to different tabs such as contact information etc; Sign In which has a field of Username and Password; Sign Up which has a field like Username, Email, Password, Confirm Password. 
2. The landing page: After the Sign In or signup is done by the client, the email of the client is set to the session so that we can have a track of the clients in other pages too. Without signing in the user will not be able to navigate to the URLs which are secured or containing the main functionality of our application. We have given two functionalities i.e., Tweet form and Tweet search.
3. The Tweet Form page: If we choose and click the tweet form button on the landing page then it will render the user/client to the tweet form page where he/she has to input the Consumer key, Consumer secret key, Access token and access token secret key in order to extract the data from twitter.
4. The Sentiment Extraction Page: once the twitter credentials are entered and verified correctly, then the user will be redirected to the Sentiment Extraction Page where he/she will be given the search bar where he/she can write and search for multiple topics separated by comma.
5. The Result Page: after entering the topics I the sentiment extraction page and submit that to the server, in backend the whole analysis is done by fetching 100 tweets per topic, one by one all the sentiments will be analysed, and combined outcome will served in this page. The results contain the graphs like pie chart, bar chart and line chart by using the canvas and google charts for better interactivity for the user from where the user can compare all the sentiments and stored in the user directory present in our server. We have also provided a button to download the results. Logout options are provided in each page covered from point no. 2 to 5.




FUTURE CHANGES
1.	A proper database for the users for saving the analysis of the sentiments and detailed information of the client.
2.	More work on the web frameworks. We will design the pages and the web application with more efficient manner such that the overall performance increases by using the JavaScript, JQuery, AJAX.
3.	Now we are using google analytics visualization library for creating the visualized graphs but in the next phase of our project we will make use of HighChartJS.
4.	Saving the history of the users last time activities and give a functionality to have a look on it.
5.	Lastly when everything is done properly we will make use of android web-view to embed our project into an android application.
