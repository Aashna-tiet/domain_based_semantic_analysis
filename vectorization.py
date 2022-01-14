import pandas as pd
import numpy as np
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize as wt
import nltk
from distanceDb import *
from gensim.utils import simple_preprocess


def training_the_dataset(data_file="/home/userone/Downloads/bugs-2021-11-13.csv"):
    df = pd.read_csv(data_file)
    # print(df.iloc[:, 2])
    x = df.iloc[:, 2]
    tagged_data = [TaggedDocument(words=wt(_d.lower()), tags=[
                                  str(i)]) for i, _d in enumerate(x)]
    model = Doc2Vec(vector_size=20, window=2, min_count=1, workers=4)
    model.build_vocab(tagged_data)
    print("The Doc2Vec model has been built using {}".format(data_file))
    return model


def generate_vectors(model, t):
    str = simple_preprocess(t)
    v = model.infer_vector(str)
    return v


def calc_distance(vec):
    distance = np.linalg.norm(vec)
    print("distance is : ", distance)
    return distance


def find_category(ref_dist):
    type_of_sentence = search(ref_dist)
    return type_of_sentence
    print("The predicted sentiment type is: {}".format(type_of_sentence))


# given that we train the model just on negative sentences
# the other one will be given status of unknown
# def train_model_with_labels():
#     pass

def test_data(model):
    xtesting = pd.read_csv('/home/userone/Downloads/test_bugs.csv')
    testingData = xtesting.iloc[:, 2]
    # text = []
    # test = []
    # for i in testingData:
    #     text.append(i)
    #     test.append(text)
    #     text = []
    # print(len(test))
    vec = []
    dist = []
    for x in testingData:
        vec.append(generate_vectors(model, x))
    for v in vec:
        dist.append(calc_distance(v))

    train_data_for_semantics(dist)


def train_data_for_semantics(dist):
    #target = ['Negative' for i in range(len(dist))]
    # for time being i m passing just the negative data hence the type
    # is hard coded
    for i in dist:
        saveData(i, "Negative")
    print("The database has been saved with requirements...")


def main():
    model = training_the_dataset()
    print("the vector model has been trained....")
    test_data(model)


if __name__ == "__main__":
    main()
