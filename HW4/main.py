import json
from wer import calculate_wer

with open("text1.txt", "r", encoding="utf-8") as f:
    text1 = f.read()

with open("text2.txt", "r", encoding="utf-8") as f:
    text2 = f.read()

metrics = calculate_wer(text1, text2)

with open("wer_results.json", "w", encoding="utf-8") as f:
    json.dump(metrics, f, ensure_ascii=False, indent=4)

print("Метрки успішно збережено в файлі wer_results.json")
print(metrics)
