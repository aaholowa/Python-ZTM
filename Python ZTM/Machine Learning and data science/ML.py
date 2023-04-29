# ML steps

# step 1 - import the data

# step 2 - clean the data

# step 3 - split the data into a training set (80%) and test set(20%)

# step 4 - create a model (import an algorithm)

# step 5 - check the output

# step 6 - improve

# New Version:

from imageai.Classification import ImageClassification
import os

exec_path = os.getcwd()

prediction = ImageClassification()

prediction.setModelTypeAsMobileNetV2()
prediction.setModelPath(os.path.join(exec_path, 'mobilenet_v2-b0353104.pth'))
prediction.loadModel()

predctions, probabilities = prediction.classifyImage(
    os.path.join(exec_path, 'house.jpg'), result_count=5)
for eachPred, eachProb in zip(predctions, probabilities):
    print(f'{eachPred} : {eachProb}')
