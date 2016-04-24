from AssociationRule import AssociationRule
from RankRule import RankRule
from RuleSet import RuleSet
from optparse import OptionParser


def ruleSetFromFile(fname):

    file_iterator = open(fname, 'r')
    ruleSet = RuleSet(None)
    for line in file_iterator:
        line = line.strip().rstrip('\n').rstrip('\r') #removing end of line
        atributes = line.split(';')
        id = atributes[0]
        rule = atributes[1]
        measures = [float(atributes[i]) for i in range(2, atributes.__len__())]
        ruleSet.appendRule(AssociationRule(id, rule, measures))
    return ruleSet

if __name__ == '__main__':

    optparser = OptionParser()
    optparser.add_option('-f', '--inputFile',
                         dest='input',
                         help='filename containing csv',
                         default="data/RulesArticle.txt")
    optparser.add_option('-o', '--outputFile',
                         dest='output',
                         help='output file',
                         default="output/RankedRules.txt")
    optparser.add_option('-a', '--withAllMeasuresAndRules',
                         dest='all',
                         help='with all measures and rules',
                         default=None)

    (options, args) = optparser.parse_args()

    ruleSet = ruleSetFromFile(options.input)

    #Ranking the rules
    rankRule = RankRule(ruleSet)
    rankedRules = rankRule.getRankedRules()

    #Writing output
    output = open(options.output,"w")
    for rule in rankedRules:
        if options.all:
            output.write(rule.__str__(withMeasuresAndRule=True)+"\n")
        else:
            output.write(rule.__str__()+"\n")

    print("File {} created.".format(options.output))