---
layout: post
title:  "Bayes Meet Covid"
date:   2020-12-01 22:11:46 -0600
categories: Bayes
---

In November, I had a relative test negative for COVID-19 which was a huge surprise to me considering her husband 
had just tested positive. I thought there was no way she *didn't* have covid! 
I assumed it was a faulty test. But as I thought about it I realized...

*Bayes Theorem!*

To all those students in college who complained "when will we ever use this..." well here it is.

As my math teacher once said, if you're going to get a tattoo 
consider getting Bayes theorem on your arm:

{% raw %}
$$ P(B|A) = \frac{P(A|B)P(B)}{P(A|B)P(B) + P(A|\sim B)P(\sim B)} $$
{% endraw %}

Let's assume B is the event my relative has covid and A is the event 
she gets a negative covid test. So $P(B|A)$ is the probability she has covid given 
she had a negative test. Lets break down the formula:

$P(A|B)$  -->  probability she got a negative test given she has covid. 
This would be the false negative rate of the test. The test she used is a "NAAT" test 
and what I was able to find for false negative ranges from 5-40%. Let's stick with 
5% for now.

$P(B)$ --> this is the prior probability, or our initial estimate of 
the probability she has covid in the first place. Two thoughts here. One idea is we could take 
how many people have covid in Utah up to today and divide by the 
population of Utah, roughly simulating the probability that someone 
we randomly choose in Utah has covid. There are about 180k cumulative covid cases 
and roughly 3.2 million Utahans. Therefore 

$$\frac{180000}{3206000} = 0.056$$

The other thought is based on [this news article](https://www.ksl.com/article/50014798/university-of-utah-study-odds-of-catching-covid-19-from-someone-at-home-is-12) citing a couple of recent medical 
studies. The "risk for infection between spouses was 43%" and surprisingly 
for non-spousal relationship in the same home its only 12%. So another option is 
$P(B) = 0.43$.

$P(A|\sim B)$ --> Given my relative doesn't have covid, probability of 
a negative test, or 1 - false positive. This should be high, lets say 0.99.

Putting it all together with the first prior we suggested:

{% raw %}
$$ P(B|A) = \frac{(0.05)(0.056)}{(0.05)(0.056) + (0.99)(1-0.056)} = 0.00299$$
{% endraw %}

So given a negative covid test, my relative has only a 0.3% chance 
of actually having covid. But let's use the second prior we suggested 
which would seem more realistic (43% chance she has it) and lets 
say the false negative rate is higher (say 20%).

{% raw %}
$$ P(B|A) = \frac{(0.2)(0.43)}{(0.2)(0.43) + (0.99)(1-0.43)} = .132$$
{% endraw %}

Amazingly my relative still only as a 13.2% chance of actually having covid
given a negative covid test!

It was fun to share this with my relative and also alleviate some general doubts about her 
negative test result. Another win for Bayes theorem. 







