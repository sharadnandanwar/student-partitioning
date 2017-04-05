import matplotlib.pyplot as plt
import numpy as np
import assignments

student_count = 1024;
scores = np.genfromtxt('../Datasets/askubuntu.com.upvotes');
ability =  np.random.choice(scores,student_count,replace=False);
ability = (ability-np.min(ability))/(np.max(ability)-np.min(ability));
ability = np.sort(ability);
ability=ability[::-1];

section_count = 128;

sections = assignments.percentileLearnAssignment(ability, section_count, 75);
plt = assignments.plotAssignment(sections);
plt.savefig('AskUbuntu_PercentileLearn_GrpStruc.eps', format="eps", bbox_inches='tight');
plt.close();

sections = assignments.randomAssignment(ability, section_count);
plt = assignments.plotAssignment(sections);
plt.savefig('AskUbuntu_Random_GrpStruc.eps', format="eps", bbox_inches='tight');
plt.close();

sections = assignments.stratifiedAssignment(ability, section_count);
plt = assignments.plotAssignment(sections);
plt.savefig('AskUbuntu_Stratified_GrpStruc.eps', format="eps", bbox_inches='tight');
plt.close();

