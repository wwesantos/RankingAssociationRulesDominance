import unittest
from AssociationRule import AssociationRule
from RuleSet import RuleSet
from SkyRule import SkyRule
from RankRule import RankRule

class TestRuleRankMethods(unittest.TestCase):

    def test_get_ranked_rules(self):
        rulesArticle = RuleSet([
            AssociationRule(1, "r1: a→d", [0.20, 0.67, 0.02]),AssociationRule(2, "r2: b→c", [0.10, 0.50, 0.00]),
            AssociationRule(3, "r3: b→d", [0.10, 0.50, 0.02]),AssociationRule(4, "r4: c→d", [0.20, 0.40, 0.10]),
            AssociationRule(4, "r5: d→a", [0.20, 0.33, 0.02]),AssociationRule(6, "r6: d→c", [0.20, 0.33, 0.10]),
            AssociationRule(5, "r7: c→b", [0.10, 0.20, 0.01]),AssociationRule(8, "r8: d→b", [0.10, 0.17, 0.02])
        ])
        rankRules = RankRule(rulesArticle)
        rank = rankRules.getRankedRules()
        self.assertTrue(rank[0] == rulesArticle.rules[0] and
                        rank[1] == rulesArticle.rules[3] and
                        rank[2] == rulesArticle.rules[5] and
                        rank[3] == rulesArticle.rules[2] and
                        rank[4] == rulesArticle.rules[1] and
                        rank[5] == rulesArticle.rules[4] and
                        rank[6] == rulesArticle.rules[6] and
                        rank[7] == rulesArticle.rules[7])

class TestSkyRuleMethods(unittest.TestCase):

    def test_undominates_ep1(self):
        rulesArticle = RuleSet([
            AssociationRule(1, "r1: a→d", [0.20, 0.67, 0.02]),AssociationRule(2, "r2: b→c", [0.10, 0.50, 0.00]),
            AssociationRule(3, "r3: b→d", [0.10, 0.50, 0.02]),AssociationRule(4, "r4: c→d", [0.20, 0.40, 0.10]),
            AssociationRule(5, "r5: d→a", [0.20, 0.33, 0.02]),AssociationRule(6, "r6: d→c", [0.20, 0.33, 0.10]),
            AssociationRule(7, "r7: c→b", [0.10, 0.20, 0.01]),AssociationRule(8, "r8: d→b", [0.10, 0.17, 0.02])
        ])
        sky = SkyRule(rulesArticle)
        undominated = sky.getUndominatedRules()
        self.assertTrue(undominated[0]==rulesArticle.rules[0] and undominated[1] == rulesArticle.rules[3])

    def test_undominates_ep2(self):
        rulesArticle = RuleSet([
            AssociationRule(1, "r1: a→d", [0.20, 0.67, 0.02]),AssociationRule(2, "r2: b→c", [0.10, 0.50, 0.00]),
            AssociationRule(3, "r3: b→d", [0.10, 0.50, 0.02]),AssociationRule(4, "r4: c→d", [0.20, 0.40, 0.10]),
            AssociationRule(5, "r5: d→a", [0.20, 0.33, 0.02]),AssociationRule(6, "r6: d→c", [0.20, 0.33, 0.10]),
            AssociationRule(7, "r7: c→b", [0.10, 0.20, 0.01]),AssociationRule(8, "r8: d→b", [0.10, 0.17, 0.02])
        ])

        #Getting Ep1
        ruleCopy = rulesArticle.copy()
        sky = SkyRule(rulesArticle)
        undominated = sky.getUndominatedRules()
        for r in undominated:
            rulesArticle.removeRule(r)

        #Getting Ep2
        sky = SkyRule(rulesArticle)
        undominated = sky.getUndominatedRules()
        self.assertTrue(undominated[0]==ruleCopy.rules[5] and undominated[1] == ruleCopy.rules[2])



class TestRuleSetMethods(unittest.TestCase):

    def test_empty_rule_vector(self):
        self.assertEqual(RuleSet(None).rules,[])

    def test_filled_rule_vector(self):
        r1 = AssociationRule(1, "r1",[1,2,3])
        r2 = AssociationRule(2, "r2",[1,2,3])
        self.assertEqual(RuleSet([r1,r2]).rules,[r1,r2])

    def test_reference_measure(self):
        r1 = AssociationRule(1, "r1",[1,2,3,4,5])
        r2 = AssociationRule(2, "r2",[5,4,3,2,5])
        rs = RuleSet([r1,r2])
        reference = rs.getReferenceRule()
        self.assertEqual(reference.measures,tuple([5.0,4.0,3.0,4.0,5.0]))

class TestAssociationRuleMethods(unittest.TestCase):

    def test_raise_empty_rule(self):
        with self.assertRaises(ValueError):
            AssociationRule(1, None,[1,2,3])

    def test_raise_invalid_measures(self):
        with self.assertRaises(TypeError):
            AssociationRule(1, "R1",12)

    def test_degSimZero(self):
        self.assertEqual(AssociationRule(1, "R1",[1,2,3,4]).degSim(AssociationRule(2, "R2",[1,2,3,4])),0.0)

    def test_degSim2(self):
        self.assertEqual(AssociationRule(1, "R1",[1,2,3,4,5]).degSim(AssociationRule(2, "R2",[1,2,3,4,6])),0.2)

    def test_degSim4(self):
        self.assertEqual(AssociationRule(1, "R1",[1,2,3,4,5]).degSim(AssociationRule(2, "R2",[1,2,3,3,6])),0.4)

    def test_dominates(self):
        r1 = AssociationRule(1, "R1",[1,2,3,4,5])
        r2 = AssociationRule(2, "R2",[1,2,3,4,5])
        self.assertTrue(r1.dominates(r2))

    def test_dont_dominate(self):
        r1 = AssociationRule(1, "R1",[1,2,3,4,5])
        r2 = AssociationRule(2, "R2",[2,2,3,4,5])
        self.assertFalse(r1.dominates(r2))

    def test_strictly_dominates(self):
        r1 = AssociationRule(1, "R1",[1,2,3,4,6])
        r2 = AssociationRule(2, "R2",[1,2,3,4,5])
        self.assertTrue(r1.strictlyDominates(r2))

    def test_dont_strictly_dominates(self):
        r1 = AssociationRule(1, "R1",[1,2,3,4,5])
        r2 = AssociationRule(2, "R2",[1,2,3,4,5]) #Equal
        self.assertFalse(r1.strictlyDominates(r2))

    def test_dont_strictly_dominates(self):
        r1 = AssociationRule(1, "R1",[1,2,3,4,5])
        r2 = AssociationRule(2, "R2",[1,1,3,4,6])
        self.assertFalse(r1.strictlyDominates(r2))

    def test_equivalent_rules(self):
        r1 = AssociationRule(1, "R1",[1,2,3,4,5])
        r2 = AssociationRule(2, "R2",[1,2,3,4,5])
        self.assertTrue(r1.dominates(r2) and r2.dominates(r1))

    def test_strictly_dominates_one_measure(self):
        r1 = AssociationRule(1, "R1",[0,1,2,3,6])
        r2 = AssociationRule(2, "R2",[1,2,3,4,5])
        self.assertTrue(r1.strictlyDominatesOneMeasure(r2))

    def test_dont_strictly_dominates_one_measure(self):
        r1 = AssociationRule(1, "R1",[0,1,2,3,5])
        r2 = AssociationRule(2, "R2",[1,2,3,4,5])
        self.assertFalse(r1.strictlyDominatesOneMeasure(r2))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAssociationRuleMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRuleSetMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSkyRuleMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRuleRankMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)

    rulesExample = RuleSet([
        AssociationRule(1, "R1", [0.4309829,	1.8655636,	3.3558367,	0.3110091,	1.6581307,	1.3871074,	1.6936951,	1.2460669,	1.276724,	2.7412197]),
        AssociationRule(2, "R2", [2.5281935,	0.1721883,	0.1603762,	2.7389153,	0.3450452,	0.2891726,	0.6412873,	0.1879048,	1.523548,	0.531534]),
        AssociationRule(3, "R3", [0.4650572,	0.2461997,	2.7749146,	1.2955165,	0.7216444,	1.3360645,	0.9006454,	0.8928032,	1.4256843,	1.1989959]),
        AssociationRule(4, "R4", [0.3626624,	6.5712536,	2.166746,	0.2685662,	7.0200294,	3.8115143,	0.406186,	0.2640491,	5.2337475,	7.1851741]),
        AssociationRule(5, "R5", [1.8126375,	1.2510913,	1.5756018,	3.0303987,	1.4036082,	0.5228775,	0.7114484,	0.4509546,	6.3267593,	1.0715585]),
        AssociationRule(6, "R6", [1.4606636,	1.61696,	1.9599725,	0.7041472,	0.6161951,	0.9956647,	0.2022348,	0.5380424,	0.2855661,	0.4883107]),
        AssociationRule(7, "R7", [1.4282581,	8.9481832,	0.6811515,	0.7384252,	3.2630817,	0.1884696,	2.066209,	3.8004705,	1.2855345,	0.8643618]),
        AssociationRule(8, "R8", [0.472131,	0.4537345,	3.8394616,	0.4686466,	0.6705395,	2.0746189,	4.5079555,	2.2767139,	0.7944379,	1.1137488]),
        AssociationRule(9, "R9", [1.3825045,	0.8160929,	1.336977,	1.5226219,	0.530021,	0.92262,	2.4226434,	2.3900542,	2.8607012,	0.8431207]),
        AssociationRule(10, "R10",[8.07268,	0.446816,	1.7744434,	0.2477175,	0.2668183,	1.6934339,	0.6886501,	0.7754696,	0.5843631,	4.5173709]),
        AssociationRule(11, "R11",[1.8126375,    8.9481832,  3.8394616,  3.0303987,  7.0200294,  3.8115143,  4.5079555,  3.8004705,  6.3267593,  7.1851741])
    ])

    rulesArticle = RuleSet([
        AssociationRule(1, "r1: a→d", [0.20, 0.67, 0.02]),
        AssociationRule(2, "r2: b→c", [0.10, 0.50, 0.00]),
        AssociationRule(3, "r3: b→d", [0.10, 0.50, 0.02]),
        AssociationRule(4, "r4: c→d", [0.20, 0.40, 0.10]),
        AssociationRule(5, "r5: d→a", [0.20, 0.33, 0.02]),
        AssociationRule(6, "r6: d→c", [0.20, 0.33, 0.10]),
        AssociationRule(7, "r7: c→b", [0.10, 0.20, 0.01]),
        AssociationRule(8, "r8: d→b", [0.10, 0.17, 0.02])
    ])

    rankRulesExample = RankRule(rulesExample)
    for rule in rankRulesExample.getRankedRules():
        print(rule)

    rankRulesArticle = RankRule(rulesArticle)
    for rule in rankRulesArticle.getRankedRules():
        print(rule.__str__(withMeasuresAndRule=True))