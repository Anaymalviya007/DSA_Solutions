class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        need this kida data and then we can return the values
        [[]] in list of list format
        {
            "opst": ["stop", "pots", "tops"]
            "act": ["act", "cat"],
            "aht": ["hat"]
        }
        """

        hashmap = {}

        for char in strs:
            key = "".join(sorted(char))

            if key not in hashmap:
                hashmap[key] = []
            
            hashmap[key].append(char)
        
        return list(hashmap.values())
                
            