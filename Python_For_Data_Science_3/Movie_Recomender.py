'''
Install Dependencies 
    [pip install numpy]
    [pip install scipy]
    [pip install lightfm]

numpy & scipy for math
lightfm will be used to perform recommendation algorithms 
'''

import numpy as np
#lightfm is a large package, so we only import what we want 
#movielens is a large csv file with 100,000 ratings for 1,000 users on 1,700 movies
#each user has at least rated 20 movies on a scale of 1 to 5
from lightfm.datasets import fetch_movielens

from lightfm import LightFM

#fetch data set and store our data
#min rating of 4
data = fetch_movielens(min_rating=4.0)

#printtraining and testing data
#storing data in a dictionary as a string 
#training data contains 10x more items than our testing data 
print(repr(data['train']))
print(repr(data['test']))

#create model
#loss measures the difference of our prediction and our models output 
#warp = Weighted Approximate-Rank Pairwise
#this allows us to minimize our function during training to be more accurate over time
#this method uses gradient descent and takes into account past ratings
model = LightFM(loss='warp')

#Now we train model on the training dictionary we set up earlier
#epochs = runs for training session
#threads = parrallel computations 
model.fit(data['train'], epochs=30, num_threads=2)

def sample_recommendation(model, data, user_ids):
#number of users and movies in training data
    n_users, n_items = data ['train'].shape
    #loop for each user
    #generate recommendations for each user we input
    #simplify problem to binary, 4 = negative & 5=positive
    for user_id in user_ids:
        #movies they already like
        #subarray in data matrix as compressed sparse row format retrieved through indices attribute
        known_positives = data['item_labels'], data['train'].tocsr()[user_id].indices
        #movies our model predicts they will like
        scores = model.predict(user_id, np.arange(n_items))
        #argsort will rank results in order of most liked to least liked
        #here the negative sign returns the results in descending order
        top_items = data['item_labels'][np.argsort(-scores)]

        #print out the results
        print("User %s" % user_id)
        print("     known positives:")
        #loop 1, top 3 movies user has picked
        for x in known_positives[:3]:
            print("     %s" % x)
            print("     Recommended")
        #loop 2, print out top 3 recommended movies 
        for x in top_items[:3]:
        print("     %s" % x)

#which users do we want to model for
sample_recommendation(model, data, [1, 2, 3])
