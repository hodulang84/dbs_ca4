from collections import Counter
import matplotlib.pyplot as plt

def read_file(changes_file):
    data = [line.strip() for line in open(changes_file, 'r')]
    return data

def get_commits(data):
    sep = 72*'-'
    commits = []
    index = 0
    while index < len(data):
        try:
            details = data[index + 1].split('|')
            commit = {'r': details[0].strip(),
                'name': details[1].strip(),
                'date': details[2].strip().split(' ')[0],
                'time': details[2].strip().split(' ')[1],
                'num_line': details[3].strip().split(' ')[0]
            }
            commits.append(commit)
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return commits

def get_changedPaths(data):
    sep = 72*'-'
    changePaths = []
    index = 0
    while index < len(data):
        try:
            details = data[index + 3].split(' ')
            changePath = {'changedPathsType': details[0].strip()
            }
            changePaths.append(changePath)
            index = data.index(sep, index + 3)
        except IndexError:
            break
    return changePaths

if __name__ == '__main__':
    changes_file = 'changes_file.txt'
    data = read_file(changes_file)
    commits = get_commits(data)
    changePaths = get_changedPaths(data)
    
    c_n = Counter(map(lambda d: d['name'], commits))
    c_d = Counter(map(lambda d: d['date'], commits))
    c_t = Counter(map(lambda d: d['time'], commits))
    c_nl = Counter(map(lambda d: d['num_line'], commits))
    path = Counter(map(lambda d: d['changedPathsType'], changePaths))
    
    print("interesting 1 : ", c_n)
    print("interesting 2 : ", c_nl)
    print("interesting 3 : ", path)    
    
    plt.bar(range(len(c_n)), c_n.values(), align = 'center')
    plt.xticks(range(len(c_n)), c_n.keys())
    plt.show()
    
    plt.bar(range(len(c_nl)), c_nl.values(), align = 'center')
    plt.xticks(range(len(c_nl)), c_nl.keys())
    plt.show()
    
    plt.bar(range(len(path)), path.values(), align = 'center')
    plt.xticks(range(len(path)), path.keys())
    plt.show()