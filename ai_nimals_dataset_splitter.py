import os
import random



os.environ["PATH"] += os.pathsep + os.getcwd()

trainingSetRatio = 0.6
validationSetRatio = 0.2
testingSetRatio = 0.2

def fileCopier(sourceSet, setPath, setFiles):
    pass

def main():
    datasetPath = os.getcwd() + "/Downloads"
    for (i, classFolder) in enumerate (os.listdir(datasetPath)):
        datasetDetectedClass = os.path.join(datasetPath, classFolder, "detected")
        dataSetList = os.listdir(datasetDetectedClass)
        calssImagesQuantity = len(dataSetList)
        className = classFolder[:-5]

        validationSetQuantity = int(calssImagesQuantity * validationSetRatio-1)
        testingSetQuantity = int(calssImagesQuantity * testingSetRatio-1)
        trainingSetQuantity = int(calssImagesQuantity * trainingSetRatio)
        trainingSetQuantity += (calssImagesQuantity - (trainingSetQuantity+validationSetQuantity+testingSetQuantity))

        random.shuffle(dataSetList)
        random.shuffle(dataSetList)
        random.shuffle(dataSetList)

        trainingSet = dataSetList[0:trainingSetQuantity]
        testingSet = dataSetList[trainingSetQuantity:testingSetQuantity+trainingSetQuantity]
        validationSet = dataSetList[testingSetQuantity+trainingSetQuantity: testingSetQuantity+trainingSetQuantity+validationSetQuantity]

        trainingSetPath = os.path.join()
        testingSetPath = os.path.join()
        validationPath = os.path.join()

        fileCopier(datasetDetectedClass, trainingSetPath, trainingSet)
        fileCopier(datasetDetectedClass, testingSetPath, testingSet)
        fileCopier(datasetDetectedClass, validationPath, validationSet)


if __name__ == "__main__":
    main()