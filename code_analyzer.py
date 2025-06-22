# write your code here
import sys
import os
import re

def is_in_string(line, character):
    """检查行中是否包含字符串中的注释符号"""
    quote_char = None
    escaped = False
    
    for i, char in enumerate(line):
        if char == '\\':
            escaped = not escaped  # 切换转义状态
            continue
            
        if not escaped:
            if quote_char is None and char in ('"', "'"):
                # 进入引号区域
                quote_char = char
            elif char == quote_char:
                # 离开引号区域
                quote_char = None
        
        # 遇到注释符号且不在引号中
        if char == character and quote_char is None:
            return False  # 这是真正的注释符号
            
        escaped = False

    return True  # 未找到未在字符串中的注释符号


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


def check_style_issues(file_path, return_results=False):
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
    3.为了简化任务，如果您的程序在字符串中发现一些误报样式问题，尤其是在多行注释（'''...'''） 中可以不考虑，我们认为这是可以接受的。
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
    """
    (四) 命名应遵循PEP样式指南
    在 Python 中，基本要求是对函数名称使用 snake_case，对类名称使用 CamelCase。
    此外，构造名称和对象名称之间应只有一个空格。
    查看有关正则表达式的 Python 教程 ：它们将帮助您实现检查。
    在这个阶段，我们需要向程序添加三个新的检查：
    [S007] def 或 class 等构造名称后有太多空格;
    [S008] 类名 class_name 应该用 CamelCase 编写;
    [S009] 函数名 function_name 应该用 snake_case 编写。
    请注意：
    1.函数名称可以以下划线（__fun、__init__）开头或结尾.
    2.为了简化任务，我们将假设类的编写始终如以下示例所示
    # a simple class
    class MyClass:
        pass

    # a class based on inheritance
    class MyClass(AnotherClass):
        pass

    实际上，可以这样声明一个类：
    class \
            S:
        pass
    但是，由于它不是声明类的常用方法，因此您可以忽略它。

    3.另一个假设是函数总是像这样声明的：
    def do_magic():
        pass

    下面是一个输入示例：
    class  Person:
        pass

    class user:

        def __init__(self, login: str, password: str):
            self.login = login
            self.password = password

        @staticmethod
        def _print1():
            print('q')

        @staticmethod
        def Print2():
            print('q')

    此代码的预期输出为：
    /path/to/file/script.py: Line 1: S007 Too many spaces after 'class'
    /path/to/file/script.py: Line 4: S008 Class name 'user' should use CamelCase
    /path/to/file/script.py: Line 15: S009 Function name 'Print2' should use snake_case
    """
    with open(file_path, encoding='utf-8') as f:
        lines = f.readlines()

    results = []
    blankline_count = 0
    for line_number, line in enumerate(lines, start=1):
        issues = []
        stripped_line = line.strip()

        # Check for line length
        if len(line) > 79:
            issues.append("S001 Too long")
        
        # Check for indentation not being a multiple of 4
        if stripped_line and (len(line) - len(line.lstrip())) % 4 != 0:
            issues.append("S002 Indentation is not a multiple of four")
        
        # Check for unnecessary semicolons
        if stripped_line and ';' in stripped_line and not is_in_string(stripped_line, ';'):
            # Ignore semicolons in comments
            if '#' in stripped_line:
                comment_index = stripped_line.index('#')
                if ';' in stripped_line[:comment_index]:
                    issues.append("S003 Unnecessary semicolon")
            else:
                issues.append("S003 Unnecessary semicolon")
        
        # Check for inline comments with less than two spaces before them
        # must inline not standalone comment
        if '#' in stripped_line and not is_in_string(stripped_line, '#') and not stripped_line.startswith('#'):
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
        
        kw_match = re.match(r'^(\s*)(def|class)(\s+)([A-Za-z_][A-Za-z0-9_]*)', line)
        if kw_match:
            leading_ws, keyword, gap, name = kw_match.groups()

            # S007: The number of spaces after the keyword must be 1
            if len(gap) > 1:
                issues.append("S007 Too many spaces after 'class' or 'def'")

            # S008: The class name must be CamelCase (capitalized first letter, no underline)
            if keyword == 'class':
                if not re.fullmatch(r'[A-Z][a-zA-Z0-9]*', name):
                    issues.append(f"S008 Class name '{name}' should use CamelCase")
            # S009: The function name must be snake_case (allowing single underscore or dunder before/after)
                #   1. 允许形如 __init__ / _private / public_
                #   2. 其余必须全部小写字母、数字、下划线
            else:  # keyword == 'def'
                if not re.fullmatch(r'(_{0,2}[a-z][a-z0-9_]*_{0,2})', name):
                    issues.append(f"S009 Function name '{name}' should use snake_case")
        
        
        # Print issues if any
        if issues:
            if return_results:
                for issue in sorted(set(issues)):
                    results.append((line_number, issue))
            else:
                for issue in sorted(set(issues)):  # 去重并排序
                    print(f"Line {line_number}: {issue}")

    if return_results:
        return results


def analyze_project():
    """
    (三) 分析项目
    在此阶段，您需要改进程序，使其能够分析指定目录中的所有 Python 文件。
    1.您还需要更改输入格式。程序必须将其作为命令行参数获取，而不是从标准输入中读取路径：
    > python code_analyzer.py directory-or-file
    2.输出格式也需要稍微更改。它应包含已分析文件的路径：
    Path: Line X: Code Message 
    3.所有输出行必须根据文件名、行号和问题代码按升序排序。

    再强调一次：
    1.如果一行多次包含相同的样式问题，则程序必须只打印一次信息。
    2.如果一行有多个具有不同类型错误代码的问题，则应按升序打印它们。
    3.我们建议您将程序代码分解为一组函数和类，以避免混淆。

    示例 1. 仅指定一个文件作为输入：
    > python code_analyzer.py /path/to/file/script.py
    /path/to/file/script.py: Line 1: S004 At least two spaces required before inline comments
    /path/to/file/script.py: Line 2: S003 Unnecessary semicolon
    /path/to/file/script.py: Line 3: S001 Too long line
    /path/to/file/script.py: Line 3: S003 Unnecessary semicolon
    /path/to/file/script.py: Line 6: S001 Too long line
    /path/to/file/script.py: Line 11: S006 More than two blank lines used before this line
    /path/to/file/script.py: Line 13: S003 Unnecessary semicolon
    /path/to/file/script.py: Line 13: S004 At least two spaces required before inline comments
    /path/to/file/script.py: Line 13: S005 TODO found

    示例 2. 输入路径是一个目录;输出应包含其中的所有 Python 文件：
    > python code_analyzer.py /path/to/project
    /path/to/project/__init__.py: Line 1: S001 Too long line
    /path/to/project/script1.py: Line 1: S004 At least two spaces required before inline comments
    /path/to/project/script1.py: Line 2: S003 Unnecessary semicolon
    /path/to/project/script2.py: Line 1: S004 At least two spaces required before inline comments
    /path/to/project/script2.py: Line 3: S001 Too long line
    /path/to/project/somedir/script.py: Line 3: S001 Too long line
    /path/to/project/test.py: Line 3: Line 13: S003 Unnecessary semicolon
    """
    path = sys.argv[1]

    if os.path.isfile(path):
        results = check_style_issues(path, return_results=True)
        if results:
            for line_info, issue in results:
                print(f"{path}: Line {line_info}: {issue}")
    elif os.path.isdir(path):
        directory = path
        folder_results = []

        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    folder_results.append((file_path, check_style_issues(file_path, return_results=True)))

        # Sort results by file path and line number
        folder_results.sort(key=lambda x: (x[0], x[1]))

        for file_path, results in folder_results:
            for line_info, issue in results:
                print(f"{file_path}: Line {line_info}: {issue}")


if __name__ == "__main__":
    analyze_project()

