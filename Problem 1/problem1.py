'''
Problem 1

Driver Code
'''

def calorie_count(calorie_data):
    '''
    Builds list of calorie data carried by each 
    individual, separated by a newline delimiter

        Parameters:
            calorie_data (str): all calorie data 
            where consecutive integers are calorie 
            counts belonging to the same elf

        Example:
            100
            200
            300

            200
            400

            500

            would be represented as

            600,
            600,
            500

        *** Special Challenge ***
        No libraries used!
    '''
    calorie_list = []
    calorie_list = calorie_data.split('\n\n')

    calorie_sum = []
    for i in calorie_list:
        ### YOUR CODE HERE ###
        pass
        
    return calorie_sum

def largest_calorie_count(calorie_sum):
    '''
    Returns value and position of largest 
    calorie sum in list

        Parameters:
            calorie_sum (list): contains sums of 
            all calorie integers
    '''
    ### YOUR CODE HERE ###

    return

def largest_three_calorie_count(calorie_list):
    '''
    Returns sum of the largest three calorie counts 
    in list

        Parameters:
            calorie_list (list): contains sums of 
            all calorie integers
    '''
    ### YOUR CODE HERE ###
    return 