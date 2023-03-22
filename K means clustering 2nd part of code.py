import cluster
import random, pylab, numpy

class Patient(cluster.Example): #Is a subtype of Cluster.examples
    pass

#----Zscaling----------------------------

def scaleAttrs(vals):# This is Z scaling 00#Handling the dynaminc range btn feature vectors.( think solving the alligator No of leegs problem). returns array 
    vals = pylab.array(vals)
    mean = sum(vals)/len(vals)# mean is going ti=o alwayss be the same independent of the inital values. whohc zero, mean will alwasy be zero. Std will alwasy be 1.
    sd = numpy.std(vals)
    vals = vals - mean
    return vals/sd

def getData(toScale = False):
    #read in data
    hrList, stElevList, ageList, prevACSList, classList = [],[],[],[],[]
    cardiacData = open('cardiacData.txt', 'r')
    for l in cardiacData:
        l = l.split(',')
        hrList.append(int(l[0]))
        stElevList.append(int(l[1]))
        ageList.append(int(l[2]))
        prevACSList.append(int(l[3]))
        classList.append(int(l[4]))
    if toScale: # either creates a  ste of example with atrributes as initially or sclaed
        hrList = scaleAttrs(hrList)
        stElevList = scaleAttrs(stElevList)
        ageList = scaleAttrs(ageList)
        prevACSList = scaleAttrs(prevACSList)
    #Build points
    points = []
    for i in range(len(hrList)):
        features = pylab.array([hrList[i], prevACSList[i],\
                                stElevList[i], ageList[i]])
        pIndex = str(i)
        points.append(Patient('P'+ pIndex, features, classList[i]))
    return points

#-----------------------K means---------------------------    
def kmeans(examples, k, verbose = False): #caling K means, Numtrail times each one getting a diff sset of initial centroids and returns resulst with lowest dissimilarity
    #Get k randomly chosen initial centroids, create cluster for each
    initialCentroids = random.sample(examples, k)
    clusters = []
    for e in initialCentroids:
        clusters.append(cluster.Cluster([e]))
        
    #Iterate until centroids do not change
    converged = False
    numIterations = 0
    while not converged:
        numIterations += 1
        #Create a list containing k distinct empty lists
        newClusters = []
        for i in range(k):
            newClusters.append([])
            
        #Associate each example with closest centroid
        for e in examples:
            #Find the centroid closest to e
            smallestDistance = e.distance(clusters[0].getCentroid())
            index = 0
            for i in range(1, k):
                distance = e.distance(clusters[i].getCentroid())
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = i
            #Add e to the list of examples for appropriate cluster
            newClusters[index].append(e)
            
        for c in newClusters: #Avoid having empty clusters. 
            if len(c) == 0:
                raise ValueError('Empty Cluster')
        
        #Update each cluster; check if a centroid has changed
        converged = True
        for i in range(k):
            if clusters[i].update(newClusters[i]) > 0.0:
                converged = False
        if verbose:
            print('Iteration #' + str(numIterations))
            for c in clusters:
                print(c)
            print('') #add blank line
    return clusters

#--------TRying K means----------------

def trykmeans(examples, numClusters, numTrials, verbose = False):
    """Calls kmeans numTrials times and returns the result with the
          lowest dissimilarity"""
    best = kmeans(examples, numClusters, verbose)
    minDissimilarity = cluster.dissimilarity(best)
    trial = 1
    while trial < numTrials:
        try:
            clusters = kmeans(examples, numClusters, verbose)
        except ValueError:
            continue #If failed, try again
        currDissimilarity = cluster.dissimilarity(clusters)
        if currDissimilarity < minDissimilarity:
            best = clusters
            minDissimilarity = currDissimilarity
        trial += 1
    return best

#-----------------------------------------------------------------------------

def printClustering(clustering):
    """Assumes: clustering is a sequence of clusters
       Prints information about each cluster
       Returns list of fraction of pos cases in each cluster"""
    posFracs = []
    for c in clustering:
        numPts = 0
        numPos = 0
        for p in c.members():
            numPts += 1
            if p.getLabel() == 1:
                numPos += 1
        fracPos = numPos/numPts
        posFracs.append(fracPos)
        print('Cluster of size', numPts, 'with fraction of positives =',
              round(fracPos, 4))
    return pylab.array(posFracs)

def testClustering(patients, numClusters, seed = 0, numTrials = 5):
    random.seed(seed)
    bestClustering = trykmeans(patients, numClusters, numTrials)
    posFracs = printClustering(bestClustering)
    return posFracs


#-------------------- Running the data, initially not scaling it-----Resukst not so good--------------------
patients = getData() #      scaling the data add "True" to the brackets, remove it-data unscaled
#--------------- 
for k in (2):
    print('\n     Test k-means (k = ' + str(k) + ')')
    posFracs = testClustering(patients, k, 2)#tes clustering is returning the fraction of positive exampls for each cluster
    
  

#numPos = 0
#for p in patients:
#    if p.getLabel() == 1:
#        numPos += 1
#print('Total number of positive patients =', numPos)