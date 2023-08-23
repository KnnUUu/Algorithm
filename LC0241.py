class Solution:
    def diffWaysToCompute(self, expression: str):
        return self.computeExpressionDP(expression, {})
    
    def computeExpressionDP(this, expr, str2value):
        """
        expr: math expression
        str2value: string to possible values map
        """
        if('+' not in expr and '-' not in expr and '*' not in expr):
            # only digit
            str2value[expr] = [int(expr)]
        else:
            for i in range(len(expr)):
                if expr[i] in {'+','-','*'}:
                    # calculate left and right results separately 
                    if(expr[0:i] in str2value):
                        lVals=str2value[expr[0:i]]
                    else:
                        lVals=this.computeExpressionDP(expr[0:i],str2value)
                    
                    if(expr[i+1:] in str2value):
                        rVals=str2value[expr[i+1:]]
                    else:
                        rVals=this.computeExpressionDP(expr[i+1:],str2value)
                    # combine results
                    for lVal in lVals:
                        for rVal in rVals:
                            if expr not in str2value: str2value[expr] = []

                            if expr[i]=='+': str2value[expr].append(lVal+rVal)
                            elif expr[i]=='-': str2value[expr].append(lVal-rVal)
                            elif expr[i]=='*': str2value[expr].append(lVal*rVal)
        return str2value[expr]

import unittest
class Test0241(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(sorted(s.diffWaysToCompute("2*3-4*5")),sorted([-34,-14,-10,-10,10]))

unittest.main()