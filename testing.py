from vectorization import*
from sklearn import metrics

# test = input("Enter the sntence you want to test : ")
testData = pd.read_csv("/home/userone/eclipse_platform.csv")
test = testData.iloc[1000, 4]
print(test)
actual_output = ["Negative"]*len(test)
model = training_the_dataset()
predicted_output = []

for i in test:
    vec = generate_vectors(model, i)
    dist = calc_distance(vec)
    predicted_output.append(find_category(dist))


accuracy = metrics.accuracy_score(actual_output, predicted_output)
print("The accuracy of this model is : ", accuracy)
