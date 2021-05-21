# date: 27/04/2021
# This function receives a list of strings that are arithmetic problems 
# and returns the problems arranged vertically and side-by-side. The function 
# optionally takes a second argument. When the second argument is set to True, 
# the answers of the arithmetic is displayed.

def arithmetic_arranger(maths_problems, calculate=None):  # sourcery no-metrics
    
    # split all inputs into useable pieces i.e. interger operands and operators
    if len(maths_problems) <= 5:

        split_up_the_problems = [_.split() for _ in maths_problems]

        worked_out_values = []

        operators = [_[1] for _ in split_up_the_problems[:]]

        upper_operand_content_in_strings = [_[0] for _ in split_up_the_problems[:]]
        upper_operand_digits = [_[0] for _ in split_up_the_problems[:]]

        lower_operand_content_in_strings = [_[2] for _ in split_up_the_problems[:]]
        lower_operand_digits = [_[2] for _ in split_up_the_problems[:]]
                
        upper_operands_length_check = [len(_) for _ in upper_operand_content_in_strings]

        lower_operands_length_check = [len(_) for _ in lower_operand_content_in_strings]

        # report error messages where any of the conditions is voilated
        if any(_ for _ in upper_operand_content_in_strings if not _.isdigit()) or any(_ for _ in lower_operand_content_in_strings if not _.isdigit()):
            arranged_problems = "Error: Numbers must only contain digits."
            
        
        elif any(_ for _ in (upper_operands_length_check + lower_operands_length_check) if _ > 4):
            arranged_problems = "Error: Numbers cannot be more than four digits."
            
        
        elif '*' in operators or '/' in operators:
            arranged_problems = "Error: Operator must be '+' or '-'."
            
        
        else:
            for _ in range(len(upper_operand_digits)):
                upper_operand_digits[_] = int(upper_operand_digits[_]) # convert string to integer value and replace its value in the list. lists are mutable objects.
            
            for _ in range(len(lower_operand_digits)):
                lower_operand_digits[_] = int(lower_operand_digits[_]) # convert string to integer value and replace its value in the list. lists are mutable objects.
            
            # initialise variables to be used later
            empty_space = " "
            arranged_problems = ""

            if calculate == True:
                for _ in range(len(operators)):

                    if operators[_] == "+":
                        worked_out_values.append(upper_operand_digits[_] + lower_operand_digits[_]) # add the operands

                    if operators[_] == "-":
                        worked_out_values.append(upper_operand_digits[_] - lower_operand_digits[_]) # subtract the operands
                        
            for _ in range(len(upper_operand_digits)):
                width_of_upper_line_characters = max(len(str(upper_operand_digits[_])), len(str(lower_operand_digits[_]))) + 2 # general formula for the length of characters.
                arranged_problems += str(upper_operand_digits[_]).rjust(width_of_upper_line_characters) + empty_space * 4 # collect the strings
            arranged_problems = arranged_problems.rstrip() # make a copy of the string before modifying it. strings are immutable objects.
            arranged_problems += '\n'
                       
            for _ in range(len(lower_operand_digits)):
                width_of_lower_line_characters = max(len(str(upper_operand_digits[_])), len(str(lower_operand_digits[_]))) + 1 # general formula for the length of characters.
                arranged_problems += (str(operators[_])) + (str(lower_operand_digits[_])).rjust(width_of_lower_line_characters) + empty_space * 4 # accumalatively collect the strings
            arranged_problems = arranged_problems.rstrip() # make a copy of the string before modifying it. strings are immutable objects.
            arranged_problems += '\n'

            for _ in range(len(lower_operand_digits)):
                dashes = max(len(str(upper_operand_digits[_])), len(str(lower_operand_digits[_]))) + 2 # general formula for the number of dashes.
                arranged_problems += '-' * dashes + empty_space * 4 # accumalatively collect the strings
            arranged_problems = arranged_problems.rstrip() # make a copy of the string before modifying it. strings are immutable objects.

            if calculate == True:
                arranged_problems += '\n'
                for _ in range(len(worked_out_values)):
                    width_of_answers_line_characters = max(len(str(upper_operand_digits[_])), len(str(lower_operand_digits[_]))) + 2 # general formula for the length of characters.
                    arranged_problems += str(worked_out_values[_]).rjust(width_of_answers_line_characters) + empty_space * 4 # accumalatively collect the strings
                arranged_problems = arranged_problems.rstrip() # make a copy of the string before modifying it. strings are immutable objects.
                        
    else:
        arranged_problems = "Error: Too many problems."
            
    return print(arranged_problems) # return the collated strings

###### WORKING TEST BENCH AREA ######
if __name__ == '__main__':
    arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])

    arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
    arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], True)
    arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])
    arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True)
    arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])

    arithmetic_arranger(["32 + 698", "3jjk01 - 2", "45 + 43", "123 + 49"])
    arithmetic_arranger(["32 + 698", "3jjk01 - 2", "45 + 43", "123 + 49"], True)

    arithmetic_arranger(["32 + 698", "380231 - 2", "45 + 43", "123 + 49"])
    arithmetic_arranger(["32 + 698", "380231 - 2", "45 + 43", "123 + 49"], True)

    arithmetic_arranger(["32 * 698", "3801 - 2", "45 + 43", "123 + 49"])
    arithmetic_arranger(["32 * 698", "3801 - 2", "45 + 43", "123 + 49"], True)

    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)

    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "1233 + 459", "4335 + 5543"])
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "1233 + 459", "4335 + 5543"], True)

    arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])

    arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])
    arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])
    arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])




