from pyparsing import *

key = Word(alphanums)('key')

equals = Suppress('=')

value = Word(alphanums)('value')

keyValueExpression = key + equals + value

with open('test.csv') as address_file:
  address_file = address_file.read()


for adrs in keyValueExpression.scanString(address_file):
  result = adrs[0]


print("{0} is {1}".format(result.key, result.value))