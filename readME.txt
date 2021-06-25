*****
This is a single layer perceptron

Currently is a proof of concept using data from round 1 of NRL 2020

Can predict at 75% accuracy the outcomes of round 2

Current Program needs to be run game by game

Run Main.py

SLP is the perceptron class

It take the inputs: 

Ladder Position
Matches
Wins 
Losses (draws count as losses)
Points for 
Points against
Points Diff
COmpetition Points
Home Losses
Away Wins

It will then create a confidence reading of winning the next game. 

Data is stored locally using sqlite but have provided a csv of round 1

Input team names with capital letter. 
Highest confidence is the predicted winner. 

******

Future Iterations: 

Will load each round data and use cumulative round data to predict next round

Will move to cloud DB

Will have GUI to select entire round, as opposed to game by game




