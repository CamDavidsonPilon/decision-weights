Decision Weights in Prospect Theory
================


It's clear that humans are irrational, but how irrational are they? After some research into behavourial economics, I became very interested in Prospect Theory (see Chapter 29 of *Thinking, Fast and Slow*). A very interesting part of Prospect theory is that it is *not* probabilities that are used in the calculation of expected value: 

![ev](http://latex.codecogs.com/gif.latex?E^{\\mathbf{Q}}[&space;Z&space;]&space;=&space;\\sum_{z_i}&space;q_i&space;z_i)

Here, the *q*'s are not the probabilities of outcome *z*, but it is from another probability measure called *decision weights* that humans actually use to weigh outcomes. Using a change of measure, we can observe the relationship between the actual probabilities and the decision weights: 

![cmg](http://latex.codecogs.com/gif.latex?E%5E%7B%5Cmathbf%7BQ%7D%7D%5B%20Z%20%5D%20%3D%20E%5E%7B%5Cmathbf%7BP%7D%7D%5Cleft%5B%20Z%20%5Cfrac%7BdQ%7D%7BdP%7D%5Cright%5D%20%3D%20%5Csum_%7Bz%7D%20p_i%20%5Cleft%28%5Cfrac%7Bq_i%7D%7Bp_i%7D%20z%5Cright%29)

My interest is in this change of measure. 



## The Setup

Suppose you have two choices:

1. Lottery A: have a 1% chance to win $10 000, 
2. Lottery B: have a 99% chance to win $101


Which would you prefer?

Well, under the real world probabilty measure, these two choices are equal: .99 *x* 101 = .01 *x* 10000. Thus a rational agent would be indifferent to either option. But a human would have a preference: they would see one more valuable than the other. Thus:

![inq](http://latex.codecogs.com/gif.latex?E%5E%7B%5Cmathbf%7BP%7D%7D%5B%20Z_1%20%5D%20%3D%20E%5E%7B%5Cmathbf%7BP%7D%7D%5B%20Z_2%20%5D%2C%20%5C%3B%5C%3B%20E%5E%7B%5Cmathbf%7BQ%7D%7D%5B%20Z_1%20%5D%20%3E%20E%5E%7B%5Cmathbf%7BQ%7D%7D%5B%20Z_2%20%5D)

rewritten: 

![inq2](http://latex.codecogs.com/gif.latex?p_1Z_1%20%3D%20p_2Z_2%2C%20%5C%3B%5C%3B%20q_1Z_1%20%3E%20q_2Z_2)

and dividing:

![inq3](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bq_1%7D%7Bp_1%7D%20%3E%20%5Cfrac%7Bq_2%7D%7Bp_2%7D%20%5C%5C%20%5CRightarrow%20%5Cfrac%7BdQ%7D%7BdP%7D%28p_1%29%20%3E%20%5Cfrac%7BdQ%7D%7BdP%7D%28p_2%29)

What's left to do is determine the direction of the first inequality. 

## Mechanical Turk it. 


So I created combinations of probabilities and prizes, all with equal real-world expected value, and asked Turkers to pick which one they preferred. Example:

![Imgur](http://i.imgur.com/KHePN5a.png)

Again, notice that .5 *x* $200 = .8 *x* $125 = $100. The original HIT data and the python scripts that generate are in the repo, plus the MTurk data. Each HIT received 10 turkers. 


**Note:** The Turking cost me $88.40, if you'd like to give back over [Gittip](https://www.gittip.com/CamDavidsonPilon/), that would be great =)
 
**Note:** I called the first choice *Lottery A* and the second choice *Lottery B*.
 
## Analysis

Below is a slightly inappropriate heatmap of the choices people made. If everyone was rational, and hence indifferent to the two choices, the probabilities should hover around 0.5. This is clearly not the case. 

![Imgur](http://i.imgur.com/poAzHxZ.png)
 
What else do we see here?

1. As expected, people are loss averse: every point in the lower-diagonal is where lottery *A* had a high probability of success than *B*. The matrix shows that most points in here are greater than 50%, thus people chose the safer bet more often. 
2. The exception to the above point is the fact that 1% is choosen more favourably over 2%. This is an instance of the *possibility effect*. People are indifferent between 1% and 2%, as they are both so rare, thus will pick the one with larger payoff. 


## FAQ

1. **Why did I ask the Turkers to deeply imagine winning $50 dollars before answering the question?** This was to offset a potential anchoring effect: if a Turkers first choice had prize $10 000, then any other prize would have looked pitiful, as the anchor had been set at $10 000. By having them imagine winning $50 (lower than any prize), then any prize they latter saw would appear better than this anchor. 
 
2. **Next steps?** I'd like to try this again, with more control over the Turkers (have a more diverse set of Turkers on it).


 [This data is mirrored and can be queried via API here](https://www.exversion.com/data/view/RABBVVQ0AQ5137Z)