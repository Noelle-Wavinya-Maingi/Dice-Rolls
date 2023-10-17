## Calculate the expected total sum of all rolls(Multiply desired mean M by total number of rolls)

## Calculate the sum of the known rolls in A

## Determine the minimum and maximum possible sum for missing rolls.

## Iterate from minimum to maximum sum of missing rolls


def solution(A, F, M):
    N = len(A)

    total_rolls = N + F

    expected_rolls = M * total_rolls

    known_sum = sum(A)

    min_possible_sum = F

    max_possible_sum = 6 * F

    if (
        expected_rolls < known_sum + min_possible_sum
        or expected_rolls > max_possible_sum + known_sum
    ):
        return [0]

    def find_possible_rolls(current_sum, remaining_rolls, result):
        if remaining_rolls == 0:
            if current_sum == expected_rolls:
                return result

            else:
                return None

        if current_sum > expected_rolls:
            return None

        possible_rolls = []

        for face in range(1, 7):
            new_result = result + [face]
            next_possible_rolls = find_possible_rolls(
                current_sum + face, remaining_rolls - 1, new_result
            )
            if next_possible_rolls:
                possible_rolls.extend(next_possible_rolls)

        return possible_rolls

    possible_rolls = find_possible_rolls(known_sum, F, [])

    if possible_rolls:
        return possible_rolls[:F]
    else:
        return [0]


# Test cases
print(solution([3, 2, 4, 3], 2, 4))  
print(solution([1, 5, 6], 4, 3))  
print(solution([1, 2, 3, 4], 4, 6))  
print(solution([6, 1], 1, 1))  
print(solution([6], 10, 4))  
