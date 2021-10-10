*****
# **NRL FOOTY TIPPER** 
****

This is a single layer perceptron

Currently is a proof of concept using data from round 1 of NRL 2020

Can predict at 75% accuracy the outcomes of round 2

Current Program needs to be run game by game

Run:
> Python3 Perceptron.py

SLP.py is the perceptron class

It take the inputs: 

- Ladder Position
- Matches
- Wins 
- Losses (draws count as losses)
- Points for 
- Points against
- Points Diff
- Competition Points
- Home Losses
- Away Wins

It will then create a confidence reading of winning the next game. 

HAve moved away from sql database, will only have csv's

Input team names with capital letter. 
Highest confidence is the predicted winner. 

*****
*****
Future Iterations: 


Will load each round data and use cumulative round data to predict next round

Will incorporate a webscraper to fetch data 

Will move to cloud DB

Will have GUI to select entire round, as opposed to game by game

*****



