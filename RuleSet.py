from AssociationRule import AssociationRule

class RuleSet(object):
    def __init__(self, rules):
        if not rules:
            self.rules = []
        else:
            self.rules = rules

    def appendRule(self, rule):
        self.rules.append(rule)

    def getReferenceRule(self):
        reference = list(self.rules[0].measures)
        for r in self.rules:
            for i in range(r.len):
                reference[i] = max(r.measures[i], reference[i])
        return AssociationRule(-1, "REFERENCE",reference)

    def getrMinDegSim(self, reference):
        bestDegSim = reference.degSim(self.rules[0])
        rStar = self.rules[0]
        for r in self.rules:
            auxDegSim = reference.degSim(r)
            if(auxDegSim < bestDegSim): #lower is better
                bestDegSim = auxDegSim
                rStar = r
        return rStar

    def removeRule(self, rule):
        self.rules.remove(rule)

    def copy(self):
        return RuleSet(self.rules.copy())