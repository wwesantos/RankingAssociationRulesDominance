from SkyRule import SkyRule

class RankRule(object):

    def __init__(self, ruleSet):
        self.R = ruleSet.copy()

    def getUndominatedSets(self):
        Ep = []
        while(self.R.rules):
            skyRule = SkyRule(self.R)
            undominatedRules = skyRule.getUndominatedRules()
            Ep.append(undominatedRules)
            for r in undominatedRules:
                self.R.removeRule(r)
        return Ep

    def getRankedRules(self):
        return [rule for ep in self.getUndominatedSets() for rule in ep]