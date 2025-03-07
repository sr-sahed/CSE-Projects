class CustomError(Exception):
    pass

try:
    raise CustomError("Something went wrong!")
except CustomError as e:
    print(e)
