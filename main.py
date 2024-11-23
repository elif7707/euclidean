points = [(6, 1), (3, 9), (1, 1), (4, 2)]

def euclidean_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        result = euclidean_distance(points[i], points[j])
        distances.append(result)

print("Minimum distance:", min(distances))
