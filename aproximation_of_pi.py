'''
Problem: Approximation of π (Pi)
We want to approximate the value of π using a Monte Carlo simulation.

Technique:
-Take a random point P(x, y) such that 0 ≤ x ≤ 1 and 0 ≤ y ≤ 1.
-If x² + y² ≤ 1, then the point lies inside the quarter circle of radius 1.
-Otherwise, the point lies outside.
-The probability that a point is inside the quarter circle equals π / 4.

Task:
-Write the function piApprox(pts), which takes a list of points pts (each point is [x, y]) and returns an approximation of π.

Input:
-pts is a list of points.
-Each point is an array of two floats [x, y] where 0 ≤ x ≤ 1 and 0 ≤ y ≤ 1.
-pts is never empty.

Output:
-Return a float value approximating π.
'''
import random

class Solution():

    def gen_rend_poins(self):
        r_list = []

        for i in range(100000000):
            x = random.randint(0,1000) / 1000
            y = random.randint(0,1000) / 1000

            r_list.append([x,y])

        return r_list


    def pi_apr(self):

        inside = 0
        pts = self.gen_rend_poins()
        print(len(pts))
        for obj in pts:
            if obj[0]**2 + obj[1]**2 <= 1:
                inside += 1

        res = (inside/len(pts))*4
        return res


res = Solution()

print(res.pi_apr())







a = Solution()