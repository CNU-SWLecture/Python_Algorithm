def hanoi(n, from_pos, to_pos, by_pos):
    if n==1:
        print(from_pos, '->', to_pos)
        return
    hanoi(n-1, from_pos, by_pos, to_pos)
    print(from_pos, '->', to_pos)
    hanoi(n-1, by_pos, to_pos, from_pos)
