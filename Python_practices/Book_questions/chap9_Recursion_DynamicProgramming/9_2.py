import numpy as np

def main():
    print(get_path_recursive(x=3, y=3, invalid_cells=[(1,0),(3,2)]))

def get_path_recursive(x, y, invalid_cells=[], x_current=0, y_current=0, path=[(0,0)]):
    if x_current == x and y_current == y:
        return True, path
    elif x_current == x and y_current == y:
        return 0
    sucess = False
    if x_current < x and (x_current+1, y_current) not in invalid_cells:
        x_current = x_current + 1
        sucess, path = get_path_recursive(x, y, invalid_cells, x_current, y_current, path)
    if (not sucess) and y_current < y and (x_current, y_current+1) not in invalid_cells:
        y_current = y_current + 1
        sucess, path = get_path_recursive(x, y, invalid_cells, x_current, y_current, path)
    if (x_current,y_current) not in path:
        path.append((x_current,y_current))
    # print(path)
    return sucess, path
            
if __name__ == '__main__':
    main()