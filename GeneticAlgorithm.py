#!/usr/bin/env python
import AIS
import random
import numpy as np
import math
import decimal
from sklearn.neighbors import KDTree

ais_instance1=AIS.Ais()
class GeneticAlgorithm:
    def __init__(self):
       pass

    def fitnesstest(self,individual,self_distance_tree,self_radius):
        dist,ind=self_distance_tree.query([individual], k=2, return_distance=True)
        print("individual's distance is", dist[0][1])
        p=float(self_radius)/(dist[0][1])
        f=math.exp(-p)
        return f




    def fitness(self,individual,normal,perc_match):

        """
        :param normal: the list of self samples
        :param perc_match: an intger 1-100
        :return: the value 0-1
        """
        p=(perc_match/float(100))*len(individual)
        #print "p",pp_mutation=1.0/len(self[0])
        #print len(individual)
        perc_num_of_feat=int(round(p,0))
        match=0
        for individuals in normal:
            ans=(individual[0:perc_num_of_feat]==individuals[0:perc_num_of_feat])
            #print individual[0:perc_num_of_feat],individuals[0:perc_num_of_feat]
            if ans==True:
                match=match+1
        p=match/float(len(normal))
        #print "p is ",p
        f=math.exp(-p)
        return f

    def crossover(self,parent1,parent2,crossover_point,p_crossover):
        """
        :param parent1: first parent with best fitness
        :param parent2: second parent with second best fitness
        :param p_crossover: the probability of crossover
        :return: a child after performing single point crossover
        """
        child_pair=[]
        if random.random()>=p_crossover:
            print("no crossover for child 1")
            child_pair.append(parent1)
        else:
            child1=parent2[0:crossover_point]+parent1[crossover_point:]
            child_pair.append(child1)
            print("crossover for child 1")
        if random.random()>=p_crossover:
            child_pair.append(parent2)
            print("no crossover for child 2")
        else:
            child2=parent1[0:crossover_point]+parent2[crossover_point:]
            child_pair.append(child2)
            print("crossover for child 2")

        return child_pair #np.array(child)

    def mutate(self,child,p_mutation,set_to_choose_from=0):
        """
        :param child: the child list pair to be mutated
        :param location: the index of feature to mutate
        :param p_mutation: probability of mutation
        :param round_off: how many decimal points we want to round up to
        :param set_to_choose_from: set containing the range of value to mutate with
        :return: choose a item from the given set range and replace the value at location
        """
        rg=range(len(child[0]))
        #location=random.choice(rg)
        #round_off=decimal.Decimal(child[0][location]).as_tuple().exponent*(-1)
        child_mut_pair=[]
        if random.random()<p_mutation:
            location=random.choice(rg)
            #to automatically detect the no of decimal points in a float we us
            round_off=decimal.Decimal('%s'%(child[0][location])).as_tuple().exponent*(-1)
            child[0][location]=round(np.random.random(),round_off)
            child_mut_pair.append(child[0])
            print("mutation for child 1")
        else:
            child_mut_pair.append(child[0])
            print("no mutation for child 1")
        if random.random()<p_mutation:
            location=random.choice(rg)
            #to automatically detect the no of decimal points in a float we us
            round_off=decimal.Decimal('%s'%(child[1][location])).as_tuple().exponent*(-1)
            child[1][location]=round(np.random.random(),round_off)
            child_mut_pair.append(child[1])
            print("mutation for child 2")
        else:
            child_mut_pair.append(child[1])
            print("no mutation for child 2")

        return child_mut_pair
