from AssociationRule import AssociationRule
from RankRule import RankRule
from RuleSet import RuleSet
from optparse import OptionParser
import sys

if __name__ == '__main__':

    file = open("data/RulesArticle.txt","r")
    #file = open("data/MedidasO.2-4.txt","r")
    fileExit = open("data/RankedRules.txt","w")

    #Reading the input file
    print("Loading file...")
    ruleSet = RuleSet(None)
    for line in file:
        atributes = line.split(';')
        id = atributes[0]
        rule = atributes[1]
        measures = [float(atributes[i].rstrip('\n').rstrip('\r')) for i in range(2, atributes.__len__())]
        ruleSet.appendRule(AssociationRule(id, rule, measures))

    #Ranking the rules
    print("Creating rank...", end="")
    rankRule = RankRule(ruleSet)
    rankedRules = rankRule.getRankedRules()

    #Writing output
    print("Creating results file...")
    for rule in rankedRules:
        #fileExit.write(str(rank+1) + ";" + str(rule.joinBy(";")) + "\n")
        fileExit.write(rule.__str__()+"\n")

    print("Program ended...")