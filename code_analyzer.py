# write your code here

def check_line_length(file_path):
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
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if len(line) > 79:
                print(f"Line {line_number}: S001 Too long")


def check_style_issues(file_path):
    """
    (二) PEP8 更多风格
    让我们向程序添加更多检查。所有这些都与 PEP8 风格指南一致。
    在此阶段，您需要向程序添加对以下 5 个错误的检查：
    1.[S002] 缩进不是 4 的倍数;
    2.[S003] 语句后不必要的分号（请注意，分号在注释中是可以接受的）;
    3.[S004] 内联注释前少于两个空格;
    4.[S005] 找到TODO（仅在评论中且不区分大小写）;
    5.[S006] 代码行前有两个以上的空行（适用于第一个非空行）
    请注意：
    1.在 Python 中，每行代码都可以为空，包含语句和/或注释。
    因此，您可以通过检查代码相对于行中第一个 '#' 符号的位置来轻松确定代码的一部分是在注释还是语句中。
    2.如果一行多次包含相同的样式问题，则程序应仅打印一次信息。但是，如果一行具有多个具有不同类型错误代码的问题，则应将它们打印为排序列表。
    3.为了简化任务，如果您的程序在字符串中发现一些误报样式问题，尤其是在多行（'''...'''） 中，我们认为这是可以接受的。
    4.我们建议您将代码分成一组函数以避免混淆。
    再强调一次：
    1.包含 Python 代码的文件的路径是从标准输入中获得的。
    2.一般的输出格式为：Line X: Code Message
    3.发现问题的行必须按升序输出。

    下面是一个样式不佳的 Python 代码示例（请不要编写这样的代码！）：
    print('What\'s your name?') # reading an input
    name = input();
    print(f'Hello, {name}');  # here is an obvious comment: this prints a greeting with a name


    very_big_number = 11_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000
    print(very_big_number)



    def some_fun():
        print('NO TODO HERE;;')
        pass; # Todo something

    它包含 9 个代码样式问题：
    Line 1: S004 At least two spaces required before inline comments
    Line 2: S003 Unnecessary semicolon
    Line 3: S001 Too long
    Line 3: S003 Unnecessary semicolon
    Line 6: S001 Too long
    Line 11: S006 More than two blank lines used before this line
    Line 13: S003 Unnecessary semicolon
    Line 13: S004 At least two spaces required before inline comments
    Line 13: S005 TODO found
    """
    with open(file_path, encoding='utf-8') as f:
        lines = f.readlines()

    blankline_count = 0
    for line_number, line in enumerate(lines, start=1):
        issues = []
        stripped_line = line.strip()

        # Check for line length
        if len(line) > 79:
            issues.append("S001 Too long")
        
        # Check for indentation not being a multiple of 4
        if stripped_line and (len(stripped_line) - len(stripped_line.lstrip())) % 4 != 0:
            issues.append("S002 Indentation is not a multiple of four")
        
        # Check for unnecessary semicolons
        if stripped_line and ';' in stripped_line:
            # Ignore semicolons in comments
            if '#' in stripped_line:
                comment_index = stripped_line.index('#')
                if ';' in stripped_line[:comment_index]:
                    issues.append("S003 Unnecessary semicolon")
            # Ignore semicolons between strings
            elif '"' in stripped_line or "'" in stripped_line:
                string_delimiter = '"' if '"' in stripped_line else "'"
                if ';' in stripped_line.split(string_delimiter, 1)[0]:
                    issues.append("S003 Unnecessary semicolon")
            else:
                issues.append("S003 Unnecessary semicolon")
        
        # Check for inline comments with less than two spaces before them
        if '#' in stripped_line:
            comment_index = stripped_line.index('#')
            if stripped_line[(comment_index - 2):comment_index] != '  ':
                issues.append("S004 At least two spaces required before inline comments")
        
        # Check for TODO comments and ignore case
        if '#' in stripped_line:
            comment_index = stripped_line.index('#')
            if 'todo' in stripped_line[comment_index + 1:].lower():
                issues.append("S005 TODO found")
        
        # Check for more than two blank lines before this line
        if not stripped_line:
            blankline_count += 1
        else:
            if blankline_count > 2:
                issues.append('S006 More than two blank lines used before this line')
            blankline_count = 0  # 重置
        
        # Print issues if any
        if issues:
            for issue in sorted(set(issues)):
                print(f"Line {line_number}: {issue}")


if __name__ == "__main__":
    check_style_issues(input().strip())
    # check_style_issues('test.py')
