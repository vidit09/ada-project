# Swiss on Reddit
## Abstract
In this project, we aim to explore the Reddit dataset to get insights into topics discussed in Switzerland. We plan to begin by extract the topics relevant to Switzerland from the dataset. We plan to visualize the main discussion topics in Switzerland over the time and study the varying trends.  We then plan to perform sentiment analysis on the comments posted to study if the response to the posts are negative or positive and compare it with similar results from another country. Finally we also intend to generate a Subreddit Simulator using Recurrent Neural Networks.  


Note: This is a provisional plan. The final reach of our objectives will have to be adjusted according to how complex these tasks prove to be, and how much time do they demand.

## Data description
1. Obtained from: https://www.reddit.com/r/datasets/comments/3bxlg7/i_have_every_publicly_available_reddit_comment/
2. Size: ~ 1.7 Billion JSON objects
3. Fields:  Better see it with an example!
 ```json
 	{"gilded":0,"author_flair_text":"Male","author_flair_css_class":"male","retrieved_on":1425124228,"ups":3,"subreddit_id":"t5_2s30g","edited":false,"controversiality":0,"parent_id":"t1_cnapn0k","subreddit":"AskMen","body":"I can't agree with passing the blame, but I'm glad to hear it's at least helping you with the anxiety. I went the other direction and started taking responsibility for everything. I had to realize that people make mistakes including myself and it's gonna be alright. I don't have to be shackled to my mistakes and I don't have to be afraid of making them. ","created_utc":"1420070668","downs":0,"score":3,"author":"TheDukeofEtown","archived":false,"distinguished":null,"id":"cnasd6x","score_hidden":false,"name":"t1_cnasd6x","link_id":"t3_2qyhmp"}
 ```


## Deliverables
Explore the dataset and get insights into the following questions:


1. Main discussion topics: We will use the number of comments per post, upvotes, and downvotes. We need to define a proper metric which would incorporate these factors to identify main topics. In the end we will use a plot with the topics vs time to show the varying trends.


2. The good, the bad and the ugly about Switzerland: Here we want to see how people comment on a post about Switzerland. We plan to use sentiment analysis on the comments and infer if the post has mostly negative or positive response. We have identified NLTK library that performs this task.


3. Inspired by SubReddit Simulator we aim to train a recurrent neural network (instead of hidden markov model as it is proposed there) with our selection of Switzerland related subreddits’ messages, and evaluate how it will answer in different threads.

## Feasibility and Risks
1. We expect to complete the exploration of main discussion topics in Switzerland before the checkpoint in mid-December.


2. While using sentiment analysis, depending upon our data and ease of use of the available tools, library’s performance, we may or may not be able to get useful insights in the given time.


3. In order to generate comments using [SubReddit Simulator](https://www.reddit.com/r/SubredditSimulator/comments/3g9ioz/what_is_rsubredditsimulator/), we will need to use Recurrent Neural Networks. Since we do not prior experience in training these models, this part of the project may or may not be feasible.

## Timeplan
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

Depending our task we will create appropriate data representation using above the fields.  

#### Weeks 3-4
Main discussion topics (see “Deliverables”).

#### Weeks 5-6
The good, the bad and the ugly about Switzerland (see “Deliverables”).

#### Weeks 7-11
Subreddit simulator (see “Deliverables”).


![alt tag](https://github.com/vidit09/ada-project/blob/master/timeline.png)

