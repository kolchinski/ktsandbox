numStudents = 100;
numQuestions = 30;

pL0 = 0.1;
pLearn = 0.2;
pGuess = 0.25;
pSlip = 0.05;

trans = [1-pLearn,pLearn; 
        0,1];
emis = [1-pGuess, pGuess; 
        pSlip, 1-pSlip];

answers = zeros(numStudents, numQuestions);
for i = 1:numStudents
    [seq,states] = hmmgenerate(numQuestions,trans,emis);
    answers(i,:) = seq;
    answers(i,:)
end

csvwrite('../data/matlab_synthetic.csv', answers); 

% trans_ = [0.5,0.5; 
%         0,1];
% emis_ = [0.5, 0.5; 
%         0.5, 0.5];
% 
% [estTR,estE] = hmmtrain(answers,trans_,emis_)