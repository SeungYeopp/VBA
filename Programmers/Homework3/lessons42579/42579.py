# 베스트앨범: https://school.programmers.co.kr/learn/courses/30/lessons/42579
def solution(genres, plays):
    ans = []

    # 앨범 정보를 저장할 딕셔너리 생성
    album_dict = {}

    # 장르와 플레이 횟수를 돌며 딕셔너리에 저장
    for idx in range(len(genres)):
        key = genres[idx]

        if key in album_dict:
            album_dict[key].append((idx, plays[idx],))
        else:
            album_dict[key] = [(idx, plays[idx])]

    genres_sorted = []
    # 장르별 총 플레이 횟수 계산
    for key in album_dict.keys():
        genres_sorted.append((key, sum([x[1] for x in album_dict[key]])))

    # 총 플레이 횟수를 기준으로 장르 정렬
    genres_sorted = sorted(genres_sorted, key=lambda x: -x[1])

    for key, _ in genres_sorted:
        # 해당 장르의 곡들을 플레이 횟수를 기준으로 정렬
        musics = sorted(album_dict[key], key=lambda x: -x[1])
        # 정렬된 곡들 중 상위 2개의 곡 인덱스를 결과 리스트에 추가
        for item in musics[:2]:
            ans.append(item[0])

    return ans


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
