from AssociationRule import AssociationRule
from RankRule import RankRule
from RuleSet import RuleSet

if __name__ == '__main__':

    file = open("data/RulesArticle.txt","r")
    fileExit = open("data/RankedRules.txt","w")

    #Reading the input file
    print("Loading file...")
    ruleSet = RuleSet(None)
    for line in file:
        atributes = line.split(';')
        rule = atributes[1]
        measures = [float(atributes[i].rstrip('\n')) for i in range(2, atributes.__len__())]
        ruleSet.appendRule(AssociationRule(rule, measures))

    #Ranking the rules
    print("Creating rank...")
    rankRulesExample = RankRule(ruleSet)

    #Writing output
    print("Creating results file...")
    for rank, rule in enumerate(rankRulesExample.getRankedRules()):
        #fileExit.write(str(rank+1) + ";" + str(rule.joinBy(";")) + "\n")
        fileExit.write(str(rank+1) + ";" + rule.rule + "\n")

    print("Program ended...")