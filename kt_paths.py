import numpy as np


#Under cts IRT model; not for BKT use
class Question:
  def __init__(self, difficulty, concept):
    self.d = difficulty
    self.c = concept
  
  def pRight(self, skill):
    return 1.0/(1.0 + np.exp(self.d - skill))
    

def ber(p):
  return np.random.binomial(1,p)

def pRight(diff, skill):
  return .25 + .75/(1.0 + np.exp(diff - skill))


pL0 = 0.3
pG = 0.25
pS = .05
pT = 0.1

numStudents = 10
numQuestions = 300
numConcepts = 5

conceptDiffs = np.random.normal(0,1,numConcepts)
qConcepts = np.random.randint(0,numConcepts, numQuestions)
qMeans = np.array([conceptDiffs[qConcept] for qConcept in qConcepts])
diffs = np.random.normal(0,1, numQuestions) + qMeans
answers = np.zeros((numStudents, numQuestions))
knowTracks = np.zeros((numStudents, numConcepts, numQuestions))


for i in range(numStudents):
  know = np.random.binomial(1, pL0, numConcepts)
  for j in range(numQuestions):
    curConcept = qConcepts[j]
    if i == 0 and curConcept == 0: print know[0]
    knowTracks[i, curConcept, j] = know[curConcept]
    knowTracks[i, :, j] = know
    answers[i,j] = ber(pRight(diffs[j], know[curConcept]))
    if ber(pT) == 1: know[curConcept] = 1

#print "concept difficulties", conceptDiffs
#print "question concepts", qConcepts
#print "question diffs", diffs
#print answers
