def add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def multiply(v, s):
    return tuple(map(lambda x: x * s, v))
