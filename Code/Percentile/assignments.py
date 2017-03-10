import numpy as np
import numpy.random
import math
import random

####################################################################################################

def meanLearnAssignment(ability, section_count):

    sections = [];
    for i in range(0,section_count):
        sections.append([ability[i]]);
    head = section_count;
    while True:
        tail = min(head+section_count, len(ability));
        block = ability[head:tail];
        randOrderBlock = np.random.permutation(block);
        for i in range(0,len(block)):
            sections[i].append(randOrderBlock[i]);
        if tail == len(ability):
            break;
        head = head+section_count;

    return sections

####################################################################################################

def medianLearnAssignment(ability, section_count):

    sections = [];

    bigSize = np.ceil(len(ability)/section_count);
    bigCount = np.mod(len(ability),section_count);
    
    smallSize = np.floor(len(ability)/section_count);
    smallCount = section_count - bigCount;
    
    if np.mod(smallSize,2)==0:
        evenCount = smallCount;
        evenSize = smallSize;
        oddCount = bigCount;
        oddSize = bigSize;
    else:    
        oddCount = smallCount;
        oddSize = smallSize;
        evenCount = bigCount;
        evenSize = bigSize;


    index = int(np.floor(bigSize/2)*bigCount + np.floor(smallSize/2)*smallCount);
    firstHalf = range(0,index);
    firstHalf = np.random.permutation(firstHalf);
    mid = range(index, len(ability)-index);
    mid = np.random.permutation(mid);
    secondHalf = range((len(ability) - index), len(ability));
    secondHalf = np.random.permutation(secondHalf);
    
    for i in range(0,oddCount):
        sections.append([]);
        begin = int(i*np.floor(oddSize/2));
        end = int((i+1)*np.floor(oddSize/2));
        sections[i].extend(ability[firstHalf[begin:end]]);
        sections[i].extend([ability[mid[i]]]);
        sections[i].extend(ability[secondHalf[begin:end]]);
                
    for i in range(oddCount,section_count):
        sections.append([]);
        begin = int(i*np.floor(evenSize/2));
        end = int((i+1)*np.floor(evenSize/2));
        sections[i].extend(ability[firstHalf[begin:end]]);
        sections[i].extend(ability[secondHalf[begin:end]]);

    return sections

####################################################################################################

def percentileLearnAssignment(ability, section_count, p):

    k = section_count;

    sections = [];
    n = len(ability)/section_count;
    beta = np.zeros(n);

    for i in range(0,n):
        upto = int(i - np.ceil(i*p/float(100)));
        beta[upto] = beta[upto]+1;

    m = 100/(100-p);
    q = math.floor(n/m);
    q_hat = math.ceil(n/m);

    for i in range(0,k):
        sections.append([]);

    cur = 0;
    remain0 = numpy.random.permutation(ability[cur:(cur+k*q)]);
    for i in range(0,k):
        sections[i].extend(remain0[q*i:q*(i+1)]);
        cur = cur+q;

    if (q_hat > q):
        remain1 = numpy.random.permutation(ability[cur:cur+k]);
        for i in range(0,k):
            sections[i].extend(remain1[i]);
        cur = cur+1;

    remain2 = numpy.random.permutation(ability[cur:]);
    r = n-q_hat;
    for i in range(0,k):
        sections[i].extend(remain2[r*i : r*(i+1)]);
        
    
    return sections;

####################################################################################################

def percentileLearnAssignment_allcase(ability, section_count, p):

    INF = 99999999;
    k = section_count;

    sections = [];
    n = len(ability)/section_count;
    beta = np.zeros(n);

    for i in range(0,n):
        upto = int(i - np.ceil(i*p/float(100)));
        beta[upto] = beta[upto]+1;

    chunkSizes = [];
    maxBeta = beta[0];
    tailChunk = [];
    prev = 0;
    for i in range(1,len(beta)):
        if (beta[i]==0):
            break;

        if (beta[i]==maxBeta):
            chunkSizes.append(i-prev);
            tailChunk = [];
            prev = i;
        else:
            tailChunk.append(beta[i]);

    chunkSizes.append(INF);
    
    heads = np.zeros(k).astype(int);
    
    sections = [];
    for i in range(0,k):
        sections.append([]);
        sections[i].append(ability[i]);

    cur = k;
    nextChunk = [chunkSizes[int(h)] for h in heads];
    while any([nextChunk[i]!=INF for i in range(0,k)]):
        m = np.min(nextChunk);
        inds =  np.where(nextChunk==m)[0];
        ind = random.choice(inds);
        sections[ind].extend(ability[cur:cur+m]);
        cur = cur+m;
        heads[ind] = heads[ind]+1;
        nextChunk[ind] = chunkSizes[heads[ind]];

    remain1 = numpy.random.permutation(ability[cur:cur+len(tailChunk)*k]);
    for i in range(0,k):
        sections[i].extend(remain1[i*len(tailChunk):(i+1)*len(tailChunk)]);
    cur = cur + k*len(tailChunk);

    remain2 = numpy.random.permutation(ability[cur:]);
    m = int(len(remain2)/k);
    for i in range(0,k):
        sections[i].extend(remain2[i*m:(i+1)*m]);
        
    
    return sections;

####################################################################################################

def randomAssignment(ability, section_count):

    alterPoints = np.ceil(np.linspace(0,len(ability),section_count,endpoint=False))
    alterPoints = np.append(alterPoints,len(ability))

    sections = [];
    for i in range(0,section_count):
        selectedIndices = np.random.choice(range(0, len(ability)), alterPoints[i+1]-alterPoints[i], replace=False);
        sections.append(ability[selectedIndices]);
        ability = np.delete(ability,selectedIndices);

    return sections

####################################################################################################

def stratifiedAssignment(ability, section_count):

    alterPoints = np.ceil(np.linspace(0,len(ability),section_count,endpoint=False))
    alterPoints = np.append(alterPoints,len(ability))

    sections = [];
    for i in range(0,section_count):
        selectedIndices = range(int(alterPoints[i]), int(alterPoints[i+1]));
        sections.append(ability[selectedIndices]);

    return sections

####################################################################################################

def roundRobinAssignment(ability, section_count):

    sections = [];
    offset = section_count;
    for i in range(0,section_count):
        composedSection = np.array([], dtype=np.float64);
        head = i;
        while True:
            composedSection = np.append(composedSection, ability[head]);
            head = head + offset;
            if head >= len(ability):
                break;
        sections.append(composedSection);

    return sections

####################################################################################################

def iterEndPointsAssignment(ability, section_count):

    sections = [];
    for i in range(0,section_count):
        mustBreak = False;
        lc = 0;
        section_strength = int(math.ceil(len(ability)/(section_count-i)));
        
        bestAv = -9999;
        bestComposition = [];

        for j in range(1,section_strength):
            lc = j;
            fc = section_strength - lc;
            leaderSet = ability[0:lc];
            followerSet = ability[len(ability)-fc:];
            composedSection = np.append(leaderSet, followerSet);
            if np.mean(composedSection) >= followerSet[0]:
                curAv = computeAv(composedSection);
                if curAv >= bestAv:
                    bestAv = curAv;
                    bestComposition = range(0,lc);
                    bestComposition.extend(range(len(ability)-fc,len(ability)));

        sections.append(ability[bestComposition]);
        ability = np.delete(ability, bestComposition);

    return sections

########################## UTITITY FUNCTIONS #######################################################

def plotAssignment(sections, p):
    import matplotlib.pyplot as plt
    import matplotlib.ticker as tkr
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.yaxis.set_major_formatter(tkr.FormatStrFormatter("%d"));
    ax.set_xlabel('Ability Score', fontsize=25);
    ax.set_ylabel('Group ID', fontsize=25);
    plt.tick_params(axis='both', which='major', labelsize=20)
    plt.tick_params(axis='both', which='minor', labelsize=20)
    plt.ylim([0,len(sections)+1]);
    plt.xlim([0,1]);
    t = [];
    for i in range(0,len(sections)):
        plt.scatter(sections[i], (i+1)*np.ones(len(sections[i])), color="#2eb82e", edgecolor='face');
        pindex = int(np.ceil(len(sections[i])*(100-p)/float(100)))-1;
        sections[i].sort();
        sections[i] = sections[i][::-1];
        print pindex, i+1, sections[i][pindex]
        print sections[i]
        plt.plot(sections[i][pindex], i+1, 'ko');
        t.extend(sections[i]);

    t = list(t);
    t.sort();
    t = t[::-1];
    t = t[int(np.ceil(len(t)*(100-p)/float(100)))-1];
    plt.plot([t, t], [0, len(sections)+1], 'r-', linewidth=3);
    return plt
    
def computeAv(section):
    Av = 0;
    m = np.mean(section);
    for i in range(0,len(section)):
        if section[i] < m:
            Av = Av + m - section[i];
    return Av

def computeMeanLG(section):
    LG = 0;
    section = np.sort(section);
    section = section[::-1];
    cs = np.cumsum(section);
    cs = cs.astype(float);
    rollingMean = cs/range(1,len(section)+1);

    for i in range(1,len(section)):
            LG = LG + rollingMean[i-1]-section[i];
    return LG

def computePercentileLG(section, p):
    LG = 0;
    section = np.sort(section);
    for i in range(0,len(section)):
        index = i + np.ceil((len(section)-i-1)*p/float(100));
        LG = LG + section[index] - section[i];
    return LG

def computeMedianLG(section):
    LG = 0;
    section = np.sort(section);
    for i in range(0,len(section)):
        index = int(np.floor((i+len(section))/2));
        median = section[index];
        LG = LG + median - section[i];
    return LG

def evaluateMeanLearnAssignment(sections):
    totalGain = 0;
    for i in range(0, len(sections)):
        totalGain = totalGain + computeMeanLG(sections[i]);
    return totalGain
    
def evaluatePercentileLearnAssignment(sections, p):
    totalGain = 0;
    for i in range(0, len(sections)):
        totalGain = totalGain + computePercentileLG(sections[i], p);
    return totalGain
    
def evaluateMedianLearnAssignment(sections):
    totalGain = 0;
    for i in range(0, len(sections)):
        totalGain = totalGain + computeMedianLG(sections[i]);
    return totalGain
    
