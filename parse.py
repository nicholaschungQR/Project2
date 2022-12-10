'''
import.py

Helper code designed for importing .txt file data
into string
'''

def parse_txt_to_str(file_path):
    '''
    parses .txt file to str

        Parameters:
            file_path (str): file path, must be .txt
        
        Returns:
            string contents of .txt file
    '''

    f = open(file_path, 'r')
    content = f.read()
    return content
