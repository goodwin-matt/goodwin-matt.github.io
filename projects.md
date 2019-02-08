---
layout: page
title: Projects
docurl: test/test.pdf
---

__Bayesian Compressive Sensing - Master's Thesis__
<br/>

I find Bayesian statistics and compressive sensing to both be very fascinating subjects and was fortunate enough to work on the intersection of these two areas for my masters thesis. The main goal of my research was to use Bayesian compressive sensing to characterize nonlinear chirp signals provided by Los Alamos National Laboratories. 

A byproduct of that work however was developing an R package using Rcpp and submitting it to CRAN. As of this writing the package is no longer on CRAN because of some issues with working on Solaris computers but I hope to get to it someday (I'll be honest - probably never unless someone contacts me about it). 

In the meantime the code works just fine and can be accessed on github [here](https://github.com/goodwin-matt/bcs). My thesis can be accessed [here][1] in pdf format.
 

[1]:{{ site.url }}/pdfs/master_final.pdf


**Predicting Cell Phone Switchers**

Project I worked on with Nate Klyn at Oracle Data Cloud. Because it is proprietary information I can't go into too much detail, but Nate wrote a great blog post about the project on [DataScience.com](https://www.datascience.com/blog/oracle-data-science-case-study-in-telecom) if you are interested in a broad overview.

**Reinforcement learning in the game Halite using deep q-learning**

This was part of a hackathon I did at work with a colleague. We both wanted to learn more about reinforment learning and how to apply it to this online AI game called Halite that my colleague found (see [here](https://halite.io) for game). We found this great [blog](https://keon.io/deep-q-learning/) that implemented deep-q learning for the CartPole game and wanted to apply the [code](https://github.com/keon/deep-q-learning) to Halite. We never were able to finish the project but learned a lot from the experience and found how powerful reinforcement learning can be. I coded up the deep-q learning tutorial [here][3] in a Jupyter notebook.

[3]:{{ site.url }}/pdfs/Q-learning_tutorial.html

**Walmart Price Checker - Textbook arbitrage**

I heard this great Planet Money [podcast](https://www.npr.org/sections/money/2014/11/10/363103753/textbook-arbitrage-making-money-off-used-books) the other day about some guys who figured out a true arbitrage opportunity with college textbooks. I wanted to see if this was true for myself so I looked into ways of creating a daily cron job that would automatically download the prices of books or other items from Amazon. It wasn't as easy as I would have hoped to do this with Amazon so I switched to Walmart.com. I'm curious to see if I find the same signal they did on Walmart's website so I'd like to update this in the future. The script I use to scrape the Walmart data is given [here][2].

[2]:{{ site.url }}/code/walmart_get_price.py
