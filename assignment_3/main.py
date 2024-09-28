"""
In this assignment, you will implement the Naive Bayes classification method
For this assignment, you will be working with a Spam Collection dataset,
consisting of text messages that have been collected for Spam research. 

The csv file contains one message per line with a total of 30 messages 
tagged either being ham (legitimate) or spam. Each line is composed of two columns: 
column 1 contains the label (ham or spam) and 
column 2 contains raw text.

Consider the first 20 samples as your training set 
and the rest 10 samples for your testing. 

Tasks: 
Load the dataset and split into training and testing sets 
(first 20 into training and the rest into testing)  (1 point)


Compute the prior probabilities: P(spam) and P(ham)  (2 points)


Compute the conditional probabilities P(sentence/spam) (2 points)


Compute the posterior probabilities 
(probability of a sentence belonging to a spam or ham) (2 points)
P(spam/sentence) ∝ P(spam) * P(sentence/spam) 
Posterior ∝ prior * conditional
P(ham/sentence) ∝ P(ham) * P(sentence/ham) 


For each sentence in the test set: (2 points)
Display the sentence
Print the posterior probability of a sentence belonging to spam or ham 
Display the class (spam or ham) 


Report the test set accuracy (1 point)
Accuracy = no. of sentences correctly predicted by model / total sentences
"""
import csv
from collections import defaultdict

spam_data=[]
ham_data=[]
training_data=[]
test_data=[]
with open('assignment_3/SpamDetection.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    next(csv_reader)
    
    for i,line in enumerate(csv_reader):
        if i<20:
            training_data.append(line)
            # spam_data.extend(line[1].split()) if line[0]=='spam' else ham_data.extend(line[1].split())
            # spam_data.append(line[1]) if line[0]=='spam' else ham_data.append(line[1])
        else:
            test_data.append(line)
p_spam=len([x for x in training_data if x[0]=='spam'])/len(training_data)
p_ham=len([x for x in training_data if x[0]=='ham'])/len(training_data)
# print(p_spam,p_ham)
for line in training_data:
    spam_data.extend(line[1].split())if line[0]=='spam' else ham_data.extend(line[1].split())
print(spam_data)
spam_dict=defaultdict(float)
for word in spam_data:
    spam_dict[word]+=1
for k in spam_dict:
    spam_dict[k]+=1
    spam_dict[k]/=(len(spam_data)+len(spam_dict.keys()))
# print(spam_dict)

ham_dict=defaultdict(float)
for word in ham_data:
    ham_dict[word]+=1
for k in ham_dict:
    ham_dict[k]+=1
    ham_dict[k]/=(len(ham_data)+len(ham_dict.keys()))
# print(ham_dict)
print(ham_dict)
#def spam_or_ham(message:string)
test='Sorry I will call later in meeting'
test_list=test.split()
# print(test_list)
print(p_spam)
p_normal=p_ham
p_spam_word=p_spam
for word in test_list:
    p_normal*=ham_dict[word]
    
for word in test_list:
    p_spam_word*=spam_dict[word]
print(p_normal)
print(p_spam_word)



print(training_data)





# p_ham=n_ham/len(training_data)
# print(spam_data)
# print(len(spam_data))
# spam_dict=defaultdict(float)
# for word in spam_data:
#     spam_dict[word]+=1
# for k in spam_dict:
#     spam_dict[k]/=len(spam_data)
# print(spam_dict)
