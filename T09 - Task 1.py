# While true loop to initate infinate loop
while True:

    # Defines input variables and opens text file to append
    # Menu changed to make user friendly!
    try:
        choice1 = int(input('\n1 - New Calculation' 
                            '\n2 - Print list of previous equations'
                            '\n3 - Exit'
                            '\n'
                            '\nPlease select from the menu: '))

        if choice1 == 1:

            input_num = (input('Enter two numbers, x,y:'))
            numbers = input_num.split(',')
            f = open('equations.txt','a') 

            no1 = float(numbers[0])
            no2 = float(numbers[1])

            # If statements with excpetions to handle exceptions in the number inputs
            if len(numbers) != 2:
                raise Exception

            # Input variable for operation
            # Menu changed to make user friendly too...
            operator = int(input('\n1 - Multiply' 
                            '\n2 - Divide'
                            '\n3 - Add'
                            '\n4 - Subtract'
                            '\n'
                            '\nselect from the menu: '))
        
            # If statements for arithmetic operations and appending to text file
            if operator == 1:
                x = no1 * no2
                answer = str(no1) + ' * ' + str(no2) + ' = ' + str(x)
                print(x)
                f.write('\n' + str(answer))
                f.close()

            elif operator == 2:
                x = no1 / no2
                answer = str(no1) + ' / ' + str(no2) + ' = ' + str(x)
                print(x)
                f.write('\n' + str(answer))
                f.close()
            
            elif operator == 3:
                x = no1 + no2
                answer = str(no1) + ' + ' + str(no2) + ' = ' + str(x)
                print(x)
                f.write('\n' + str(answer))
                f.close()

            elif operator == 4:
                x = no1 - no2
                answer = str(no1) + ' - ' + str(no2) + ' = ' + str(x)
                print(x)
                f.write('\n' + str(answer))
                f.close()

            #Exception handling for wrong operation input
            else:
                raise Exception

            '''
            I have not changed the code below. As i see it, the equations list when printed provide both the calcualtion and answer:

            "4 * 5 = 20"

            Code reviewers comment: 
            "Please note that the functionality for reading from a text file should return equations and their results. 
            Unfortunately, your program only returns equations."

            Please can my code be re-evaluated as I belive on this point, my code fulfils the requirements. 
            '''
      
        # Equations if statment executing the action by opening the file.
        # Wrting to a new variable and printing this variable.
        # file name replaced to be more descriptive
        elif choice1 == 2:
            while True:
                try: 
                    file_input = input('Enter the text file name you would like to open (\'equations\' will return previous calculations!):')
                    open_file = open(str(file_input)+'.txt','r')
                    equ_list = open_file.read()
                    print(equ_list)
                    open_file.close()
                    break
                except:
                    print('File does not exist! Please enter again.')
        elif choice1 == 3:
            print('\nGoodbye!\n')
            break
        
        else:
            raise Exception

    #Exception for logic errors 
    except Exception:
        print('Oops! your input was not expected. Please try again.')
        