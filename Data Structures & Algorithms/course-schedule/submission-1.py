class Solution:
    """
    Task: Check if it is possible to finish all given cources.
    
    I want to clarify problem, so let me describe example 1
    I wonder if the course number is used by 0 to numCourse

    Why I cant solve this ?
    - コース同士が条件として参照しあっている場合にはFalseであるとわかるが、判定方法がわからなかった
    - Cycle detection problemと気が付かなかった

    How to solve
    - Make Premap as a graph which express the relationship each cources. 
    - Map'key is a course number, and the value is list of prerequisites course number
    - 必要なコースを少量したらprereqから削除する、コースの修了有無はprereqがemptyになった時にそのコースは受け終わったものとする
    - ただしPreMapをそのものを操作しなくても問題を解くことができる、単に取りたいコースをsetに追加していき、次のそのコースに必要なコースを訪問し、addする
    これを繰り返すとCycleがある場合にすでに訪れたものが現れた場合にはんていすることができる。
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each to prereq list
        preMap = {
            crs: []
            for crs in range(numCourses)
        }

        for crs, prereq in prerequisites:
            preMap[crs].append(prereq)

        # visitSet = all courses alonthe curr dfs path
        visitSet = set()
        def dfs(crs: int):
            if crs in visitSet:
                return False
            
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            visitSet.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
