import numpy as np
import math

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

def plotAssignment(sections):
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
    for i in range(0,len(sections)):
        plt.scatter(sections[i], (i+1)*np.ones(len(sections[i])), color="#2eb82e", edgecolor='face');
        plt.plot(np.mean(sections[i]), i+1, 'ko');
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
    
def evaluateMedianLearnAssignment(sections):
    totalGain = 0;
    for i in range(0, len(sections)):
        totalGain = totalGain + computeMedianLG(sections[i]);
    return totalGain
