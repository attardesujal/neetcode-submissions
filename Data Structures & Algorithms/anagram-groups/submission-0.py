class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_list = []

        for s in strs:
            found = False

            for group in final_list:
                if sorted(s) == sorted(group[0]):
                    group.append(s)
                    found = True
                    break

            if not found:
                final_list.append([s])

        return final_list