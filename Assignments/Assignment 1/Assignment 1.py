# -*- coding: utf-8 -*-
"""
Created on Wed Oct 04 10:57:34 2017

@author: Gerwyn
"""

from __future__ import division

import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.special import factorial
from scipy.stats.stats import pearsonr

plt.close('all')

#########################################################

# Question 1

""" 30% and 10% of Republican and Independent voters are, respectively,
behind the change in the law, while 80% of the Democrat voters are in favour. You are visiting the
state, and ask a Police Officer what she thinks of the idea. She says she’s against the change to
the law. What is the probability that she votes Democrat? """

# Finding the number of Democrat, Republican and Independent Voters from the State of Florida

# Source : https://www.nytimes.com/elections/results/florida

print("Question 1 :- ")

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

print('P(D|Fc) =', Probability)

###################################################

# Question 2

""" Roughly half of its latest batch of CPUs contains a flaw. How many CPUs from the batch would
they need to examine to know the probability that any given CPU is faulty to better than 5%?  """

print("Question 2 :- ")

p = 1/2
a = 0.05   # error in our accuracy
t = 0.98   # t value (95% confidence)

n_cpu = (t/a)**2*(1-p)*(p)

print("Number of CPU for the probability that any given CPU is faulty to better than 5% is", n_cpu)


# OR

""" IGNORE BELOW """

def B_trial(p, a):

    N = 1

    while True:

        H = np.int(N/2)

        fact = math.factorial(N)/(math.factorial(H)*math.factorial(N - H))

        B = fact*(p**(N/2))*((1-p)**(N-(N/2)))

        if B <= a:

            print B

            break

        else :

            N += 1

    return N


n_trial = B_trial(p, a)

print("Number of CPU for the probability that any given CPU is faulty to better than 5% is", n_trial)

##################################################

# Question 3

""" A group researching cancer have previously found that the genetic marker D3 is a useful
indication that a person will develop the more aggressive form of melanoma skin cancer, in that D3
is present in 65% of the aggressive cases. However the test is expensive. A rival group claim that
the marker M23 is more sensitive than D3, and works out considerably cheaper to test for. The
rival research team manage to get DNA samples from 7 patients with the aggressive form of the
disease, all of whom test positive for the genetic marker M23. Based on these results, is M23 a
better marker for the disease than D3?  """

print("Question 3 :- ")


def B(N, p, v):

    if type(v) == int:

        T = np.linspace(0, N, N+1)

        fact = factorial(N)/(factorial(T)*factorial(N-T))

        B = fact*(p**T)*((1-p)**(N-T))

        Bino = np.sum(B[T >= v])

    else:

        Bino = np.zeros(len(v))

        for i in range(len(v)):

            fact = factorial(N)/(factorial(v[i])*factorial(N-v[i]))

            Bino[i] = fact*(p**v[i])*((1-p)**(N-v[i]))

    return Bino


NB = 7

pb = 0.65

s = 7

print("P(7, 0.65, 7) =", B(NB, pb, s))

# Plot of binomial

plt.figure()

v = np.linspace(0, NB, 100)

p = B(NB, pb, v)

plt.plot(v, p)

plt.xlabel(r'$ \nu $')
plt.ylabel(r'$ P_{7,0.65} (\nu) $')

###################################################

# Question 4

""" Eight new recruits for a rugby team are timed in both the 100 meters and 1,500 to assess
their athletic abilities """

# Source : https://stackoverflow.com/questions/3949226/calculating-pearson-correlation-and-significance-in-python

# And : https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.corrcoef.html

# And : http://www.socscistatistics.com/pvalues/Default.aspx

print("Question 4 :- ")

x_Data = np.array([12, 11, 13, 14, 12, 15, 12, 16])
y_Data = np.array([280, 290, 220, 260, 270, 240, 250, 230])


def R(x_Data, y_Data):

    Mean_x_Data = np.mean(x_Data)
    Mean_y_Data = np.mean(y_Data)

    r = np.sum((x_Data - Mean_x_Data)*(y_Data - Mean_y_Data))/np.sqrt((np.sum((x_Data - Mean_x_Data)**2))*(np.sum((y_Data - Mean_y_Data)**2)))

    return r


r = R(x_Data, y_Data)

print("r = ", r)

print("P8(|r| >", np.abs(r), ") = 5.706 %, using analytical function for r and an online p-value calculator")

# Or use an inbuilt function

pr = pearsonr(x_Data, y_Data)

print("P8(|r| >", np.abs(pr[0]), ") = ", pr[1]*100, "%, using an inbuilt function for both r and p-value")

# Plotting data points

plt.figure()

p_coeff,residuals,_,_,_= np.polyfit(x_Data, y_Data, 1, full=True)

p = np.poly1d(p_coeff)

x_trial = np.linspace(np.min(x_Data), np.max(x_Data), 100)

plt.plot(x_trial, p(x_trial), color='blue')

plt.plot(x_Data, y_Data, color='black', linestyle='None', marker='.')
plt.xlabel("100m")
plt.ylabel("1500m")

#####################################################

# Question 5

""" Using only a uniform random number generator, compute your own table of significance
values for linear correlation coefficient r. Do not use the analytic expression for r """

print("Question 5 :- ")

N = np.linspace(3, 10, 8)

num = 10000  # Number of trials used to increase the accuracy of our results


def P_r(N, num):

    # Creating our 2d array for r values

    r = np.zeros((len(N), num))

    for i in range(len(N)):

        for j in range(num):

            # Creating random sets of numbers of length N

            X = np.random.uniform(0, 1, np.int(N[i]))
            Y = np.random.uniform(0, 1, np.int(N[i]))

            # Using the function created in Question 4 to find our values of r

            r[i, j] = np.abs(R(X, Y))  # Finding the positive values of r so the calculations later can be coded easier

    return r


r = P_r(N, num)


def table(N, r):
    print("Table of probability of correlation due to chance")

    print("           r     =     0,    0.1,    0.2,   0.3,   0.4,   0.5,   0.6,   0.7,   0.8,   0.9,   1")

    # Critical value r0

    r0 = np.linspace(0, 1, 11)

    # Probability P

    P = np.zeros((len(N), len(r0)))

    for i in range(len(N)):

        for j in range(len(r0)):

            # The probability of r being greater than a critical value r0

            P[i, j] = np.int64((len(r[i, :][r[i, :] > r0[j]])/num)*100)

        print("N = ", N[i], P[i, :])

    return P


P_Corr = table(N, r)

plt.show()