"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        employees_id = {e.id: e for e in employees}
        def dfs(id):
            result = sum([dfs(sub_id) for sub_id in employees_id[id].subordinates])
            return result + employees_id[id].importance
        
        return dfs(id)
