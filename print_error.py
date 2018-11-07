## You have to write a function printer_error which given a string will output the error rate of the printer as a string 
# representing a rational whose numerator is the number of errors and the denominator the length of the control string. 
# Don't reduce this fraction to a simpler expression.
# The string has a length greater or equal to one and contains only letters from ato z.


def error_string(s):
    TARGET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
    #Step1 Find alphates which ate out of range.
    error = 0
    for i in range(0, len(s) - 1):
        if s[i] not in TARGET:
    #Step2 Count the number of such an alphabet
            error += 1
    #Step3 return the ratio of such an string 
    return str(error) + "/" + len(s)
