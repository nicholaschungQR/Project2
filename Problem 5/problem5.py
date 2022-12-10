def build_map(crates):
    '''
    Build a list representation of stacked crates,
    parsed into dicitonary

        Parameter:
            crates (list): list of crates


    Example:

        ['                    [Q]     [P] [P]',
        '                [G] [V] [S] [Z] [F]',
        '            [W] [V] [F] [Z] [W] [Q]',
        '        [V] [T] [N] [J] [W] [B] [W]',
        '    [Z] [L] [V] [B] [C] [R] [N] [M]',
        '[C] [W] [R] [H] [H] [P] [T] [M] [B]',
        '[Q] [Q] [M] [Z] [Z] [N] [G] [G] [J]',
        '[B] [R] [B] [C] [D] [H] [D] [C] [N]']

        turns into...

        {1: ['[B]', '[Q]', '[C]'],
         2: ['[R]', '[Q]', '[W]', '[Z]'],
         3: ['[B]', '[M]', '[R]', '[L]', '[V]'],
         4: ['[C]', '[Z]', '[H]', '[V]', '[T]', '[W]'],
         5: ['[D]', '[Z]', '[H]', '[B]', '[N]', '[V]', '[G]'],
         6: ['[H]', '[N]', '[P]', '[C]', '[J]', '[F]', '[V]', '[Q]'],
         7: ['[D]', '[G]', '[T]', '[R]', '[W]', '[Z]', '[S]'],
         8: ['[C]', '[G]', '[M]', '[N]', '[B]', '[W]', '[Z]', '[P]'],
         9: ['[N]', '[J]', '[B]', '[M]', '[W]', '[Q]', '[F]', '[P]']}

    '''
    all_crates = {}
    for i in range(len(crates[0])//4 + 1):
        ### YOUR CODE HERE ###
        pass
        
    for j in crates:
        ### YOUR CODE HERE ###
        pass

    # reverse list for easier handling
    for key, value in all_crates.items():
        ### YOUR CODE HERE ###
        pass

    return all_crates

def display(crate):
    print('=====================')
    for key, val in crate.items():
        print(val)
    print('=====================')

def move_crates(crate_map, instruction_data):
    count = 0
    display(crate_map)
    for curr in instruction_data:
        ### YOUR CODE HERE ###
        pass

    for key, val in crate_map.items():
        ### YOUR CODE HERE ###
        pass

    return ### YOUR CODE HERE ###

def move_crate_stacks(crate_map, instruction_data):
    count = 0
    display(crate_map)
    for curr in instruction_data:
        ### YOUR CODE HERE ###
        pass

    for key, val in crate_map.items():
        ### YOUR CODE HERE ###
        pass


    return ### YOUR CODE HERE ###