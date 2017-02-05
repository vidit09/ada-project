# Swiss on Reddit
## Abstract
In this project, we aim to explore the Reddit dataset to get insights into topics discussed in Switzerland and other countries in Europe.
The initail plan was to visualise the main discussion topics in Switzerland over the years, perform sentiment analysis on the comments and to generate a Subreddit simulator. However after the discussion at December checkpoint, it was decided that both sentiment analysis and Subreddit simulator would not give reliable results. As a result, The objectives of the project was changed to the following:

1. Growth in Reddit usage in Switzerland, UK, Germany, France, Spain and Italy.
2. Topic modeling and evolution of topics over time in the above countries
3. Interaction among users and their contributions to discussions in different subreddits.


## Data description
1. Obtained from: https://www.reddit.com/r/datasets/comments/3bxlg7/i_have_every_publicly_available_reddit_comment/
2. Size: ~ 1.7 Billion JSON objects
3. Fields:  Better see it with an example!
```
{
   "gilded": 0,
   "author_flair_text": "Male",
   "author_flair_css_class": "male",
   "retrieved_on": 1425124228,
   "ups": 3,
   "subreddit_id": "t5_2s30g",
   "edited": false,
   "controversiality": 0,
   "parent_id": "t1_cnapn0k",
   "subreddit": "AskMen",
   "body": "I can't agree with passing the blame, but I'm glad to hear it's at least helping you with the anxiety.",
   "created_utc": "1420070668",
   "downs": 0,
   "score": 3,
   "author": "TheDukeofEtown",
   "archived": false,
   "distinguished": null,
   "id": "cnasd6x",
   "score_hidden": false,
   "name": "t1_cnasd6x",
   "link_id": "t3_2qyhmp"
}
```


## Deliverables
(To be noted that we had to modify the deliverables after the discussion during checkpoint in December)
Explore the dataset and get insights into the following questions:

1. Extract the Switzerland and EU specific submissions and comments: The dataset on the cluster consists of all the Reddit submissions and comments from the year 2007 to 2015 (Aug). The first part of the project is to filter the submissions and comments specific to subreddits in Switzerland, UK, Germany, France, Italy and Spain. This will be accomplished using Spark dataframe.

2. Growth in Reddit usage: To study the usage of Reddit over the years in Switzerland, UK, Germany, France, Italy and Spain. An interactive visualisation will be created in D3js to see the increase in the number of submissions/comments in different countries over the years. 

3. Main discussion topics: We will use the number of comments per post, upvotes, and downvotes in order to determine the most popular topics. In addition to this, we will perform topic modeling using LDA on the comments for each country. The aim is to study the following
  1.  Main discussion topics in each country
  2.  What are other countries talking about Switzerland ?

In the end we will use a plot with the topics vs time to show the varying trends of different topics over the time.

4. Interaction among users and their contribution to different subreddits. The objective is to determine if the same small set of people contribute to most of the conversations across different subreddits or if each subreddit attracts its own set of people. The idea is to consider the top 3 or 4 submissions with the most number of comments in 2014 for each country. Each node in the graph is a reddit user who contributed to these discussions. Each edge in the graph represents the user's comment to the submission. This will help us determine if the same set of users are commenting on submissions in different subreddits. 


## Conclusions and Findings:
1. Reddit usage has increased dramatically over the last 2-3 years
2. Few subreddits account for most of the conversations
3. Heavily used by tourists and people moving in from other countries
4. Surprisingly, most conversations in Switzerland subreddits are in English
5. Neighbouring countries mostly refer to Switzerland in conversations about tax, immigration, banks, and referendum.
6. Political topics draw a lot of interest and controversies among users.
7. UK alone generates the same amount of content as that of other countries combined (Germany, France, Italy, Spain, Switzerland).
8. UK loves to talk about Doctor Who and Football on Reddit.


## Feasibility and Risks
1. We expect to complete the exploration of main discussion topics in Switzerland before the checkpoint in mid-December.


2. While using sentiment analysis, depending upon our data and ease of use of the available tools, library’s performance, we may or may not be able to get useful insights in the given time.


3. In order to generate comments using [SubReddit Simulator](https://www.reddit.com/r/SubredditSimulator/comments/3g9ioz/what_is_rsubredditsimulator/), we will need to use Recurrent Neural Networks. Since we do not prior experience in training these models, this part of the project may or may not be feasible.

(After the discussion during December checkpoint, it was decided that both points 2 (Sentiment analysis) and 3(Subreddit simulator) were not going to yield reliable results and as a result, we decided to focus our efforts on growth in Reddit content, Topic modeling and to study communication between users to topics in different subreddits.)

## Timeplan
(The following timeplan was modified based on discussions and changes in the project deliverables.)
#### Week1 - Scrapping
Scrapping the Swiss SubReddit Networks names from [r/Switzerland](https://www.reddit.com/r/Switzerland/)

#### Week2 - Big Data Preprocessing
* Filtering Dataset by “subreddit” to separate Swiss content from the rest
* Extracting relevant fields from the json blocks like,
  1. Get the parent post.
  2. Users’ Comment on the post.
  3. Number of Up and Downvotes on the comment.
Controversiality of comment.
  4. Karma of the user commenting (not given in the dataset! Used of Reddit’ API to expand our data is required).
  5. Time of the post.
  
#### Weeks 3-4
Main discussion topics (see “Deliverables”).

#### Weeks 5-6
The good, the bad and the ugly about Switzerland (see “Deliverables”).

#### Weeks 7-11
Subreddit simulator (see “Deliverables”).


