numbs = [5, 10, 15, 45, 22]

def run(numbs):
    new_numbs = [i for i in numbs if i == numbs[0] or i == numbs[len(numbs) - 1]]
    print(new_numbs)
    
if __name__ == '__main__':
    run(numbs)