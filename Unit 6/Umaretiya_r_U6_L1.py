import sys; args = sys.argv[1:]

# Name: Rushil Umaretiya
# Date: 4-29-2021

import os, math

def transfer(t_funct, input_val):
   x = sum(input_val)
   functions = {
      'T1': x,
      'T2': 0 if x <= 0 else x,
      'T3': 1 / (1 + math.e ** -x),
      'T4': -1 + 2/(1+math.e**-x)
   }
   if t_funct in functions:
      return functions[t_funct]
   raise Exception('That is not a valid transfer function.')

def dot_product(input_vals, weights, layer):
   return [[input_vals[weight] * weights[layer][cell_num][weight] for weight in range(len(weights[layer][cell_num]))] for cell_num in range(len(weights[layer]))]

def evaluate(file, input_vals, t_funct):
   with open(file, 'r') as weight_file:
      # had to do this because ai grader is weird
      raw_lines = [[float(weight) for weight in layer.split()] for layer in weight_file.read().split('\n')]
      lines = [line for line in raw_lines if len(line) != 0]


   weights = []

   for i in range(len(lines)):
      if (i == 0):
         cells = len(input_vals)
      else:
         cells = len(weights[i - 1])
      
      cell_weight = []

      for cell in range(len(lines[i]) // cells):
         weight = lines[i][cell * cells : (cell + 1) * cells]
         cell_weight.append(weight)
      
      weights.append(cell_weight)
   
   layer = 0
   while (layer < len(weights) - 1):
      weighted_input = dot_product(input_vals, weights, layer)
      input_vals = []
      for input_val in weighted_input:
         input_vals.append(transfer(t_funct, input_val))
      layer += 1

   output = []
   
   for i in range(len(weights[layer][0])):
      output.append(weights[layer][0][i] * input_vals[i])

   return output

def main():
   args = sys.argv[1:]
   file, inputs, t_funct, transfer_found = '', [], 'T1', False
   for arg in args:
      if os.path.isfile(arg):
         file = arg
      elif not transfer_found:
         t_funct, transfer_found = arg, True
      else:
         inputs.append(float(arg))
   if len(file)==0: exit("Error: Weights file is not given")
   li = (evaluate(file, inputs, t_funct))
   for x in li:
      print (x, end=' ')
if __name__ == '__main__': main()