from RuleSet import RuleSet

class SkyRule(object):

    def __init__(self, R):
        self.sky = [] #Final undominated rules
        self.C = R.copy() #Candidate undominated rules
        self.E = R.copy() #Current undominated rules

    def getUndominatedRules(self):
        while(self.C.rules): #While there are candidates

            rStar = self.C.getrMinDegSim(self.C.getReferenceRule()) #r* <- r of C having min(DegSim(r,reference))
            self.C.removeRule(rStar) #C <- C\{r*}
            Sr = [] #Sr
            self.sky.append(rStar)

            for e in self.E.rules:
                if(rStar.strictlyDominates(e)):
                    self.C.removeRule(e)
                elif(e.strictlyDominatesOneMeasure(rStar)):
                    Sr.append(e)

            self.E = RuleSet(Sr) #New current candidates are only undominated rules that dominates rStar in at least one measure

        return self.sky