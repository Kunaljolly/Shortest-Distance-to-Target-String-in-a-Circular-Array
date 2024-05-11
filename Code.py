class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        if target not in words:
            return -1

        # Calculate the distance in both directions
        forward_distance = 0
        backward_distance = 0
        for i in range(n):
            if words[(startIndex + i) % n] == target:
                forward_distance = i
                break
        for i in range(n):
            if words[(startIndex - i + n) % n] == target:
                backward_distance = i
                break

        # Return the minimum distance
        return min(forward_distance, backward_distance)
