# NBA-Starter-Or-Not
**Table of Contents**
1. Introduction
2. How-to-Run

**Introduction**
This is Python code that retrieves player data from a sportsrefrence open-source library, and runs that through a logistic regression model to tell if a player should be a starter or not. There are two files in here, the first retrieves the data through many iterations as the data is housed in smaller subsections rather than an entire database. This first file also cleans up the data and gets it into an Excel file that is ready to use. The second file runs the data through a logistic regression and then uses the coefficents to create a probability function that allows us to determine whether an individual player should be a starter or not.

**How-to-Run**
The code in these two files are written to be run in Google Colab. The Excel file created in the first file is stored locally in Colab, and the regression file pulls from that locally stored Excel file. There are ways of doing it without Google Colab but that is not shown here.
