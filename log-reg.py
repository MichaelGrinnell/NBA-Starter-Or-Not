from sklearn.model_selection import train_test_split #this is to split the data into test data and training data to make the logisitic regression model
from sklearn.linear_model import LogisticRegression #this is to run the logisitic regression
from sklearn import metrics #thisis to show the accuracy
import seaborn as sn #this and the next are to create a heatmap of the confustion matrix
import matplotlib.pyplot as plt
import statsmodels.api as sm #this is to show the coefficients so I can later create the probability function

X = df4[['2PM', '2PA','3PM','3PA','FTM','FTA','ORB','DRB','AST','STL','BLK','TOV','PF']] #this contains all of the predicters
y = df4['Starter'] #this is the target variable being used
X = sm.add_constant(X) #this it to add a constant into the mix, for some reason the logistic regression doesnt do it manually
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=0, stratify=y) #this is to split the data into training and test sets to build the model, and it shuffles the data around to try and make it more random
logistic_regression= LogisticRegression(max_iter=1000) #this sets up the logisitc regression function
logistic_regression.fit(X_train,y_train) #this runs the logistic regression on the training data
y_pred=logistic_regression.predict(X_test) #this then checks that model with the testing data to see the accuracy
confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted']) #this sets up the confusion matrix so we can see the how the data was split
sn.heatmap(confusion_matrix, annot=True) #this shows us the confusion matrix
print('Accuracy: ',round((metrics.accuracy_score(y_test, y_pred)*100),2),'%') #this shows us the accuracy of  our model
plt.show()
logit_model=sm.Logit(y_train,X_train) #this sets up logisitc regression results based on our training data
result=logit_model.fit() #this runs the model
print(result.summary()) #this lets us see the coefficents among other things

import math #this is so i can use the e**
x=input('Enter Player ID: ') #this is so i can enter  players id and have that id run for all the stats I want to pull
y=Player(x)
print(y.name)
TPM = ((y('2020-21').two_pointers/y('2020-21').minutes_played)*36)
TPA = ((y('2020-21').two_point_attempts/y('2020-21').minutes_played)*36)
THRPM = ((y('2020-21').three_pointers/y('2020-21').minutes_played)*36)
THRPA = ((y('2020-21').three_point_attempts/y('2020-21').minutes_played)*36)
FTM = ((y('2020-21').free_throws/y('2020-21').minutes_played)*36)
FTA = ((y('2020-21').free_throw_attempts/y('2020-21').minutes_played)*36)
ORB = ((y('2020-21').offensive_rebounds/y('2020-21').minutes_played)*36)
DRB = ((y('2020-21').defensive_rebounds/y('2020-21').minutes_played)*36)
AST = ((y('2020-21').assists/y('2020-21').minutes_played)*36)
STL = ((y('2020-21').steals/y('2020-21').minutes_played)*36)
BLK = ((y('2020-21').blocks/y('2020-21').minutes_played)*36)
TOV = ((y('2020-21').turnovers/y('2020-21').minutes_played)*36)
PF = ((y('2020-21').personal_fouls/y('2020-21').minutes_played)*36)
log_prob=(1/(1+(math.exp(-(-3.7410 + (0.7221 *(TPM)) + (-0.1764 *(TPA)) + (1.2685 *(THRPM)) + (-0.3249*(THRPA)) + (0.5920*(FTM)) + (-0.3152*(FTA)) + (-0.2229*(ORB)) + (0.2455*(DRB)) + ( 0.2470*(AST)) + (-0.0009 *(STL)) + (0.1955*(BLK)) + (-0.0181*(TOV))+ (-0.5428 *(PF)))))))
#above is the logisitic regression equation so I can enter a players stats and see where they would be classified
print('Probability=',log_prob)

GS= y('2020-21').games_started/y('2020-21').games_played
if GS >= .75:
  print(y.name, 'is a starter')
if GS< .75:
  print(y.name, 'is not a starter')

if log_prob >= .5:
  print(y.name, 'should be starting')
if log_prob < .5:
  print(y.name, 'should not be starting')

#after running the the first cell to get the necessary libraries, here are some players you can try this out on
#inglejo01
#curryst01
#fournev01
#williro04