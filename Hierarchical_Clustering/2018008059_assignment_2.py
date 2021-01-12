import math


class Clustering:
    k_number = 0
    node_number = 0
    node = None
    node_list = []
    similarity_list =[]

    def __init__(self, filename):
        self.node_list.clear()
        self.similarity_list.clear()
        with open(filename, 'r') as f:
            self.k_number, self.node_number = [int(x) for x in f.readline().strip().split(' ')]
            self.similarity_list =[[0 for col in range(self.node_number)] for row in range(self.node_number)]
            for line in f:
                self.node= tuple(int(x) for x in line.strip().split(','))
                self.node_list.append(self.node)

    def cosine_similarity(self):
        for i in range(0,self.node_number):
            for j in range(0,self.node_number):
                mole = self.node_list[i][0]*self.node_list[j][0]+self.node_list[i][1]*self.node_list[j][1]
                deno = self.node_list[i][0]*self.node_list[i][0]+self.node_list[i][1]*self.node_list[i][1]
                deno1 = math.sqrt(float(deno))
                deno = self.node_list[j][0] * self.node_list[j][0] + self.node_list[j][1] * self.node_list[j][1]
                deno1 *=math.sqrt(float(deno))
                similarity = mole/deno1
                self.similarity_list[i][j] = similarity

        for i in range(0,self.node_number):
            self.similarity_list[i][i] = -100

    def single(self, file):
        f = open(file, 'a')
        f.write('\n---\nsingle\n')

        self.cosine_similarity()

        group = [[] for row in range(self.node_number)]

        for i in range(0,self.node_number):
            group[i].append(self.node_list[i])

        lst = []
        iv=0
        jv=0
        similarity_level = []

        number = len(self.similarity_list)

        while number != 3:
            maxv = max(map(max,self.similarity_list))

            for i in range(0,self.node_number):
                for j in range(0, self.node_number):
                    if self.similarity_list[i][j] == maxv:
                        iv = i
                        jv = j
                        break

            if iv > jv: #iv가 항상 작다.
                tmp = iv
                iv = jv
                jv = tmp

            number -= 1

            for i in range(0,self.node_number):
                self.similarity_list[iv][i] = max(self.similarity_list[iv][i], self.similarity_list[jv][i])
                self.similarity_list[i][iv] = self.similarity_list[iv][i]
                self.similarity_list[jv][i] = -100
                self.similarity_list[i][jv] = -100
                self.similarity_list[i][i] = -100

            for i in range(len(group[jv])):
                group[iv].append(group[jv][i])

            group[jv]=[]
            similarity_ = max(map(max, self.similarity_list))
            similarity_level.append(similarity_)

        f.write('cluster: ')
        for n in range(self.node_number):
            if not group[n]:
                continue
            else:

                f.write('[')
                for x in range(1,len(group[n])):
                    f.write(str(group[n][x]))
                    f.write(',')
                    lst.append(group[n][x])
                f.write(str(self.node_list[n]))
                lst.append(self.node_list[n])
                f.write('] ')

        for n in range(self.node_number):
            if self.node_list[n] not in lst:
                f.write('[')
                f.write(str(self.node_list[n]))
                f.write('] ')

        f.write('\nspan: ')
        f.write(str(similarity_level[-2])+', ')
        f.write(str(similarity_level[-1]))

        f.close()

    def complete(self, file):
        f = open(file, 'a')
        f.write('\n---\ncomplete\n')
        self.cosine_similarity()

        group = [[] for row in range(self.node_number)]

        for i in range(0,self.node_number):
            group[i].append(self.node_list[i])

        lst = []
        iv=0
        jv=0
        similarity_level = []

        number = len(self.similarity_list)

        while number != 3:
            maxv = max(map(max,self.similarity_list))

            for i in range(0,self.node_number): #세로크기
                for j in range(0, self.node_number): #가로 크기
                    if self.similarity_list[i][j] == maxv: #한 세로당 가로요소하나씩
                        iv = i
                        jv = j
                        break

            if iv > jv: #iv가 항상 작다.
                tmp = iv
                iv = jv
                jv = tmp

            number -= 1

            for i in range(0,self.node_number):
                self.similarity_list[iv][i] = min(self.similarity_list[iv][i], self.similarity_list[jv][i])
                self.similarity_list[i][iv] = self.similarity_list[iv][i]
                self.similarity_list[jv][i] = -100
                self.similarity_list[i][jv] = -100
                self.similarity_list[i][i] = -100

            for i in range(len(group[jv])):
                group[iv].append(group[jv][i])

            group[jv]=[]
            similarity_ = max(map(max, self.similarity_list))
            similarity_level.append(similarity_)

        f.write('cluster: ')
        for n in range(self.node_number):
            if not group[n]:
                continue
            else:

                f.write('[')
                for x in range(1,len(group[n])):
                    f.write(str(group[n][x]))
                    f.write(',')
                    lst.append(group[n][x])
                f.write(str(self.node_list[n]))
                lst.append(self.node_list[n])
                f.write('] ')

        for n in range(self.node_number):
            if self.node_list[n] not in lst:
                f.write('[')
                f.write(str(self.node_list[n]))
                f.write('] ')

        f.write('\nspan: ')
        f.write(str(similarity_level[-2]) + ', ')
        f.write(str(similarity_level[-1]))

        f.close()

    def average(self, file):
        f = open(file, 'a')
        f.write('\n---\naverage\n')
        self.cosine_similarity()

        group = [[] for row in range(self.node_number)]

        for i in range(0,self.node_number):
            group[i].append(self.node_list[i])

        lst = []
        iv=0
        jv=0
        similarity_level = []

        number = len(self.similarity_list)

        while number != 3:
            maxv = max(map(max,self.similarity_list))

            for i in range(0,self.node_number): #세로크기
                for j in range(0, self.node_number): #가로 크기
                    if self.similarity_list[i][j] == maxv: #한 세로당 가로요소하나씩
                        iv = i
                        jv = j
                        break

            if iv > jv: #iv가 항상 작다.
                tmp = iv
                iv = jv
                jv = tmp

            number -= 1

            for i in range(0,self.node_number):
                self.similarity_list[iv][i] = (self.similarity_list[iv][i] + self.similarity_list[jv][i])/2
                self.similarity_list[i][iv] = self.similarity_list[iv][i]
                self.similarity_list[jv][i] = -100
                self.similarity_list[i][jv] = -100
                self.similarity_list[i][i] = -100

            for i in range(len(group[jv])):
                group[iv].append(group[jv][i])

            group[jv]=[]
            similarity_ = max(map(max, self.similarity_list))
            similarity_level.append(similarity_)


        f.write('cluster: ')
        for n in range(self.node_number):
            if not group[n]:
                continue
            else:
                f.write('[')
                for x in range(1,len(group[n])):
                    f.write(str(group[n][x]))
                    f.write(',')
                    lst.append(group[n][x])
                f.write(str(self.node_list[n]))
                lst.append(self.node_list[n])
                f.write('] ')

        for n in range(self.node_number):
            if self.node_list[n] not in lst:
                f.write('[')
                f.write(str(self.node_list[n]))
                f.write('] ')

        f.write('\nspan: ')
        f.write(str(similarity_level[-2]) + ', ')
        f.write(str(similarity_level[-1]))

        f.close()


def run(plane: str):
    clus = Clustering(plane+".txt")

    with open(plane+'_output.txt', 'w') as f:
        f.write(str(clus.k_number))

    clus.single(plane+'_output.txt')
    clus.complete(plane+'_output.txt')
    clus.average(plane+'_output.txt')


if __name__ == '__main__':
    run('CoordinatePlane_1')
    run('CoordinatePlane_2')
    run('CoordinatePlane_3')