def main():
    user_input = input()
    print(convert(user_input))

def convert(text):
    return text.replace(':)', '🙂').replace(':(', '🙁')

#i dont get the __name__ == "__main__" part. can you explain it to me?Sure! In Python, the `if __name__ == "__main__":` statement is used to determine whether a Python script is being run as the main program or if it is being imported as a module into another script.
if __name__ == "__main__":
    main()
