"""You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
Return the average salary of employees excluding the minimum and maximum salary. 
Answers within 10-5 of the actual answer will be accepted."""

class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        self.salary = salary
        sal_list = []
        for sal in salary:
            sal = float(sal)
            if sal == min(salary):
                continue
            elif sal == max(salary):
                continue
            else:
                sal_list.append(sal)
            return sum(sal_list)/len(sal_list)