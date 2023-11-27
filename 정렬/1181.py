N = int(input())

words = []
for _ in range(N):
    word = input().strip()
    if word not in words:  # 중복된 단어는 하나만 남기고 제거
        words.append(word)

# 길이가 짧은 것부터, 길이가 같으면 사전 순으로 정렬
sorted_words = sorted(words, key=lambda x: (len(x), x))

# 정렬된 결과 출력
for w in sorted_words:
    print(w)