# write your code here
"""
(一) PEP8 代码长行
在此阶段，您的程序应从指定文件中读取 Python 代码并执行单个检查：代码行的长度不应超过 79 个字符。
1.文件的路径是从标准输入获取的。
2.一般的输出格式为：Line X: Code Message
其中 X 是行号，计数从 1 开始，Code 是发现的风格问题（如 S001）的代码，Message 是问题的可读描述 （可选）。
例如：Line 3: S001 Too long
3.行的顺序应始终是先到后。
4.您的程序可以输出另一条消息，而不是 Too long。输出的其余部分必须与提供的示例完全匹配。
在代码 S001 中，S 表示文体问题，001 是问题的内部编号。

以下是文件内容的示例：
print('What\'s your name?')
name = input()
print(f'Hello, {name}')  # here is an obvious comment: this prints a greeting with a name

very_big_number = 11_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000
print(very_big_number)

此代码包含两行长行（>79 个字符）：第 3 行和第 5 行。
以下是给定示例的预期输出：
Line 3: S001 Too long
Line 5: S001 Too long
"""

def check_line_length(file_path):
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if len(line) > 79:
                print(f"Line {line_number}: S001 Too long")


if __name__ == "__main__":
    check_line_length(input().strip())
