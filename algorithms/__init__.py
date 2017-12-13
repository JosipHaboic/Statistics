'''
How to choose the right algorithm
With all the different algorithms in table 1.2, how can you choose which one to use?
First, you need to consider your goal. What are you trying to get out of this? (Do you
want a probability that it might rain tomorrow, or do you want to find groups of voters
with similar interests?) What data do you have or can you collect? Those are the big
questions. Let’s talk about your goal.
If you’re trying to predict or forecast a target value, then you need to look into
supervised learning. If not, then unsupervised learning is the place you want to be. If
you’ve chosen supervised learning, what’s your target value? Is it a discrete value like
Yes/No, 1/2/3, A/B/C, or Red/Yellow/Black? If so, then you want to look into classification. If the target value can take on a number of values, say any value from 0.00
to 100.00, or -999 to 999, or + to -, then you need to look into regression.
If you’re not trying to predict a target value, then you need to look into unsupervised learning. Are you trying to fit your data into some discrete groups? If so and
that’s all you need, you should look into clustering. Do you need to have some numerical estimate of how strong the fit is into each group? If you answer yes, then you probably should look into a density estimation algorithm.
'''