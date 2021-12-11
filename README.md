# COS 427 Final Project
Team members: Benjamin Hodgkins

Goals: The goal of this project was to develop a NLP classifier to classify four classes of 
abstract from PubMed. This classifier would distinguish between abstracts about Influenza, HIV, 
Lung Cancer and Heart Disease. 

Materials and Methods: 40,000 abstracts (10,000 of each class) were used for training/validation/testing,
in a 70-15-15 split. Naive Bayes, SVM and Logistic Regression classifiers were used with a BoW representation.
main.py contains the pre-processing/classifiers, while import_data.py was run to collect the data from PubMed
which is stored in abstracts.txt

Results: To measure success of the classifiers, accuracy, precision, recall and F1 score were all noted.
All three classifiers had over 0.96 for each category, indicating the classifiers worked very well. 
Total time to train was about 20s. 

Conclusion: As noted above, all three classifiers with a BoW representation worked extremely well. 

Discussion: BoW is a fairly simple representation and if this classifier were adapted to full papers,
it likely would not work as well since papers have less structure than an abstract. Additionally,
these algorithms probably overfitted based on the high F1 score, and would need a lot more data if 
these classifiers were expanded to classify more diseases. Classes with less data could be challenging
to classify.

Outlooks: In the future, the number of classes that this project could detect could be expanded to 
cover many more of the diseases/conditions covered by PubMed abstracts. Additionally, these same 
techniques could be used to process full-text articles on PubMedCentral.
