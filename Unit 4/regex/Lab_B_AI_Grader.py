# Nicole Kim, 2/5/2019, edited on 2/3/2021

'''In Q40-42, An Othello board is any string of length 64 made up of only the characters in "xX.Oo".  
An Othello edge is any string of length 8 made up of only the characters in "xX.Oo".'''

def num_40(subject):
   # Write a regular expression that will match on an Othello board represented as a string. 
   pattern = "/^[xo.]{64}$/i"  #notice that python does not want / /
   return pattern

def num_41(subject):
   # Given a string of length 8, determine whether it could represent an Othello edge with exactly one hole.
   pattern = "/^[xo]*\.[xo]*$/i"
   return pattern

def num_42(subject):
   # Given an Othello edge as a string, determine whether there is a hole such that if X plays to the hole (assuming it could), 
   # it will be connected to one of the corners through X tokens. Specifically, this means that one of the ends must be a hole, 
   # or starting from an end there is a sequence of at least one x followed immediately by a sequence (possibly empty) of o, 
   # immediately followed by a hole.
   pattern = "/^\.o*x|xo*\.$/i"
   return pattern

def num_43(subject):
   # Match on all strings of odd length.
   pattern = "/^(..)*.$/"
   return pattern

def num_44(subject):
   # Match on all odd length binary strings starting with 0, and on even length binary strings starting with 1.
   pattern = "/^(0|1[01])([01]{2})*$/"
   return pattern

def num_45(subject):
   # Match all words having two adjacent vowels that differ.
   pattern = "/\w*(a[eiou]|e[aiou]|i[aeou]|o[aeiu]|u[aeio])\w*/i"
   return pattern

def num_46(subject):
   # Match on all binary strings which DO NOT contain the substring 110.
   pattern = "/^(0*10)*0*1*$/"
   return pattern

def num_47(subject):
   # Match on all non-empty strings over the alphabet {a, b, c} that contain at most one a.
   pattern = "/^(a[bc]*|[bc]+a?[bc]*)$/"
   return pattern

def num_48(subject):
   # Match on all non-empty strings over the alphabet {a, b, c} that contain an even number of a's.
   pattern = "/^[bc]*(a[bc]*a[bc]*)*$/"
   return pattern

def num_49(subject):
   # Match on all positive, even, base 3 integer strings. 
   pattern = "/^[02]*(1[02]*1[02]*)*$/"
   return pattern

import sys;
args = sys.argv[1:]
idx = int(args[0])-40

print(eval("num_" + args[0])(""))