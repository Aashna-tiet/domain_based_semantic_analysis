import vectorization
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

model = vectorization.training_the_dataset


xtesting = pd.read_csv('/home/userone/Downloads/test_bugs.csv')
testingData = xtesting.iloc[:, 2]

vec = []
for i in testingData:
    print(i)
    vec.append(vectorization.generate_vectors(model, i))


kmeans = KMeans(n_clusters=2, random_state=0).fit(vec)
kmeans.labels_

str = input("Enter the string you want to test : ")
vector = vectorization.generate_vectors(model, str)
