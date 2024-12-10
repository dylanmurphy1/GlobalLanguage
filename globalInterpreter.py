class Interpreter:
    
    def interpret(string, variables):
        operators = '+-/*%'
        currentVariables = variables
        doElse = False
        doElif = False
        skip = False

        def varmap(var, state):
            if var in state:
                return state[var]
            else:
                return None

        # evaluates math expressions
        def math(expression):
            operation = ""
            symbols = []
            if any(char in expression for char in operators):
                for symbol in expression:
                    symbols.append(symbol)

                for op in symbols:
                    if (op == "+"):
                        operation = "+"
                        break
                    elif (op == "-"):
                        operation = "-"
                        break
                    elif (op == "/"):
                        operation = "/"
                        break
                    elif (op == "*"):
                        operation = "*"
                        break
                    elif (op == "%"):
                        operation = "%"
                        break
                
                numbers = expression.split(operation)
                if ('!' in numbers[0]):
                    firstNum = chr(translationToNum(numbers[0]))
                else:
                    numbers[0] = translationToNum(numbers[0])
                    firstNum = None
                if ('!' in numbers[1]):
                    secondNum = chr(translationToNum(numbers[1]))
                else:
                    numbers[1] = translationToNum(numbers[1])
                    secondNum = None
                
                if (type(numbers[0]) == int) and (type(numbers[1]) == int):
                    if (operation == "+"):
                        num1 = numbers[0]
                        num2 = numbers[1]
                        return num1 + num2
                    elif (operation == "-"):
                        num1 = numbers[0]
                        num2 = numbers[1]
                        return num1 - num2
                    elif (operation == "/"):
                        num1 = numbers[0]
                        num2 = numbers[1]
                        return num1 / num2
                    elif (operation == "*"):
                        num1 = numbers[0]
                        num2 = numbers[1]
                        return num1 * num2
                    elif (operation == "%"):
                        num1 = numbers[0]
                        num2 = numbers[1]
                        return num1 % num2
                    else:
                        return expression
                elif ((varmap(firstNum, currentVariables)) != None) and ((varmap(secondNum, currentVariables)) != None):
                    if (operation == "+"):
                        num1 = varmap(firstNum, currentVariables)
                        num2 = varmap(secondNum, currentVariables)
                        return num1 + num2
                    elif (operation == "-"):
                        num1 = varmap(firstNum, currentVariables)
                        num2 = varmap(secondNum, currentVariables)
                        return num1 - num2
                    elif (operation == "/"):
                        num1 = varmap(firstNum, currentVariables)
                        num2 = varmap(secondNum, currentVariables)
                        return num1 / num2
                    elif (operation == "*"):
                        num1 = varmap(firstNum, currentVariables)
                        num2 = varmap(secondNum, currentVariables)
                        return num1 * num2
                    elif (operation == "%"):
                        num1 = varmap(firstNum, currentVariables)
                        num2 = varmap(secondNum, currentVariables)
                        return num1 % num2
                    else:
                        return expression
                elif ((varmap(firstNum, currentVariables)) != None) and (type(numbers[1]) == int):
                    if (operation == "+"):
                        num1 = varmap(firstNum, currentVariables)
                        num2 = numbers[1]
                        return num1 + num2
                    elif (operation == "-"):
                        num1 = varmap(firstNum, currentVariables)
                        num2 = numbers[1]
                        return num1 - num2
                    elif (operation == "/"):
                        num1 = varmap(firstNum, currentVariables)
                        num2 = numbers[1]
                        return num1 / num2
                    elif (operation == "*"):
                        num1 = varmap(firstNum, currentVariables)
                        num2 = numbers[1]
                        return num1 * num2
                    elif (operation == "%"):
                        num1 = varmap(firstNum, currentVariables)
                        num2 = numbers[1]
                        return num1 % num2
                    else:
                        return expression
            else:
                return int(varmap(chr(translationToNum(expression)), currentVariables))

        # compares values
        def compare(val1, val2, operator):
            if operator == '=':
                return val1 == val2
            if operator == '<':
                return val1 < val2
            if operator == '>':
                return val1 > val2
            
        # translates symbols to numerical value
        def translationToNum(symbols):
            sum = 0
            for symbol in symbols:
                if symbol == '^':
                    sum += 100
                elif symbol == '@':
                    sum += 10
                elif symbol == '#':
                    sum += 1
            return sum
        
        # translates ASCII value to Global symbols
        def translationToSymbol(num):
            string = str(num)
            newSymbol = ""
            if len(string) == 2:
                tensDigit = int(string[0])
                while tensDigit > 0:
                    newSymbol += '@'
                    tensDigit -= 1
                onesDigit = int(string[1])
                while onesDigit > 0:
                    newSymbol += '#'
                    onesDigit -= 1
            elif len(string) == 3:
                hundredsDigit = int(string[0])
                while hundredsDigit > 0:
                    newSymbol += '^'
                    hundredsDigit -= 1
                tensDigit = int(string[1])
                while tensDigit > 0:
                    newSymbol += '@'
                    tensDigit -= 1
                onesDigit = int(string[2])
                while onesDigit > 0:
                    newSymbol += '#'
                    onesDigit -= 1
            return newSymbol

        # Interpreting commands    
        statements = string.split('\n')
        
        if varmap("currentStatementWhile", currentVariables) != None:
            currentStatement = varmap("currentStatementWhile", currentVariables)
        else:
            currentStatement = 0
        
        for statement in statements:
            withSpacesStatement = statement
            statement = statement.replace(" ", "")
            
            # if, else if, else statements
            if "???" in statement:
                condition = statement.replace("?", "")
                if any(op in statement for op in operators) and '=' in statement:
                    expression, result = condition.split("=")
                    expressionValue = math(expression)
                    result = translationToNum(result)
                    if expressionValue == result:
                        doElse = False
                        doElif = False
                        skip = False
                        currentStatement += 1
                        continue
                    else:
                        doElse = True
                        doElif = True
                        skip = True
                        currentStatement += 1
                        continue
            if ("??" in statement) and (doElif == False):
                skip = True
            elif ("??" in statement) and (doElif == True):
                condition = statement.replace("??", "")
                if any(op in statement for op in operators) and '=' in statement:
                    expression, result = condition.split("=")
                    expressionValue = math(expression)
                    result = translationToNum(result)
                    if expressionValue == result:
                        doElse = False
                        doElif = False
                        skip = False
                        currentStatement += 1
                        continue
                    else:
                        doElse = True
                        skip = True
                        currentStatement += 1
                        continue
            if ("?" in statement) and (doElse == True):
                skip = False
            elif ("?" in statement) and (doElse == False):
                skip = True
            # End of IF/ELF/ELSE statement
            if '}' in statement:
                skip = False
            
            # Assignment
            if ('~' in statement) and (skip == False):
                statement = statement.replace("~", "")
                if any(op in statement for op in operators) and '=' in statement:
                    varName, expression = statement.split("=")
                    varName = chr(translationToNum(varName))
                    varValue = math(expression)
                else:
                    varName, varValue = statement.split("=")
                    varName = chr(translationToNum(varName))
                    varValue = translationToNum(varValue)

                currentVariables[varName] = varValue
            
            # Printing
            if ('$' in statement) and (skip == False):
                statement = statement.replace("$", "")
                if statement == "\"\"":
                    print(" ")
                elif "\"" in statement:
                    statement = statement.replace("\"", "")
                    if ("," in statement) and ("-" in statement):
                        sentence = ""
                        words = statement.split("-")
                        for w in words:
                            wordInSentence = ""
                            letters = w.split(",")
                            for l in letters:
                                wordInSentence += chr(translationToNum(l))
                            sentence += wordInSentence
                            sentence += " "
                        sentence = sentence[:-1]
                        print(sentence)
                    elif "," in statement:
                        word = ""
                        letters = statement.split(",")
                        for letter in letters:
                            word += chr(translationToNum(letter))
                        print(word)
                    else:
                        print(chr(translationToNum(statement)))
                else:
                    varName = chr(translationToNum(statement))
                    if varmap(varName, currentVariables) == None:
                        raise NameError("variable not defined: " + varName)
                    else:
                        print(varmap(varName, currentVariables))

            # WHILE loops    
            if "∞" in statement:
                whileCode = ""
                i = currentStatement
                while ('|' in statements[i + 1]) == False:
                    whileCode += statements[i + 1]
                    whileCode += "\n"
                    i += 1
                whileCode = whileCode.replace(" ", "")
                condition = statement.replace("∞", "")
                if '=' in condition:
                    comparison = '='
                    expression, result = condition.split("=")
                    expressionValue = math(expression)
                    result = translationToNum(result)
                    if expressionValue == result:
                        skip = False
                    else:
                        skip = True
                elif '<' in condition:
                    comparison = '<'
                    expression, result = condition.split("<")
                    expressionValue = math(expression)
                    result = translationToNum(result)
                    if expressionValue < result:
                        skip = False
                    else:
                        skip = True
                elif '>' in condition:
                    comparison = '>'
                    expression, result = condition.split(">")
                    expressionValue = math(expression)
                    result = translationToNum(result)
                    if expressionValue > result:
                        skip = False
                    else:
                        skip = True
                currentVariables["currentStatementWhile"] = currentStatement + 1
                while compare(expressionValue, result, comparison):
                    Interpreter.interpret(whileCode, currentVariables)
                    expressionValue = math(expression)
                del currentVariables["currentStatementWhile"]
                skip = True

            # FOR loops
            if "&" in statement:
                statement = statement.replace("&", "")
                counter, loopRange = statement.split("(")
                counterValue = varmap(chr(translationToNum(counter)), currentVariables)
                loopRange = loopRange.replace(")", "")
                low, high = loopRange.split(",")
                totalLoops = translationToNum(high) - translationToNum(low)
                forCode = ""
                i = currentStatement
                while ('|' in statements[i + 1]) == False:
                    forCode += statements[i + 1]
                    forCode += "\n"
                    i += 1
                forCode = forCode.replace(" ", "")
                currentVariables["currentStatementFor"] = currentStatement + 1
                while varmap(chr(translationToNum(counter)), currentVariables) <= totalLoops:
                    Interpreter.interpret(forCode, currentVariables)
                    counterValue += 1
                    currentVariables[chr(translationToNum(counter))] = counterValue
                del currentVariables["currentStatementFor"]
                skip = True

            # End of while/for loop
            if '|' in statement:
                skip = False

            # English to Global method
            if ':' in withSpacesStatement:
                withSpacesStatement = withSpacesStatement.replace(": ", "")
                final = ""
                for char in withSpacesStatement:
                    if char == " ":
                        final = final[:-1]
                        final += "-"
                    else:
                        charValue = ord(char)
                        final += translationToSymbol(charValue)
                        final += ","
                final = final[:-1]
                print(final)

            # prints instructions and rules
            if '¿' in statement:
                fileName = "dictionary.txt"
                file = open(fileName)
                fileContents = file.readlines()
                for line in fileContents:
                    print(line)
                    
            # Move to next statement
            currentStatement += 1

defaultVariables = {}
# Reading input from files
fileName = "example.global"
file = open(fileName)
fileContents = file.readlines()
codeString1 = ""
for line in fileContents:
    codeString1 += line
Interpreter.interpret(codeString1, defaultVariables)
defaultVariables = {}