raw_data = read_file('myFinalData.csv');

[ sorted ] = SortData(raw_data(2:end,:));

input = [sorted(:, 1:3) sorted(:,5:10)];
output = sorted(:,4);

[training_in, training_out, testing_in, testing_out] = DataSets(input, output);
rng('default');

% NON REGULARIZED
mdl = fitglm(training_in, training_out, 'Distribution', 'binomial');
scores = predict(mdl, testing_in);
[X,Y,T,AUC] = perfcurve(testing_out, scores, 1);
figure;
plot(X,Y);
xlabel('False positive rate');
ylabel('True positive rate');
title('ROC for Unregularized Logistic Regression');

%Errors
training_scores = predict(mdl, training_in);
training_error = mean((training_scores >= 0.5) ~= training_out);
testing_error = mean((scores >= 0.5) ~= testing_out);

fprintf('Unregularized Logistic Regression Statistics\n');
fprintf('Training error: %f%%\nTest error: %f%%\n', training_error * 100, testing_error * 100);
fprintf('AUC value: %f\n\n', AUC);

%REGULARIZED (Lasso)
[mdl_reg,FitInfo] = lassoglm(training_in, training_out, 'binomial', 'CV', 3);
weights = mdl_reg(:, FitInfo.IndexMinDeviance);
scores_reg = testing_in * weights + FitInfo.Intercept(FitInfo.IndexMinDeviance);
scores_reg = 1 ./ (1 + exp(-scores_reg));
[X_reg,Y_reg,T_reg,AUC_reg] = perfcurve(testing_out, scores_reg, 1);
figure;
plot(X_reg,Y_reg);
xlabel('False positive rate');
ylabel('True positive rate');
title('ROC for Regularized Logistic Regression');

%Errors
training_scores_reg = training_in * weights + FitInfo.Intercept(FitInfo.IndexMinDeviance);
training_scores_reg = 1 ./ (1 + exp(-training_scores_reg));
training_error_reg = mean((training_scores >= 0.5) ~= training_out);
testing_error_reg = mean((scores_reg >= 0.5) ~= testing_out);

fprintf('Regularized Logistic Regression Statistics\n');
fprintf('Training error: %f%%\nTest error: %f%%\n', training_error_reg * 100, testing_error_reg * 100);
fprintf('AUC value: %f\n', AUC_reg);