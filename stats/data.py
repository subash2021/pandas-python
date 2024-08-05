
def generate_hashtag(s):
    #your code here
    all_criteria_met = False
    if not s:
        return False
    
    else:
        s = s.replace(' ','')
        s = s.capitalize()
        print(s)
        s = '#' + str(s)
        if len(s)>140:
            return False
        elif not s:
            return False
        
    return s
empty_string = ''
string_input = ' hello i Am Data '
string_input = string_input.strip().split(' ')
string_input = [s.capitalize() for s in string_input]
string_input = ''.join([item for item in string_input])
print(string_input)
#print(generate_hashtag(empty_string))
#print(generate_hashtag(string_input))