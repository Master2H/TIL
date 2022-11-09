Matrix Factorization

행렬 곱을 이용하면 A는 row의 수, B는 column의 수만큼의 matrix가 나옴

(= A, B의 임베딩 크기가 얼마이든 상관없이 원하는 maxrix 크기를 뽑아냄)

이를 통해 결측치는 계산 안하고 존재하는 값에만 loss를 줄이는 방향으로 분석하여 실제 결과에 대한 matrix와 유사하게끔 반복-결측치는 제외하고 나머지 값들이 실제 결과와 유사하게

(결측치에 대한 높은 예측값도 추천 알고리즘으로 활용 가능)

→ A, B에 대한 feature를 뽑아 낼 수 있음

치명적인 단점(새로운 데이터 및 새로운 유저에 취약함)

또 다른 추천시스템(Apriori - 상관관계를 빈도 분석해주는 라이브러리)

단어 분석은 BERT를 활용 가능

MF는 3차원도 가능함(데이터 통합 및 추천 시스템에서 활용 가능)

최근 흐름 : MF → 딥러닝

논문 - 연구자들이 가장 이해하기 쉽도록 쓴 문헌

1. 구글링(개발 단계)
2. 논문 (연구 단계) 
- schoolar.google.com
- 제목 : 내가 뭘했는지 모든 걸 담고 있음
- 흥미로운 논문 발견 → 초록(Abstract) → 본문
- review paper : 특정 분야 전문가가, 정말 다른 논문들을 쫙 모아서 정리하는 논문 (연구 단계에서 활용도 높음)
1. 최신 트랜드 + 코드
- 검색 팁 (관련 키워드 + github(소스))
- ‘도메인’ ← 데싸 분석 잘 못하더라도, 해당 분야 분석가로서 이름을 날릴 수 있음

tip) 바이오, 의과 도메인 - ibric.org

[hibrain.net](http://hibrain.net) - 석사 자리 확인 가능 사이트

캐나다 등 북미 석사로 갈 수 있으면 가는 것 추천(2년 정도 지나면 영주권 발급)

- 영주권 + 미국 관련 기업 = 미국 영주권 발급 가능

지난내용 복습

multi-class : 정답이 여러 개중에 오직 하나

(output) Final layer : Softmax activation fuction

Loss : Categorical cross-entropy

multi-label : 정답이 동시에 여러 개 존재
-> 시그모이드, 바이너리


ENE 분석

Numeric(ex. Age) : Wilcoxon  test (t.test)

Categorical : Fisher exact test (chisq.test)

Propensity Score Matching

원하는 변수에 대해서만 제대로 통계분석 가능

디자인 작업 필요하면 디자인 협업 커뮤니티 or 카톡방 ([https://letspl.me/](https://letspl.me/) 등)

파이썬 기반 개발자 프레임워크 추천
-플라스크, 장고, FastAPI