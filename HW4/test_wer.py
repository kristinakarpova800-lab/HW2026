from wer import calculate_wer


def test_wer_1():
    ref = "тест перевірки алгоритму"
    hyp = "тест перевірки алгоритму"
    res = calculate_wer(ref, hyp)

    assert res["WER"] == 0.0
    assert res["S(Substitutions)"] == 0
    assert res["D(Deletions)"] == 0
    assert res["I(Insertions)"] == 0
    assert res["N(Reference words)"] == 3


def test_wer_2():
    ref = "це дуже гарний день"
    hyp = "це зовсім поганий день"
    res = calculate_wer(ref, hyp)

    assert res["S(Substitutions)"] == 2
    assert res["N(Reference words)"] == 4


def test_wer_3():
    ref = "швидкий лис"
    hyp = "дуже швидкий лис"
    res = calculate_wer(ref, hyp)

    assert res["N(Reference words)"] == 2
    assert res["I(Insertions)"] == 1

