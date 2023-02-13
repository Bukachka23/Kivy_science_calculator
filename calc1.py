import math
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import re

# The main class of the application.
class MainWindow(BoxLayout):
    # This method takes in a string argument "calculation" which represents a mathematical expression and evaluates
    # it using the eval() function. The result of the evaluation is then assigned to the text property of an object referred to as self.display.
    # If there is a syntax error in the input expression, the text property of self.display is set to "Syntex Error".
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except:
                self.display.text = "Syntex Error"
    # This method takes in a string argument "input" and adds it to the text property of self.display.
    # If the text property of self.display is equal to "Syntex Error", "0" or "0.0", it is first reset to an empty string.
    def click(self, input):
        if (self.display.text == "Syntex Error" or self.display.text == "0" or self.display.text == "0.0"):
            self.display.text = ""
            self.display.text += input
        else:
            self.display.text += input
    # This method takes in a string argument "s" and removes the last character from it
    # by slicing the string and reassigning the resulting value to the text property of self.display.
    def delete(self, s):
        lenth = len(s)
        self.display.text = s[:-1]

    # This method takes in an integer argument "n" and calculates its factorial using the math.factorial() function.
    # The result of the calculation is then converted to a string
    def fact(self, n):
        val = math.factorial(n)
        self.display.text = str(val)
    # This method takes in a string argument "num" which represents a number and calculates its square root using the math.sqrt() function.
    # The result of the calculation is then converted to a string and returned by the method.
    def squrt(self, num):
        val = math.sqrt(float(num))
        return str(val)
    #
    def scientific(self, exp):
        # is used to check if the text property of self.display is empty.
        if (self.display.text == ""):
        # is used to reset the text property of self.display to an empty string.
            self.display.text = ""
        else:
            try:
                # value matching
                print("Raw Exp= " + exp + "\n")
                # is used to remove the 'e' character from the end of the string.
                exp = exp.replace("e", "2.7182818284590452353")
                exp = exp.replace("π", "3.14159265358979323846264338327950288419716939937510582097494459231")
                exp = exp.replace("^", "**")


                # is used to find the pattern '√' in the string.
                pattern = re.compile("√")
                # is used to find the pattern '√' in the string.
                matches = pattern.finditer(exp)
                i = 0
                y = {}
                for match in matches:
                    # is used to find the span of the pattern '√' in the string.
                    y[i] = match.span()
                    i = i + 1

                if (i != 0):
                    index = -5
                    for k in range(i - 1, -1, -1):
                        # print("y["+str(k)+"]=")
                        # print(y[k])
                        # is used to find the span of the pattern '√' in the string.
                        start1 = y[k][0]
                        # is used to find the span of the pattern '√' in the string.
                        end1 = y[k][1]
                        # index = len(exp) is
                        index = len(exp)
                        # print("start="+str(start1))
                        # print("End="+str(end1))
                        func_name = exp[y[k][0]:y[k][1]]
                        # print(func_name)

                        for l in range(end1, len(exp)):

                            # print(exp[l:l+1])
                            if ((exp[l:l + 1] == "(") or (exp[l:l + 1] == ")") or (exp[l:l + 1] == "*") or (
                                    exp[l:l + 1] == "-")
                                    or (exp[l:l + 1] == "/") or (exp[l:l + 1] == "+") or (exp[l:l + 1] == "\n")):
                                print(exp[l:l + 1])
                                index = l
                                break
                        # print(exp[start1:index])
                        # print("index="+str(index)+"\n")
                        exp = exp.replace(exp[start1:index], self.squrt(exp[start1 + 1:index]))
                    # print(exp)

                # is used to find the pattern 'sin' in the string.
                fns = {0: "log2", 1: "log10", 2: "ln", 3: "sin", 4: "cos", 5: "tan"}
                # this loop is used to find the pattern 'sin' in the string.
                for j in fns:
                    # print("\n\n")
                    pattern = re.compile(fns[j] + "[(](.*?)[)]")
                    #
                    matches = pattern.finditer(exp)
                    i = 0
                    x = {}
                    for match in matches:
                        x[i] = match.span()
                        i = i + 1

                    if (i != 0):
                        for k in range(i - 1, -1, -1):
                            # print(x[k])
                            start = x[k][0]
                            end = x[k][1]
                            # print("End="+str(end))
                            func_name = exp[x[k][0]:x[k][1]]
                            if (j == 0):
                                var = float(func_name[5:(end - start - 1)])  # find no under the fn
                                # print(func_name+"="+str(math.log(var,2)))
                                exp = exp.replace(func_name, str(math.log(var, 2)))
                            # print(exp)
                            if (j == 1):
                                var = float(func_name[6:(end - start - 1)])
                                # print(func_name+"="+str(math.log(var,10)))
                                exp = exp.replace(func_name, str(math.log(var, 10)))
                            # print(exp)
                            if (j == 2):
                                var = float(func_name[3:(end - start - 1)])
                                # print(func_name+"="+str(math.log(var,2.7182818284590452353)))
                                exp = exp.replace(func_name, str(math.log(var, 2.7182818284590452353)))
                            # print(exp)
                            if (j == 3):
                                var = float(eval(func_name[4:(end - start - 1)]))
                                # print(func_name+"="+str(math.sin(var)))
                                exp = exp.replace(func_name, str("{0:.2f}".format(round(math.sin(var)))))
                            # print(exp)
                            if (j == 4):
                                var = float(eval(func_name[4:(end - start - 1)]))
                                # print(func_name+"="+str(math.cos(var)))
                                exp = exp.replace(func_name, str("{0:.2f}".format(round(math.cos(var)))))
                            # print(exp)
                            if (j == 5):
                                var = float(eval(func_name[4:(end - start - 1)]))
                                # print(func_name+"="+str(math.tan(var)))
                                exp = exp.replace(func_name, str("{0:.5f}".format(round(math.tan(var)))))
                            # print(exp)

                print("Modified exp= " + exp)

                self.display.text = str(eval(exp))
            except:
                self.display.text = "Syntex Error"


gui = Builder.load_file("calc.kv")


class Calculator(App):
    def build(self):
        return gui


Calculator().run()