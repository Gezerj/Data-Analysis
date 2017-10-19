# -*- coding: utf-8 -*-
"""
Created on Wed Oct 04 10:57:34 2017

@author: Gerwyn
"""

from __future__ import division
import numpy as np
import scipy.stats as sc
from scipy.stats.stats import pearsonr
import matplotlib.pyplot as plt

plt.close("all")

#########################################################

# Question 1

""" 30% and 10% of Republican and Independent voters are, respectively,
behind the change in the law, while 80% of the Democrat voters are in favour. You are visiting the
state, and ask a Police Officer what she thinks of the idea. She says she’s against the change to
the law. What is the probability that she votes Democrat? """

##########################################################


# Finding the number of Democrat, Republican and Independent Voters from the State of Florida

# Source : https://www.nytimes.com/elections/results/florida


# Democrat

VoD = 4504975

# Republican

VoR = 4617886

# Independent

VoI = 81731

# 3 Party Total

To3 = VoD + VoR + VoI

# Others

VoO = 297025

# Total Overall

ToV = VoD + VoR + VoI + VoO


# From the Question we can find the number of voters who would be for and against the change in the law

# Voters Who are For and a Democrat

DVF = 0.8

DF = np.int(DVF*VoD)

# Voters Against and a Democrat

DVFc = (1-DVF)

DFc = np.int(DVFc*VoD)

# Voters Who are For and a Republican

RVF = 0.3

RF = np.int(RVF*VoR)

# Voters Against and a Republican

RVFc = (1-RVF)

RFc = np.int(RVFc*VoR)

# Voters Who are For and a Independent

IVF = 0.1

IF = np.int(IVF*VoI)

# Voters Against and a Independent

IVFc = (1-IVF)

IFc = np.int(IVFc*VoI)


# Average For

AF = (DF + RF + IF)/To3

# Average Against

AA = (DFc + RFc + IFc)/To3


# Others For

OF = np.int(AF*VoO)

# Others Against

OFc = np.int(AA*VoO)


# Total For

TF = DF + RF + IF + OF

# Total Against

TFc = DFc + RFc + IFc + OFc


# Defining our functions

def P(A, B):

    """ Probabibility of geting A out of B """

    return A/B


# Probability of voting Democrat

PD = P(VoD, ToV)

# Probability of voting Against the change

PFc = P(TFc, ToV)


# Probability of Voting against given you vote democrat is just the probability DVFc

PFcgD = DVFc


# Therefore using Bayes Theorem, the probability of voting democrat given your against the change is :-

Probability = (PFcgD*PD)/PFc

print Probability

###################################################

# Question 2

""" Roughly half of its latest batch of CPUs contains a flaw. How many CPUs from the batch would
they need to examine to know the probability that any given CPU is faulty to better than 5%?  """

p = 1/2
a = 0.05

N = 100000

x = np.linspace(0, N, N + 1)

x1 = sc.binom.pmf(x, N, p)

#b = np.min(x[x1 > a])/N






##################################################

# Question 3

""" A group researching cancer have previously found that the genetic marker D3 is a useful
indication that a person will develop the more aggressive form of melanoma skin cancer, in that D3
is present in 65% of the aggressive cases. However the test is expensive. A rival group claim that
the marker M23 is more sensitive than D3, and works out considerably cheaper to test for. The
rival research team manage to get DNA samples from 7 patients with the aggressive form of the
disease, all of whom test positive for the genetic marker M23. Based on these results, is M23 a
better marker for the disease than D3?  """






###################################################

# Question 4

""" Eight new recruits for a rugby team are timed in both the 100 meters and 1,500 to assess
their athletic abilities """

# Source : https://stackoverflow.com/questions/3949226/calculating-pearson-correlation-and-significance-in-python

# And : https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.corrcoef.html

hm = np.array([12, 11, 13, 14, 12, 15, 12, 16])
tm = np.array([280, 290, 220, 260, 270, 240, 250, 230])

mhm = np.mean(hm)
mtm = np.mean(tm)

r = np.sum((hm - mhm)*(tm - mtm))/np.sqrt((np.sum((hm - mhm)**2))*(np.sum((tm - mtm)**2)))

print "P8(|r| >",-r ,") = 5.3 %"

# Or use an inbuilt function

pr = pearsonr(hm, tm)

print "P8(|r| >",-pr[0] ,") = ", pr[1]*100, "%"


plt.plot(hm, tm, color='black', linestyle='None', marker='.')

#####################################################

# Question 5

""" Using only a uniform random number generator, compute your own table of significance
values for linear correlation coefficient r. Do not use the analytic expression for r """

n = 20

xTrial = np.random.uniform(0, 1, n)

yTrial = np.random.uniform(0, 1, n)

Prop = []

tP = pearsonr(xTrial, yTrial)

for i in xrange(len(xTrial)):

    sumT = np.sum(xTrial)

    if xTrial[i] > np.abs(tP[0]) and xTrial[i] < 1 - np.abs(tP[0]):

        Prop.append(xTrial[i])

    R = np.sum(Prop)/sumT

print R
print tP






plt.show()