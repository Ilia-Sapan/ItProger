arr = [1,1,2,2,3]

# int: the lowest type id of the most frequently sighted birds



def migratoryBirds(arr):
    birds = {bird:arr.count(bird) for bird in set(arr)}
    return min(int(bird) for bird, count in birds.items() if count == max(map(int,birds.values())))

