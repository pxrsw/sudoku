import copy
import datetime


class Sodoku():
    
    
    def __init__(self, state, size, sub_column_size, sub_row_size):
        
    
        self.state = state
        self.size = size
        self.sub_column_size = sub_column_size
        self.sub_row_size = sub_row_size
        self.domains = {}
        
        self.update_domains()
        
    def update_domains(self):
        self.domains = {}
        numbers = []
        for y in range(self.size):
            for x in range(self.size):
                if (self.state[y][x] == 0):
                    numbers = []
                    for number in range(1, self.size + 1):
                        if(self.is_consistent(number, y, x) == True):
                            numbers.append(number)
                    if(len(numbers) > 0):
                        self.domains[(y, x)] = numbers
                            
    
    def is_consistent(self, number, row, column):
        for x in range(self.size):
            if self.state[row][x] == number:
                return False
        for y in range(self.size):
            if self.state[y][column] == number:
                return False
        row_start = (row//self.sub_row_size)*self.sub_row_size
        col_start = (column//self.sub_column_size)*self.sub_column_size;
       
        for y in range(row_start, row_start+self.sub_row_size):
            for x in range(col_start, col_start+self.sub_column_size):
       
       
                if self.state[y][x]== number:
                    return False
       
        return True
    
    def get_first_empty_cell(self) :
        for y in range(self.size):
            for x in range(self.size):
                if (self.state[y][x] == 0):
                    return (y, x)
        
        return (None, None)

    
    def get_most_constrained_cell(self) :
    
        if(len(self.domains) == 0):
            return (None, None)
    
        keys = sorted(self.domains, key=lambda k: len(self.domains[k]))
    
        return keys[0]
    
    def solved(self):
    
        for y in range(self.size):
            for x in range(self.size):
                
    
                if (self.state[y][x] == 0):
                    return False
    
        return True
    
    
    def backtracking_search_1(self):
    
        y, x = self.get_first_empty_cell()
    
        if(y == None or x == None):
            return True
    
        for number in range(1, self.size + 1):
    
            if(self.is_consistent(number, y, x)):
    
                self.state[y][x] = number
    
                if (self.backtracking_search_1() == True):
                    return True
    
                self.state[y][x] = 0
    
        return False
    
    def backtracking_search_2(self):
    
        if(self.solved() == True):
            return True
        
        y, x = self.get_most_constrained_cell()
        
        
        if (y == None or x == None):
            return False
        
        numbers = copy.deepcopy(self.domains.get((y, x)))
        
        for number in numbers:
        
            if(self.is_consistent(number, y, x)):
        
                self.state[y][x] = number
        
                del self.domains[(y, x)]
        
                if (self.backtracking_search_2() == True):
                    return True
        
                self.state[y][x] = 0
        
                self.update_domains()
        
        return False

    def print_state(self):
        for y in range(self.size):
            print('| ', end='')
            if y != 0 and y % self.sub_row_size == 0:
                for j in range(self.size):
                    print(' - ', end='')
                    if (j + 1) < self.size and (j + 1) % self.sub_column_size == 0:
                        print(' + ', end='')   
                print(' |')
                print('| ', end='')
            for x in range(self.size):
                if x != 0 and x % self.sub_column_size == 0:
                    print(' | ', end='')
                digit = str(self.state[y][x]) if len(str(self.state[y][x])) > 1 else ' ' + str(self.state[y][x])
                print('{0} '.format(digit), end='')
            print(' |')
        

def main():
    numbers = [7,0,5,0,4,0,0,1,0,0,3,6,9,6,0,0,7,0,0,0,0,1,4,0,0,2,0,0,0,0,3,6,0,0,0,8,0,0,0,10,8,0,0,9,3,0,0,0,11,0,12,1,0,0,0,0,10,0,5,9,0,0,6,0,0,3,12,0,0,0,0,0,0,0,0,0,0,7,4,0,0,9,0,0,2,12,0,7,0,0,0,0,4,10,0,5,0,0,0,11,5,0,0,2,7,0,0,0,1,0,0,0,3,6,0,0,0,0,8,0,0,11,3,0,0,0,0,5,0,0,9,7,10,5,0,0,2,0,0,7,0,3,0,1]
    size = 12 
    sub_column_size = 4
    sub_row_size = 3 
    

    initial_state = []
    row = []
    counter = 0


    for number in numbers:
        counter += 1
        row.append(number)
        if(counter >= size):
            initial_state.append(row)
            row = []
            counter = 0


    sodoku = Sodoku(initial_state, size, sub_column_size, sub_row_size)

    print('Puzzle input:')
    sodoku.print_state()
    
    before_algorithm_time = x = datetime.datetime.now()
    sodoku.backtracking_search_2()
    after_algorithm_time = x = datetime.datetime.now()
    
    print('\nPuzzle solution:')
    sodoku.print_state()
    print()
    print('Time for solving algorithm with backtracking algorithm: ', (after_algorithm_time - before_algorithm_time))
    print()



    initial_state = []
    row = []
    counter = 0


    for number in numbers:
        counter += 1
        row.append(number)
        if(counter >= size):
            initial_state.append(row)
            row = []
            counter = 0


    sodoku = Sodoku(initial_state, size, sub_column_size, sub_row_size)

    
    before_algorithm_time = x = datetime.datetime.now()
    sodoku.backtracking_search_1()
    after_algorithm_time = x = datetime.datetime.now()
    
    print()
    print('Time for solving algorithm with optimize backtracking algorithm: ', (after_algorithm_time - before_algorithm_time))
    print()

if __name__ == "__main__": main()