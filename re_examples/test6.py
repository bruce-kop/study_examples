'''
escape(pattern)
可以对字符串中所有可能被解释为正则运算符的字符进行转义的应用函数。
如果字符串很长且包含很多特殊技字符，而你又不想输入一大堆反斜杠，
或者字符串来自于用户(比如通过raw_input函数获取输入的内容)，
且要用作正则表达式的一部分的时候，可以使用这个函数。
'''