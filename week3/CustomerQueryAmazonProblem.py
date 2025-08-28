class Solution:
    def validKeywords(self, keywords: list[str], query: str) -> list[list[str]]:
        # keywords can be an empty list? keywords can have repeated elements? does it matter?
        # the mininum length of query would be 2? 'cuz it's the min to start searching

        keywords.sort()

        result = []

        for i in range(2, len(query)+1):
            for k in keywords:
                if not k.startswith(query[:i]):
                    keywords.remove(k)
                result.append(keywords)

        return result
        
        # Time complexity: O(n*m), n = len(keywords), m = len(query) ?
        # Memory complexity: O(1)