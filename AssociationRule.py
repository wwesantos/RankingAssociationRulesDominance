class AssociationRule(object):
    def __init__(self, rule, measures):
        try:
            if not measures or not rule:
                raise ValueError
            self.measures = tuple([float(x) for x in measures])
            self.len = len(measures)
            self.rule = rule

        except ValueError:
            raise ValueError('The measures and the rule must be nonempty')

        except TypeError:
            raise TypeError('The measures must be an vector')

    def __str__(self):
        return '{} = {}'.format(self.rule, self.measures)

    def joinBy(self, char):
        return self.rule + ";" + char.join([str(m) for m in self.measures])

    #Degree of similarity
    def degSim(self,r2):
        return sum([abs(x-y) for x,y in zip(self.measures, r2.measures)])/self.len

    #Dominates = True of all measures of self are greather or equal than measures in r2
    def dominates(self, r2):
        for x,y in zip(r2.measures, self.measures):
            if (x>y): return False
        return True

    #Strictly Dominates = Dominates and there is at least measure in self that is better than in r2
    def strictlyDominates(self, r2):
        if(self.dominates(r2) and self.strictlyDominatesOneMeasure(r2)):
            return True
        return False

    #Strictly in one measure
    def strictlyDominatesOneMeasure(self, r2):
        for x,y in zip(self.measures, r2.measures):
            if (x>y): return True
        return False