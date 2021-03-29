import json
from random import choice
from argparse import ArgumentParser


with open('n.json') as n, open('adjective.json') as a:
  noun = json.load(n)
  adj = json.load(a)

  n.close()
  a.close()

def generate(number=None, seperator=' ', color=True):
  """ Generate a codename with an adjective and noun"""
 
  if number != None:
    for _ in range(number):
      print(seperator.join([choice(adj), choice(noun)]).title())
  else:
    for _ in range(20):
      print(seperator.join([choice(adj), choice(noun)]).title())


  if seperator:
    print(seperator.join([choice(adj), choice(noun)]).title())
