# Exam 1 Review

## Topics
1. Min/Max of Function
2. Optimize Under Constraints
3. Crazy Problem Approach
4. Linear Regression

## Examples
1. $$f(x) = x^2e^{-x}$$
2. A boat leaves a dock at 2:00 P.M. and travels due south at a speed of 20 km/h. Another boat has been heading due east at 15 km/h and reaches the same dock at 3:00 P.M. How many minutes past 2:00 P.M. were the boats closest together?
3. Assume that the speed of new computers costing a certain amount of money grows exponentially over time, with the speed doubling every 18 months. Suppose you need to run a very time consuming program and are allowed to buy a new computer costing a fixed amount on which to run the program. If you start now, the program will take 10 years to finish. How long should you delay buying the computer and starting the program so that it will finish in the shortest amount of time from now? Also, what will the shortest finishing time be? 
4. Do a linear regression on some points with random discuss what line means.

## Work

1. Take derivative and set equal to zero.
$$f'(x) = 2xe^{-x} +x^2e^{-x}(-1)$$

$$2xe^{-x} -x^2e^{-x}=xe^{-x}\left(2-x\right)=0$$

So $x = 0$ or $e^{-x} = 0$ or $2-x = 0$.  The middle one is never zero!  

How to find if maximum or minimum?  Check the sign of the derivative.  It is negative below zero, positive from 0 to 2 and negative after 2.  Thus 0 is a minimum and 2 isd a max.

