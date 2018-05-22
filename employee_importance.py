"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        
        def get_importance(employees, id):
            employee = [x for i, x in enumerate(employees) if x.id == id][0]
            imp = employee.importance
            subs = employee.subordinates

            if not subs:
                return imp

            for id_no in subs:
                imp += get_importance(employees, id_no)

            return imp
        
        return get_importance(employees, id)