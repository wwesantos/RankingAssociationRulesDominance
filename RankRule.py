from RuleSet import RuleSet
from SkyRule import SkyRule

class RankRule(object):

    def __init__(self, R):
        self.R = R.copy()

    def getUndominatedSets(self):
        Ep = []
        while(self.R.rules):
            sky = SkyRule(self.R)
            undominated = sky.getUndominatedRules()
            Ep.append(undominated)
            for r in undominated:
                self.R.removeRule(r)
        return Ep

    def getRankedRules(self):
        return [r for e in self.getUndominatedSets() for r in e]