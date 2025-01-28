try:
    a=int(input())
    b=int(input())
    print(a/b)
except ValueError as e:
    print("ValueError found",e)
except TypeError as e:
    print("typeerror found",e)
except Exception as e:
    print("exception found",e)
finally:
    print("finish")