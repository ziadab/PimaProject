
# coding: utf-8
#30 Black
#31 Red
#32 Green
#33 Yellow
#34 Blue
#35 Magenta
#36 Cyan
#37 White

# In[1]:


import numpy as np
import pandas as pd

data = pd.read_csv('diabetes.csv')



# In[3]:


shit = ["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"]
labels = data['Outcome'].values
features = data[list(shit)].values


from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.5)


# In[9]:


x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.35)


# In[17]:


clf = RandomForestClassifier(n_estimators=20)
clf = clf.fit(features, labels)


#In[19]


print("This Resolt is not sure 100% if you want a sure prediction go to your neer doctor from you \n\n")

pregnancies = int(input("Put number of times pregnant you was pregnant (if you was male put '0') : "))
glucose = int(input("Put value of plasma glucose concentration a 2 hours in an oral glucose tolerance test : "))
bloodpressure = int(input("Put diastolic blood pressure on (mm/Hg) : "))
skinthicknesstriceps =  int(input("put skin fold thickness on (mm) : "))
insulin = int(input("Put the value os 2-Hour serum insulin on (mu U/ml) : "))
bmi = float(input("Put value of Body mass index on (weight in kg/(height in m)^2) : "))
diabetespedigreefunction = float(input("Put value of diabetes pedigree function : "))
age = int(input("Put your age : "))

#In[24]


anwser = clf.predict([[pregnancies,glucose,bloodpressure,skinthicknesstriceps,insulin,bmi,diabetespedigreefunction,age]])

if int(anwser) == 1 :
	print("\n\n\33[31mSoory Dude but I think you have Diabetes")
	print("Go to The Doctor Now")

elif int(anwser) == 0:
	print("You are all right for now but be careful\n")

# In[18]:


