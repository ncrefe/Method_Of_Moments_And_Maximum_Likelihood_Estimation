# Method of Moments and Maximum Likelihood Estimation
a) MoM and MLE Estimation

Estimate the parameter θ using Method of Moments (MoM) and Maximum Likelihood Estimation (MLE) for the distribution with the following density:
```
 f(x) = θ * (x^(θ-1)) , 0<x<1
        0 , otherwise
```
Apply findings to X = {0.3, 0.6, 0.8, 0.9} and calculate the two estimates for this sample
set.
- In code, implement the two functions which take a sample set X and return the calculated
estimate of the parameter θ using MoM and MLE. Call these two functions to calculate the
estimates for the same X given above and print the results.

- Implement a function that takes the population (P) and sample size (N) as its
input, uses 100000 samples of size N from the population P to calculate MoM and MLE
estimates of the parameter θ from. Use np.random.random_integers to create indices for
random sampling. After plotting the histograms of both estimators in a single figure (use 100
bins and alpha=0.5 ), it returns the mean and the variance of the two estimators.
Call the implemented function for N = [1,2,3,4,5,10,50,100,500,1000]. Print the estimator mean
and variances for each N.
