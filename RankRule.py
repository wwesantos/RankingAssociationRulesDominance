from SkyRule import SkyRule

class RankRule(object):

    def __init__(self, ruleSet):
        self.R = ruleSet.copy()

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
        return [rule for ep in self.getUndominatedSets() for rule in ep]