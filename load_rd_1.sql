--
-- File generated with SQLiteStudio v3.3.3 on Sat Aug 14 09:38:29 2021
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Ladder_1
CREATE TABLE Ladder_1 (Team STRING PRIMARY KEY, Position INTEGER, Matches INTEGER, Wins INTEGER, Losses INTEGER, "For" INTEGER, Against INTEGER, Difference INTEGER, Points INTEGER, Away_Wins INTEGER, Home_Losses INTEGER);
INSERT INTO Ladder_1 (Team, Position, Matches, Wins, Losses, "For", Against, Difference, Points, Away_Wins, Home_Losses) VALUES ('Knights', 1, 1, 1, 0, 20, 0, 20, 2, 0, 0);
INSERT INTO Ladder_1 (Team, Position, Matches, Wins, Losses, "For", Against, Difference, Points, Away_Wins, Home_Losses) VALUES ('Raiders', 2, 1, 1, 0, 24, 6, 18, 2, 0, 0);
INSERT INTO Ladder_1 (Team, Position, Matches, Wins, Losses, "For", Against, Difference, Points, Away_Wins, Home_Losses) VALUES ('Storm', 3, 1, 1, 0, 18, 4, 14, 2, 0, 0);
INSERT INTO Ladder_1 (Team, Position, Matches, Wins, Losses, "For", Against, Difference, Points, Away_Wins, Home_Losses) VALUES ('Wests Tigers', 4, 1, 1, 0, 24, 14, 10, 2, 1, 0);
INSERT INTO Ladder_1 (Team, Position, Matches, Wins, Losses, "For", Against, Difference, Points, Away_Wins, Home_Losses) VALUES ('Broncos', 5, 1, 1, 0, 28, 21, 7, 2, 1, 0);
INSERT INTO Ladder_1 (Team, Position, Matches, Wins, Losses, "For", Against, Difference, Points, Away_Wins, Home_Losses) VALUES ('Eels', 6, 1, 1, 0, 8, 2, 6, 2, 0, 0);
INSERT INTO Ladder_1 (Team, Position, Matches, Wins, Losses, "For", Against, Difference, Points, Away_Wins, Home_Losses) VALUES ('Panthers', 7, 1, 1, 0, 20, 14, 6, 2, 0, 0);
INSERT INTO Ladder_1 (Team, Position, Matches, Wins, Losses, "For", Against, Difference, Points, Away_Wins, Home_Losses) VALUES ('Rabbitohs', 8, 1, 1, 0, 22, 18, 4, 2, 0, 0);
INSERT INTO Ladder_1 (Team, Position, Matches, Wins, Losses, "For", Against, Difference, Points, Away_Wins, Home_Losses) VALUES ('Sharks', 9, 1, 0, 1, 18, 22, -4, 0, 0, 0);
INSERT INTO Ladder_1 (Team, Position, Matches, Wins, Losses, "For", Against, Difference, Points, Away_Wins, Home_Losses) VALUES ('Bulldogs', 10, 1, 0, 1, 2, 8, -6, 0, 0, 0);
INSERT INTO Ladder_1 (Team, Position, Matches, Wins, Losses, "For", Against, Difference, Points, Away_Wins, Home_Losses) VALUES ('Roosters', 11, 1, 0, 1, 14, 20, -6, 0, 0, 0);
INSERT INTO Ladder_1 (Team, Position, Matches, Wins, Losses, "For", Against, Difference, Points, Away_Wins, Home_Losses) VALUES ('Cowboys', 12, 1, 0, 1, 21, 28, -7, 0, 0, 0);
INSERT INTO Ladder_1 (Team, Position, Matches, Wins, Losses, "For", Against, Difference, Points, Away_Wins, Home_Losses) VALUES ('Dragons', 13, 1, 0, 1, 14, 24, -10, 0, 0, 1);
INSERT INTO Ladder_1 (Team, Position, Matches, Wins, Losses, "For", Against, Difference, Points, Away_Wins, Home_Losses) VALUES ('Sea Eagles', 14, 1, 0, 1, 4, 18, -14, 0, 0, 1);
INSERT INTO Ladder_1 (Team, Position, Matches, Wins, Losses, "For", Against, Difference, Points, Away_Wins, Home_Losses) VALUES ('Titans', 15, 1, 0, 1, 6, 24, -18, 0, 0, 0);
INSERT INTO Ladder_1 (Team, Position, Matches, Wins, Losses, "For", Against, Difference, Points, Away_Wins, Home_Losses) VALUES ('Warriors', 16, 1, 0, 1, 0, 20, -20, 0, 0, 0);

-- Table: results_rd_1
CREATE TABLE results_rd_1 (Team STRING PRIMARY KEY REFERENCES Ladder_1 (Team), Result INTEGER);
INSERT INTO results_rd_1 (Team, Result) VALUES ('Knights', 1);
INSERT INTO results_rd_1 (Team, Result) VALUES ('Raiders', 1);
INSERT INTO results_rd_1 (Team, Result) VALUES ('Storm', 1);
INSERT INTO results_rd_1 (Team, Result) VALUES ('Wests Tigers', 1);
INSERT INTO results_rd_1 (Team, Result) VALUES ('Broncos', 1);
INSERT INTO results_rd_1 (Team, Result) VALUES ('Eels', 1);
INSERT INTO results_rd_1 (Team, Result) VALUES ('Panthers', 1);
INSERT INTO results_rd_1 (Team, Result) VALUES ('Rabbitohs', 1);
INSERT INTO results_rd_1 (Team, Result) VALUES ('Sharks', 0);
INSERT INTO results_rd_1 (Team, Result) VALUES ('Bulldogs', 0);
INSERT INTO results_rd_1 (Team, Result) VALUES ('Roosters', 0);
INSERT INTO results_rd_1 (Team, Result) VALUES ('Cowboys', 0);
INSERT INTO results_rd_1 (Team, Result) VALUES ('Dragons', 0);
INSERT INTO results_rd_1 (Team, Result) VALUES ('Sea Eagles', 0);
INSERT INTO results_rd_1 (Team, Result) VALUES ('Titans', 0);
INSERT INTO results_rd_1 (Team, Result) VALUES ('Warriors', 0);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
