# Artificial-Intelligence
HYU CSE4007
-----------------------
## 1. Maze Search
  다양한 search algorithm을 이용하여 미로 경로를 탐색한다.
  ### 세부 사항
  > - 미로에는 입구와 출구가 있으며, 통로와 벽이 구분되어 있다.
  > - 출구는 자물쇠로 잠겨 있어 출구로 가는 도중에 키를 습득해야 한다.
  > - 키가 여러 개인 경우 모두 습득해야 하며 습득 순서는 무관하다.
  > - 알고리즘: Breadth First Search, Iterative Deepening Search, Greedy Best First Search, A* Algorithm
  > - 각 미로마다 4가지 알고리즘을 모두 사용한다.
  > - 각각의 미로를 탈출하기 위해 알고리즘 별로 탐색한 노드의 개수와 최단 경로로 점수 산출한다.
  
  ### 미로 표현
  > - 입력: k번째 미로(k) / 행렬 크기(m*n) / 1,2,3,4,5,6으로 표현된 m*n 행렬
  > - 출력: 1,2,3,4,5 로 표현된 m*n 행렬, 최단경로 길이, 탐색 노드 개수
  > - 미로: 1=벽, 2=통로, 3=출발점, 4=도착점, 6=key
 
 ### 환경
 > - 프로그래밍 언어 : python 3.5
 >- OS : windows 10
 
 ## 2. Hierarchical Clustering
  Hierarchical Agglomerative Clustering 기법을 이용하여 좌표평면상의 점들을 clustering 한다.
  ### 세부 사항
  > - 총 3가지의 좌표평면의 점들에 대한 데이터를 각각 3개의 군집으로 묶일 수 있게 하는 similarity level을 구하는 것이 목표이다.
  > - 좌표평면상의 점은 각각 n개가 주어진다.
  > - 점들 사이의 similarity는 Cosine Similarity로 정의한다.
  > - clustering 방법:  single-link clustering, complete-link clustering, group average-link clustering
  > - 각 방법마다 3개의 군집으로 나눠지게 하는 similarity level 범위를 구한다.
  
  ### 입출력 txt 표현
  > - 입력: k번째 좌표평면(k) / 점의 개수(n) / 점들의 좌표(x,y)
  > - 출력: k번째 좌표평면(k) / 각 방법의 clusters, similarity level 범위
  
   ### 환경
 > - 프로그래밍 언어 : python 3.5
 > - OS : windows 10
 
