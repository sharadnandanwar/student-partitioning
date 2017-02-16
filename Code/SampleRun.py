import paperPlots as pp

inputFile = '../Datasets/SSC/SSC NER Region';
outputFile = 'SSC-NER';
outputDir = '../';
stuCount = 1024;
secCount = 32;
trials = 30;

pp.PlotMeanGain(inputFile, outputFile, outputDir, stuCount, secCount, trials);
pp.PlotMedianGain(inputFile, outputFile, outputDir, stuCount, secCount, trials);
pp.PlotGrpStruc(inputFile, outputFile, outputDir, stuCount, secCount);

