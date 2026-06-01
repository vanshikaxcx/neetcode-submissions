class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={} #dictionary
        n=len(strs)
        for i in range(n):
            key="".join(sorted(strs[i])) #sorting all the words and then joining the list created by sorted function
            if key not in groups:
                groups[key]=[] #if key doesnt exist in the dictionary already then we will create a new empty list
            groups[key].append(strs[i]) #for every key we will append the corresponding word 
        return list(groups.values())         