class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        ref=strs[0]
        for L in range(len(ref),0,-1):
            is_common=True
            prefix = ref[:L]
            for i in range(1,len(strs)):
                curr_string = strs[i]
                if not curr_string.startswith(prefix):
                    is_common=False
                    break
            if is_common:
                return prefix
        return ""
        

        