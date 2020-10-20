#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 21:17:56 2019

@author: karenkerwin
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Karen Kerwin
# Section:      535
# Assignment:   Lab 6b
# Date:         09 October 2019
#

#  key point and slope variables:
a_x = 0  #  the "O" on the graph
a_y = 0  #  the "O" on the graph

b_x = 0.015 #  strain value (x) of point B
b_y  = 44   #  stress value (y) of point B

c_x  = 0.06 #  strain value (x) of point C
c_y = 44    #  stress value (y) of point C

d_x = 0.18 #  strain value (x) of point D
d_y = 60   #  stress value (y) of point D

e_x = 0.27 #  strain value (x) of point E
e_y = 52   #  stress value (y) at point E, in which the structural steel fractures.

slope_ab = (b_y - a_y) / (b_x - a_x)  #  Young's Modulus / linear elastic

slope_bc = (c_y - b_y) / (c_x - b_x)  #  plastic slope

slope_cd = (d_y - c_y) / (d_x - c_x) #  strain hardening slpoe

slope_de = (e_y - d_y) / (e_x - d_x) #  necking slope

print('This program will calculate stress on a steel fracture for a given strain.')

strain = float(input('Please enter the value of strain of interest. '))
while strain < 0:
    strain = float(input('Error. Please enter a positive strain value of interest. '))


#  conditional if statement regarding the 'category' of the strain and the output of stress:
if strain >= 0 and strain < 0.015:
    category = 'linear elsatic'
    stress = b_y - (slope_ab) * (b_x - strain)
elif strain >= 0.015 and strain < 0.06:
    category = 'plastic'
    stress = c_y - (slope_bc) * ( c_x - strain)
elif strain >= 0.06 and strain < 0.18:
    category = 'hardening'
    stress = d_y - (slope_cd) * ( d_x - strain)
elif strain == 0.18:
    category = 'hardening'
    stress = d_y - (slope_cd) * ( d_x - strain)
    print('This is the point of maximum strength.')
elif strain >= 0.18 and strain < 0.27:
    category = 'necking'
    stress = e_y - (slope_de) * ( e_x - strain)
else:
    stress = 0  #  couldn't figure out how to make this a string? Not sure if that was necesary since the category can say it is fractured anyway. Technically there is no stress since its broken anyway 0_o ? let me know!
    category = 'fractured'



print('The stress is %.2f'  %stress , 'and is in the' , category , 'phase.')