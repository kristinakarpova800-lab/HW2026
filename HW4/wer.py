import json
from utils import _init_matrix_

def del_cost() -> int:
    return 1

def ins_cost() -> int:
    return 1

def sub_cost(sourse_word: str, target_word: str) -> int:
    return 1 if sourse_word != target_word else 0

def calculate_wer(referense_text: str, hypothesis_text: str) -> float:
    ref = referense_words = referense_text.split()
    hyp = hypothesis_words = hypothesis_text.split()

    n = len(ref)
    m = len(hyp)

    N = n  #number of words in the reference text

    D_matrix = _init_matrix_(n + 1, m + 1)
    D_matrix[0][0]= 0

    for i in range(1, n + 1):
        D_matrix[i][0] = i * del_cost()

    for j in range(1, m + 1):
        D_matrix[0][j] = j * ins_cost()

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D_matrix[i][j] = min(
                D_matrix[i - 1][j] + del_cost(), #Deletion   
                D_matrix[i - 1][j - 1] + sub_cost(ref[i - 1], hyp[j - 1]), #Substitution
                D_matrix[i][j - 1] + ins_cost() #Insertion
                
            )

    i, j = n, m
    S, D, I = 0, 0, 0

    while i > 0 or j > 0:
        if i > 0 and j > 0 and D_matrix[i][j] == D_matrix[i - 1][j - 1] + sub_cost(ref[i - 1], hyp[j - 1]):
            if ref[i - 1] != hyp[j - 1]:
                S += 1
            i -= 1
            j -= 1
        elif i > 0 and D_matrix[i][j] == D_matrix[i - 1][j] + del_cost():
            D += 1  
            i -= 1
        else:
            I += 1
            j -= 1

    wer_value = (S + D + I) / n if n > 0 else 0.0

    return {
        "WER": wer_value,
        "S(Substitutions)": S,
        "D(Deletions)": D,
        "I(Insertions)": I,
        "N(Reference words)": N
        }