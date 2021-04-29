# A.I. Sports Data Science Challenge
Welcome to the A.I. Sports data challenge, we are glad you are here! 

Let's get started. 

Take some time to read the instructions below. If you have
any questions _before you begin_, please send an email to 
[jason@aisportsfirm.com](mailto:jason@aisportsfirm.com) &
[jared@aisportsfirm.com](mailto:jared@aisportsfirm.com)
and we will do our best to address your question(s) in a timely manner.



## Background
A.I. Sports operates in the fast-paced sports betting industry. Predicting the results of a sporting event is extremely challenging. Our clients understand this difficulting but expect our models outperform the market. We have to ensure that our predicted probabilites allow bettors to find an edge over their competition.

A.I Sports is dedicated to helping clients make the best decisions possible with their captial. We provide cutting-edge products that enable them to be successful. We are always experimenting and tinkering with our models to improve results. Testing out new approaches and various algorithms is all in a days work. The drive to always improve is needed if you want to excel here. The ability to build and deploy models quickly is a needed skillset.



## The Challenge
We are interested in gauging your ability to take a machine learning project from conception to reality. In this data challenge, you are tasked with building a classification model for College Basketball games using the supplied dataset. To complete this challenge, you will need to clone this repository and commit your changes to the clone. When you are satisfied with your model, open a pull request to this repository. Before opening a pull request, ensure that you have met the requirements specified below.

You are expected to deliver the following in your pull request:

```
    1. submission.csv: A file containing the predictions from your
       model on the provided test dataset.
       
    2. training.py or training.R: A Python or R script that contains the logic used to
       train your model using or the provided training dataset.
       
    3. METRICS.md: A markdown file indicating the evaluation metric(s) 
       you chose and your justification for choosing said metric(s).
       
    4. Any additional supporting python or R files, modules and packages that
       you need to create in order to successfully train your model on
       the training dataset and make predictions on the test dataset.
```


## The Data
In this repository, you will find a compressed CSV file called 
`train.csv.tar.bz2` 
containing the data that we would like you to use for the challenge. 
The features within the provided dataset are:
```
game_id: The unique identifier for each game
game_stats: There are many boxscore and advanced stats for each game
vegas_spread: The vegas line that we are attempting to beat
```

Additionally, you will find a CSV file named `test.csv.tar.bz2` that
contains the following features:
```
game_id: The unique identifier for the document
vegas_spread: The vegas line that we are attempting to beat
prediction: Output from your model
bet_recommendation: Which side of the game should our client bet or should they not bet this game (Home, Away, No Bet)
```

_NOTE: Please refrain from using any data sources other than what you might find in the CSV files._ 

## Code Requirements
You are required to complete this challenge using Python 3 
(version 3.6 or later) or R. Within that scope, you are free to use whichever
libraries and frameworks allow you to get the job done.

We will attempt to run your code as-is, so you should include everything
we might need (or some mechanism for getting everything we might need)
to successfully run your code.

## Evaluation
For this challenge, _you_ are tasked with selecting the appropriate
metric(s) with which to evaluate your model. As mentioned above, you will
need to provide justification for your choice(s).

*Documentation is important*

## Timeline
As a candidate, you have 7 days in order to complete and submit your pull
request for review, but remember, there are other candidates being considered
for this position as well.

## Submission Instructions
Once your confident in your solution, submit a pull request and our team
will evaluate your solution.

Good luck!
