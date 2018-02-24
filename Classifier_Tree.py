#import dependencies 
#import scikit and specify the module we want to import
from sklearn import tree

#clf as Decision Tree 
clf = tree.DecisionTreeClassifier()

#X is a list of lists (a text string)
#[height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

#labeled data 
Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']


#fit/trains the model on our sample data 
clf = clf.fit(X, Y)

#store our prediction to determine whether the parameters entered are either male or female. 
prediction = clf.predict([[190, 70, 43]])

#print our prediction
print(prediction)
