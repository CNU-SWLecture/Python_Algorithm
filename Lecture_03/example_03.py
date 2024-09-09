def permutation(vec, k):
    if k==len(vec) -1:
        print(vec)
        return
    for i in range (k, len(vec)):
        vec[k], vec[i] = vec[i], vec[k]
        permutation(vec, k+1)
        vec[k], vec[i] = vec[i], vec[k]
vec = ['a', 'b', 'c', 'd']
permutation(vec, 0)