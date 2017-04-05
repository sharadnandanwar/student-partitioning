import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
import numpy as np
import assignments
from pylab import *

rcParams['legend.numpoints'] = 1
matplotlib.rc('xtick', labelsize=20) 
matplotlib.rc('ytick', labelsize=20)

student_count = 1024;
scores = np.genfromtxt('../Datasets/askubuntu.com.upvotes');

trials = 30;

for group_size in [8, 32, 128]:

    x = range(1,21);
    xp = [100 - 100/float(i) for i in x];
    y = np.zeros([len(x),3]);

    for j in range(1,trials+1):
        print "Trial", j
        ability =  np.random.choice(scores,student_count,replace=False);
        ability = (ability-np.min(ability))/(np.max(ability)-np.min(ability));
        ability = np.sort(ability);
        ability=ability[::-1];

        for i in x:
            perc = 100 - 100/float(i);
            section_count = student_count/group_size;
    
            sections = assignments.percentileLearnAssignment(ability, section_count, perc);
            val = assignments.evaluatePercentileLearnAssignment(sections, perc);
            y[i-1][0] = y[i-1][0] + val/trials;

            sections = assignments.randomAssignment(ability, section_count);
            val = assignments.evaluatePercentileLearnAssignment(sections, perc);
            y[i-1][1] = y[i-1][1] + val/trials;

            sections = assignments.stratifiedAssignment(ability, section_count);
            val = assignments.evaluatePercentileLearnAssignment(sections, perc);
            y[i-1][2] = y[i-1][2] + val/trials;

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.xaxis.set_major_formatter(tkr.FormatStrFormatter("%d"));
    ax.set_xlabel('Percentile', fontsize=25);
    ax.set_ylabel('Gain', fontsize=25);
    
    plt.plot(xp, y[:,0], '--', color = 'blue', label='Percentile Part.', zorder=5, linewidth=3, marker='s', markersize=8, markeredgewidth=3, markeredgecolor='#0000ff', markerfacecolor='#ffffff');
    plt.plot(xp, y[:,1], '-.', color = 'green', label='Random', zorder=3, linewidth=3, marker='v', markersize=10, markeredgewidth=2, markeredgecolor='#00ff00', markerfacecolor='#ffffff');
    plt.plot(xp, y[:,2], '-.', color = 'red', label='Stratified', zorder=1, linewidth=3, marker='o', markersize=10, markeredgewidth=3, markeredgecolor='#ff0000', markerfacecolor='#ffffff');

    plt.grid();
    l = plt.legend(loc='upper left');
    l.set_zorder(6);

    fig.savefig('AskUbuntu_'+str(group_size)+'nLearn.eps', format="eps", bbox_inches='tight')
    plt.close(fig);


