

a = "fdfdf"
def test_raise(a):
    try:
        if not a.isdigit():
            raise ValueError("is not digital.")

    except Exception as e:
        print(e.args,e.__cause__,e.__context__,e.__suppress_context__,e.__traceback__)
        raise
    else:
        print("没有异常的时候执行语句 1.")
    finally:
        print("finally.")

    print("没有异常的时候执行语句 2.")


if __name__ == '__main__':

    try:
        test_raise("a")
    except Exception as e:
        print("上层异常处理：", repr(e))

    print("程序结束")
