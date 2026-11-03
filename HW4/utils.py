def _init_matrix_(n: int, m: int) -> list[list[int | None]]:
    result = []

    for _ in range(n):
        result.append([None] * m)
    
    return result