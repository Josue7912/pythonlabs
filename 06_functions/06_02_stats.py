'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(numlist):
  # define the function here
  maximum = max(numlist)
  minimum = min(numlist)
  average = sum(numlist) / len(numlist)
  summ = sum(numlist)
  return maximum, minimum, average, summ

# call the function below here

print(stats(example_list))