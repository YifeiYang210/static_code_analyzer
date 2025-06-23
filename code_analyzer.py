# write your code here
import sys
import os
import re
import ast

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
    """
    （五）分析参数和变量
    ast 模块还包含许多表示 Python 语法的不同元素的类。
    例如，类 FunctionDef 是树的一个节点，表示代码中某个函数的定义，
    类 arguments 表示函数的参数，类 Assign 表示一个表达式，其中的值被分配给某个变量。
    您可以使用所有这些（和其他）类来查找要检查正确性的代码（变量名称等）的位置。

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            function_name = node.name
            # check whether the function's name is written in camel_case
            pass

    在这个最后阶段，你需要改进你的程序，检查函数参数的所有名称以及局部变量是否满足 PEP8 的要求。
    程序不得强制在函数之外（例如，在模块或类中）使用变量的名称。
    最方便的方法是使用 ast 模块中的抽象语法树 （AST）。
    此外，您的程序必须检查给定的代码是否不使用可变值（列表、字典和集合）作为默认参数，以避免程序中出现错误。
    您需要向分析器添加三个新检查：
    [S010] 参数名称 arg_name 应以 snake_case 编写;
    [S011] 变量 var_name 应该用 snake_case 编写;
    [S012] 默认参数值为 mutable。

    1.函数名称以及函数体中的变量名称应以 snake_case 书写。
    但是，只有在定义了函数时，才应输出无效函数名称的错误消息。
    仅当为该变量分配了值时，才应输出无效变量名称的错误消息，而不是在代码中进一步使用此变量时输出。

    2.为了简化任务，你只需要检查可变值是否直接赋值给一个参数：
    def fun1(test=[]):  # default argument value is mutable
        pass
        
    def fun2(test=get_value()):  # you can skip this case to simplify the problem
        pass
        
    3.如果一个函数包含多个可变参数，则此函数的消息应该只输出一次。
    4.如果变量和参数名称是用 snake_case 编写的，则假定它们有效。初始下划线 （_） 也是可以接受的。

    下面是一个输入示例：
    CONSTANT = 10
    names = ['John', 'Lora', 'Paul']


    def fun1(S=5, test=[]):  # default argument value is mutable
        VARIABLE = 10
        string = 'string'
        print(VARIABLE)

    /path/to/file/script.py: Line 5: S010 Argument name 'S' should be snake_case
    /path/to/file/script.py: Line 5: S012 Default argument value is mutable
    /path/to/file/script.py: Line 6: S011 Variable 'VARIABLE' in function should be snake_case
    请注意，不会打印 print（VARIABLE） 行的消息，因为它已经输出到第 6 行，其中变量 VARIABLE 被分配了一个值。
    """
    with open(file_path, encoding='utf-8') as f:
        lines = f.readlines()

    # Construct snake_case (allowing double underscores before/after)
    snake_re = re.compile(r'^_{0,2}[a-z][a-z0-9_]*_{0,2}$')
    source_code = ''.join(lines)
    ast_issues: dict[int, list[str]] = {}

    # Help function: recursively extract variable names from the assignment target
    def _extract_names(target):
        if isinstance(target, ast.Name):
            return [target.id]
        if isinstance(target, (ast.Tuple, ast.List)):
            names = []
            for elt in target.elts:
                names.extend(_extract_names(elt))
            return names
        return []
    
    try:
        tree = ast.parse(source_code)
    except SyntaxError:
        tree = None
    
    if tree:
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                # ---------- S010：arg_name should be snake_case ----------
                """
                def fn(a, b=1, /, c, *args, d, e=2, **kwargs)
                posonlyargs: [a, b]  仅限位置参数 (/ 左侧, Python3.8+)
                args: [c]            标准位置参数 (位于 / 和 * 之间, 或没有特殊符号)
                vararg: args         关键字参数 (* 右侧)
                kwonlyargs: [d, e]   *args (如果存在)
                kwarg: kwargs        **kwargs (如果存在)
                """ 
                all_args = (
                    node.args.posonlyargs +
                    node.args.args +
                    node.args.kwonlyargs
                )
                # *arg / **kwarg
                if node.args.vararg:
                    all_args.append(node.args.vararg)
                if node.args.kwarg:
                    all_args.append(node.args.kwarg)

                for arg in all_args:
                    if not snake_re.fullmatch(arg.arg):
                        ast_issues.setdefault(arg.lineno, []).append(
                            f"S010 Argument name '{arg.arg}' should be snake_case"
                        )

                # ---------- S012：可变默认值 ----------
                mutable_found = any(
                    isinstance(d, (ast.List, ast.Dict, ast.Set))
                    for d in (node.args.defaults + node.args.kw_defaults)
                    if d is not None      # kw_defaults 可含 None
                )
                if mutable_found:
                    ast_issues.setdefault(node.lineno, []).append(
                        "S012 Default argument value is mutable"
                    )

                # ---------- S011：局部变量名var_name should be snake_case ----------
                reported_vars = set()
                for inner in ast.walk(node):
                    """
                    ast.Assign: 用于标准赋值，可以同时给多个目标赋值（包括元组解包）。
                    ast.AnnAssign: 用于带类型注解的赋值，只能给单个目标赋值，可以有初始值也可以没有。
                    ast.AugAssign: 用于增强赋值（如+=），只能给单个目标赋值。
                    a = 1
                    b: int = 2
                    c += 3
                    对应 AST 结构
                    Module(
                        body=[
                            Assign(targets=[Name(id='a')], value=Constant(value=1)),
                            AnnAssign(
                                target=Name(id='b'),
                                annotation=Name(id='int'),
                                value=Constant(value=2),
                                simple=1
                            ),
                            AugAssign(
                                target=Name(id='c'),
                                op=Add(),
                                value=Constant(value=3)
                            )
                        ]
                    )
                    """
                    if isinstance(inner, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
                        # 获取所有赋值目标
                        targets = []
                        if isinstance(inner, ast.Assign):
                            targets = inner.targets
                        else:  # AnnAssign / AugAssign
                            targets = [inner.target]  # 单个节点属性转化为列表，兼容上面可多个目标赋值

                        for tgt in targets:
                            for var_name in _extract_names(tgt):
                                if (var_name not in reported_vars and
                                        not snake_re.fullmatch(var_name)):
                                    ast_issues.setdefault(inner.lineno, []).append(
                                        f"S011 Variable '{var_name}' in function should be snake_case"
                                    )
                                    reported_vars.add(var_name)

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
            # S009: The function name must be snake_case
                #   1. allow __init__ / _private / public_
                #   2. others must be logit, _, a-z
            else:  # keyword == 'def'
                if not re.fullmatch(r'(_{0,2}[a-z][a-z0-9_]*_{0,2})', name):
                    issues.append(f"S009 Function name '{name}' should use snake_case")
        
        # Check for AST issues
        issues.extend(ast_issues.get(line_number, []))

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

