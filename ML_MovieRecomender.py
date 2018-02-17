import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

#fetch data set
data = fetch_movielens(min_rating=4.0)

#printtraining and testing data
print(repr(data['train']))
print(repr(data['test']))

#create model
#warp stands for Weighted Approximate-Rank Pairwise
#uses gradient descent and takes into account past ratings
model = LightFM(loss='warp')
#train model
#epochs = run
model.fit(data['train'], epochs=30, num_threads=2)

def sample_recommendation(model, data, user_ids):
        #number of users and movies in training data
        n_users, n_items = data ['train'].shape

        #generate recommendations for each user we input
        for user_id in user_ids:

                #movies they already like
                known_positives = data['item_labels'], data['train'].tocsr()[user_id].indices

                #movies our model predicts they will like
                scores = model.predict(user_id, np.arange(n_items))
                #rank them in order of most like to least liked
                #here the negative sign returns the results in descending order
                top_items = data['item_labels'][np.argsort(-scores)]

                #print out the results
                print("User %s" % user_id)
                print("     known positives:")
                #loop 1
                for x in known_positives[:3]:
                    print("     %s" % x)
                #print top 3 recommendations 
                print("     Recommended")
                #loop 2
                for x in top_items[:3]:
                    print("     %s" % x)
#which users do we want to model for
sample_recommendation(model, data, [1, 2, 3])
