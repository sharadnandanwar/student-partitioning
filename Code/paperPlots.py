import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
import numpy as np
import assignments
from pylab import *

########################################################################################################################

def PlotMeanGain(inputFile, outputFile, outputDir, student_count, section_count, trials):
	rcParams['legend.numpoints'] = 1
	matplotlib.rc('xtick', labelsize=20) 
	matplotlib.rc('ytick', labelsize=20)

	scores = np.genfromtxt(inputFile);

	left =1;
	right = 9;

	x = [1024/2**i for i in range(left,right+1)];
	y = np.zeros([right-left+1,4]);

	for j in range(1,trials+1):
		ability =  np.random.choice(scores,student_count,replace=False);
		ability = (ability-np.min(ability))/(np.max(ability)-np.min(ability));
		ability = np.sort(ability);
		ability=ability[::-1];

		for i in range(left,right+1):
			group_size = 2**i;
			section_count = student_count/group_size;
	
			sections = assignments.meanLearnAssignment(ability, section_count);
			val_meanLearn = assignments.evaluateMeanLearnAssignment(sections);
			y[i-left][0] = y[i-left][0] + (val_meanLearn)/trials;

			sections = assignments.randomAssignment(ability, section_count);
			val_random = assignments.evaluateMeanLearnAssignment(sections);
			y[i-left][1] = y[i-left][1] + (val_random)/trials;

			sections = assignments.stratifiedAssignment(ability, section_count);
			val_stratified = assignments.evaluateMeanLearnAssignment(sections);
			y[i-left][2] = y[i-left][2] + (val_stratified)/trials;

			sections = assignments.iterEndPointsAssignment(ability, section_count);
			val_iterEP = assignments.evaluateMeanLearnAssignment(sections);
			y[i-left][3] = y[i-left][3] + (val_iterEP)/trials;
		
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)
	ax.set_xscale('log',basex=2)
	ax.xaxis.set_major_formatter(tkr.FormatStrFormatter("%d"));
	ax.set_xlabel('Number of Groups', fontsize=25);
	ax.set_ylabel('Gain', fontsize=25);

	print y[:,0]
	plt.plot(x, y[:,0], '--', color = 'blue', label='Mean Learn', zorder=4, linewidth=3, marker='s', markersize=8, markeredgewidth=3, markeredgecolor='#0000ff', markerfacecolor='#ffffff');
	plt.plot(x, y[:,1], '-.', color = 'green', label='Random', zorder=3, linewidth=3, marker='v', markersize=10, markeredgewidth=2, markeredgecolor='#00ff00', markerfacecolor='#ffffff');
	plt.plot(x, y[:,3], '--', color = 'red', label='IterEndPoints', zorder=2, linewidth=3, marker='d', markersize=10, markeredgewidth=2, markeredgecolor='#ff0000', markerfacecolor='#ffffff');
	plt.plot(x, y[:,2], '-.', color = 'black', label='Stratified', zorder=1, linewidth=3, marker='o', markersize=10, markeredgewidth=3, markeredgecolor='#000000', markerfacecolor='#ffffff');

	plt.grid();
	l = plt.legend(loc=0);
	l.set_zorder(5);

	plt.ylim([0,200]);
	fig.savefig(outputDir+'/'+outputFile+'_MeanLearn.eps', format="eps", bbox_inches='tight')
	plt.close(fig);
	return

########################################################################################################################
	
def PlotMedianGain(inputFile, outputFile, outputDir, student_count, section_count, trials):
	rcParams['legend.numpoints'] = 1
	matplotlib.rc('xtick', labelsize=20) 
	matplotlib.rc('ytick', labelsize=20)

	scores = np.genfromtxt(inputFile);

	left =1;
	right = 9;

	x = [1024/2**i for i in range(left,right+1)];
	y = np.zeros([right-left+1,4]);

	for j in range(1,trials+1):
		ability =  np.random.choice(scores,student_count,replace=False);
		ability = (ability-np.min(ability))/(np.max(ability)-np.min(ability));
		ability = np.sort(ability);
		ability=ability[::-1];

		for i in range(left,right+1):
			group_size = 2**i;
			section_count = student_count/group_size;
	
			sections = assignments.medianLearnAssignment(ability, section_count);
			val_medianLearn = assignments.evaluateMedianLearnAssignment(sections);
			y[i-left][0] = y[i-left][0] + (val_medianLearn)/trials;

			sections = assignments.randomAssignment(ability, section_count);
			val_random = assignments.evaluateMedianLearnAssignment(sections);
			y[i-left][1] = y[i-left][1] + (val_random)/trials;

			sections = assignments.stratifiedAssignment(ability, section_count);
			val_stratified = assignments.evaluateMedianLearnAssignment(sections);
			y[i-left][2] = y[i-left][2] + (val_stratified)/trials;

			sections = assignments.iterEndPointsAssignment(ability, section_count);
			val_iterEP = assignments.evaluateMedianLearnAssignment(sections);
			y[i-left][3] = y[i-left][3] + (val_iterEP)/trials;
		
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)
	ax.set_xscale('log',basex=2)
	ax.xaxis.set_major_formatter(tkr.FormatStrFormatter("%d"));
	ax.set_xlabel('Number of Groups', fontsize=25);
	ax.set_ylabel('Gain', fontsize=25);

	print y[:,0]
	plt.plot(x, y[:,0], '--', color = 'blue', label='Median Learn', zorder=4, linewidth=3, marker='s', markersize=8, markeredgewidth=3, markeredgecolor='#0000ff', markerfacecolor='#ffffff');
	plt.plot(x, y[:,1], '-.', color = 'green', label='Random', zorder=3, linewidth=3, marker='v', markersize=10, markeredgewidth=2, markeredgecolor='#00ff00', markerfacecolor='#ffffff');
	plt.plot(x, y[:,3], '--', color = 'red', label='IterEndPoints', zorder=2, linewidth=3, marker='d', markersize=10, markeredgewidth=2, markeredgecolor='#ff0000', markerfacecolor='#ffffff');
	plt.plot(x, y[:,2], '-.', color = 'black', label='Stratified', zorder=1, linewidth=3, marker='o', markersize=10, markeredgewidth=3, markeredgecolor='#000000', markerfacecolor='#ffffff');

	plt.grid();
	l = plt.legend(loc=0);
	l.set_zorder(5);

	plt.ylim([0,200]);
	fig.savefig(outputDir+'/'+outputFile+'_MedianLearn.eps', format="eps", bbox_inches='tight')
	plt.close(fig);
	return
	
########################################################################################################################

def PlotGrpStruc(inputFile, outputFile, outputDir, student_count, section_count):

	scores = np.genfromtxt(inputFile);
	ability =  np.random.choice(scores,student_count,replace=False);
	ability = (ability-np.min(ability))/(np.max(ability)-np.min(ability));
	ability = np.sort(ability);
	ability=ability[::-1];

	sections = assignments.meanLearnAssignment(ability, section_count);
	plt = assignments.plotAssignment(sections);
	plt.savefig(outputDir+'/'+outputFile+'_MeanLearn_GrpStruc.eps', format="eps", bbox_inches='tight');
	plt.close();

	sections = assignments.medianLearnAssignment(ability, section_count);
	plt = assignments.plotAssignment(sections);
	plt.savefig(outputDir+'/'+outputFile+'_MedianLearn_GrpStruc.eps', format="eps", bbox_inches='tight');
	plt.close();

	sections = assignments.randomAssignment(ability, section_count);
	plt = assignments.plotAssignment(sections);
	plt.savefig(outputDir+'/'+outputFile+'_Random_GrpStruc.eps', format="eps", bbox_inches='tight');
	plt.close();

	sections = assignments.stratifiedAssignment(ability, section_count);
	plt = assignments.plotAssignment(sections);
	plt.savefig(outputDir+'/'+outputFile+'_Stratified_GrpStruc.eps', format="eps", bbox_inches='tight');
	plt.close();

	sections = assignments.iterEndPointsAssignment(ability, section_count);
	plt = assignments.plotAssignment(sections);
	plt.savefig(outputDir+'/'+outputFile+'_IterEndPoints_GrpStruc.eps', format="eps", bbox_inches='tight');
	plt.close();
	
	return

