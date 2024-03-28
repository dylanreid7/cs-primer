import subprocess
import sys

class ProcessNode(object):
    def __init__(self, pid, ppid, info):
        self.pid = pid
        self.ppid = ppid
        self.info = info
        self.children = []

def print_tree(node, depth = 0):
    if depth > 0:
        print('|')
    stick = ''
    for i in range(depth):
        stick += '--'
    print(stick, node.pid, node.info)

    for n in node.children:
        print_tree(n, depth + 1)


def print_pstree():
    header = sys.stdin.readline().split()
    print(header)
    # get access to the output of the commands
    # 
    try: 
        pid_idx = header.index('PID')
        ppid_idx = header.index('PPID')
        comm_idx = header.index('COMM')

    except ValueError:
        print('Usage: ps -o pid,ppid,[etc] | python pstree.py')
        exit(1)

    root = []

    for line in sys.stdin:
        parts = line.split()
        pid = parts[pid_idx]
        ppid = parts[ppid_idx]
        info = ' '.join(x for i, x in enumerate(parts) if i not in {pid_idx, ppid_idx})
        p_node = ProcessNode(pid, ppid, info)
        
        parent = find_parent(root, ppid)
        if parent is None:
            for i, p in enumerate(root):
                if p.ppid == pid:
                    p_node.children.append(p)
                    root.pop()
                    break
            root.append(p_node)
        else:
            parent.children.append(p_node)

    #print tree
    for n in root:
        print_tree(n)


def find_parent(candidates, target_pid):
    for p in candidates:
        if p.pid == target_pid:
            return p
    for p in candidates:
        parent = find_parent(p.children, target_pid)
        if parent is not None:
            return parent
    return None    
    

print_pstree()
