% Read in synthetic data created in python
M = csvread('../data/python_synthetic.csv');
trans_ = [0.6,0.4; 
        0,1];
emis_ = [0.6, 0.4; 
        0.4, 0.6];

[estTR,estE] = hmmtrain(M,trans_,emis_)
