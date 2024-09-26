class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @lru_cache(None)
        def compute(expr: str) -> List[int]:
            if expr.isdigit() or (expr[0] == '-' and expr[1:].isdigit()):  # Check if expr is a number
                return [int(expr)]

            result = []

            for i, char in enumerate(expr):
                if char in '+-*':
                    left_results = compute(expr[:i])
                    right_results = compute(expr[i + 1:])
                    
                    for left in left_results:
                        for right in right_results:
                            if char == '+':
                                result.append(left + right)
                            elif char == '-':
                                result.append(left - right)
                            elif char == '*':
                                result.append(left * right)

            return result
        
        return compute(expression)