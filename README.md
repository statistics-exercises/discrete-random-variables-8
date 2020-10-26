# Plotting Geometric random variables

Now that you can write a function to generate geometric random varibles lets make a scatter plot for this type of random variable.  For this exercise you will need to generate 100 geometric random variables and drawing a graph showing the values of all these random variables.

To complete this exercise you will need to:  

- Write a function called `geometric` that takes  `p` (the probability of success) as an argument using what you learned in the previous exercise.

- Use this function and what you know about loops and lists to generate a list called `random_variables` that contains 100 geometric random variables all of which have the p parameter set to the global variable `prob`.

I have included code in the cell on the left that will plot your list of random variables.  To get this code to work, however, you will need to write a second list called `indices` that contains a numerical index for each of these random variables.  The first of these indices should be equal to one, the second should be equal to two, the third should be three and so on.  
