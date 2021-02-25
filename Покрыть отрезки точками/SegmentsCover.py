'''
По данным nn отрезкам необходимо найти множество точек минимального размера,
для которого каждый из отрезков содержит хотя бы одну из точек.

В первой строке дано число 1<=n<=100 отрезков. 
Каждая из последующих n строк содержит по два числа 0<=l<=r<=10^9,
задающих начало и конец отрезка. 

Выведите оптимальное число mm точек и сами mm точек. 
Если таких множеств точек несколько, выведите любое из них.
'''


n = int(input()) 

segments = [[int(x) for x in input().split()] for i in range(n)]
segments.sort(key=lambda x: x[1])

right_point = segments[0][1]
points = []
points.append(right_point)

for i in range(1, len(segments)):
	if segments[i][0] > right_point:
		points.append(segments[i][1])
		right_point = segments[i][1]

print(len(points))
print(' '.join(str(point) for point in points))