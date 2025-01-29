class StringClass:
    def __init__(key):
        key.input_string = ""
    def getString(key):
        key.input_string = input("Enter a string: ")
    def printString(key):
        print(key.input_string.upper())
if __name__ == "__main__":
    string_obj = StringClass()
    string_obj.getString()  
    string_obj.printString() 