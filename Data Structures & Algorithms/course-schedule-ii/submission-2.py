class Solution:
    """
    Task: Return a valid ordering cources as List whose element is cource number.

    Now I want clarify this problem.
    - Ofcorse Output List have duplucates element because we dont neet to course two times or more.
    - I thik we can express the relationship cources and prerequeisities also this prerequiesities also course as graph
    
    So let me describe the graph by using exmaple1.
    I am going to use this example:
    Input: numCourses = 5. prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
    Ouput: [2, 4, 3, 1, 0] etc...

    I draw the relationship between crs and preresites as graph from input adjcency list
    Also, we can express the relationship by using Map
    like key is crs numbers. and value is the list the elemment is also crs.

    In this example, like this
    crs(key)|prereques(value)
    0|[1, 2]
    1|[3, 4]
    2|[]
    3|[4]
    4|[]

    I think we can use recursibly call by using dfs.
    base case is if the crs prerequesites is empty, append crs number into result list and return
    another base case is we already take the crs, we should early back and do not append the crs.

    and we should call dfs because it is possible that there are some graph like separated.

    Why I cant solve ?
    - When the function detect the cycle, the output is not empty list
    """
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        preMap = { crs: [] for crs in range(numCourses) }
        for crs, prereq in prerequisites:
            preMap[crs].append(prereq)
        
        visit = set()
        cycle = set() # To detect the cycle on the recently path
        def dfs(crs: int) -> bool:
            nonlocal res
            if crs in cycle:
                return False
            
            if crs in visit: # すでに訪問済みであるなら以降の操作はせずTrue
                return True
                        
            cycle.add(crs) 
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            cycle.remove(crs) # allow to call dfs in main funcst
            res.append(crs)
            visit.add(crs)
            
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return res







