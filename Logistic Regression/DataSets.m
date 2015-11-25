function [training_in, training_out, testing_in, testing_out] = DataSets( in, out )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here

    [row, ~] = size(in);
    s = rng(1, 'v5normal');
    rng(s);
    rand_num = randperm(row);
    
    training_in = [];
    training_out = [];
    testing_in = [];
    testing_out = [];
    
    for i = 1:16786
        training_in = [training_in; in(rand_num(i), :)];
        training_out = [training_out; out(rand_num(i), :)];
    end

    for i = 16787:25824
        testing_in = [testing_in; in(rand_num(i), :)];
        testing_out = [testing_out; out(rand_num(i), :)];
    end

end

