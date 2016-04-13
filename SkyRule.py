from RuleSet import RuleSet

class SkyRule(object):

    def __init__(self, ruleSet):
        self.sky = [] #Final undominated rules
        self.C = ruleSet.copy() #Candidate undominated rules
        self.E = ruleSet.copy() #Current undominated rules
        self.referenceRule = ruleSet.getReferenceRule()

    def getUndominatedRules(self):
        while(self.C.rules): #While there are candidates
            rStar = self.C.getrMinDegSim(self.referenceRule) #r* <- r of C having min(DegSim(r,reference))
            self.C.removeRule(rStar) #C <- C\{r*}
            Sr = RuleSet(None) #Sr
            self.sky.append(rStar)
            
            for e in self.E.rules:
                if(rStar.strictlyDominates(e)):
                    self.C.removeRule(e)
                elif(e.strictlyDominatesOneMeasure(rStar)):
                    Sr.appendRule(e)

            self.E = Sr #New current candidates are only undominated rules that dominates rStar in at least one measure

        return self.sky