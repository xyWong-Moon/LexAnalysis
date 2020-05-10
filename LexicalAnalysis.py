__author__ = 'WangXinyuan'

Reserved = ['char', 'int', 'if', 'else', 'var', 'return', 'break',
            'do', 'while', 'for', 'double', 'float', 'then',
            'end', 'repeat', 'until', 'read', 'write']  # 保留字
SpecialSymbol = ['<', '>', '=', '+', '-', '*', '/', ':', ';', '(', ')', '[', ']', '|', '"', ',', '&']  # 特殊符号
sign = 0


def GetToken(sentence, row):  # 1：保留字或标识符 2:数字 3:符号
    word_temp = []  # 用于存放word
    global sign
    while sentence[sign] == (" " or "  "):#清除空格
        sign = sign + 1

    if ("A" <= sentence[sign] <= "Z") or ("a" <= sentence[sign] <= "z"):  # 1
        word_temp += sentence[sign]
        sign = sign + 1
        while ("A" <= sentence[sign] <= "Z") or ("a" <= sentence[sign] <= "z") or ("0" <= sentence[sign] <= "9"):
            word_temp += sentence[sign]
            sign = sign + 1
        word = ''.join(word_temp)
        for i in range(len(Reserved)):  # 判断保留字
            if word == Reserved[i]:
                print("\t" + str(row + 1) + ":Reserved word: " + word)
                return 1
        print("\t" + str(row + 1) + ":ID: name = " + word)
        return 1

    elif "0" <= sentence[sign] <= "9":  # 2
        isPoint = False  # 判断是否为浮点型，默认整形
        word_temp += sentence[sign]
        sign = sign + 1
        while "0" <= sentence[sign] <= "9":
            word_temp += sentence[sign]
            sign = sign + 1

        if sentence[sign] == ".":  # 浮点型
            isPoint == True
            word_temp += sentence[sign]
            sign = sign + 1
            while "0" <= sentence[sign] <= "9":
                word_temp += sentence[sign]
                sign = sign + 1
            word = ''.join(word_temp)
            print("\t" + str(row + 1) + ":NUM value=: " + word + "  Type:Float")
            return 2
        else:  # 整形
            word = ''.join(word_temp)
            print("\t" + str(row + 1) + ":NUM value=: " + word + "  Type:Int")
            return 2

    elif sentence[sign] in SpecialSymbol:  # 3
        for i in range(len(SpecialSymbol)):  # 判断符号
            if sentence[sign] == SpecialSymbol[i]:
                word_temp += sentence[sign]
                sign = sign + 1
                if (word_temp == ("<" or ">")) and (sentence[sign] == "="):
                    word_temp += sentence[sign]
                    sign = sign + 1
                    word = "".join(word_temp)
                    print("\t" + str(row + 1) + ":" + word)
                    return 3
                elif word_temp != ("<" or ">"):
                    word = "".join(word_temp)
                    print("\t" + str(row + 1) + ":" + word)
                    return 3

    elif sentence[sign] == "{":  # 注释
        while True:
            if sentence[sign] != "}":
                if (sentence[sign] == "\n"):
                    print("\t" + str(row + 1) + ":错误!!!!!注释括号缺失!")
                    return 5
                sign = sign + 1;
            else:  # 注释括号完整
                sign = sign + 1
                return 4
    elif sentence[sign] == "\n":
        return 0;
    else:
        print("\t" + str(row + 1) + ":错误!!!!!")
        return 0;


def main():
    SourceProgram = []
    Filepath = input("请输入文件路径：")
    for line in open(Filepath, 'r'):
        SourceProgram.append(line)
    for i in range(len(SourceProgram)):
        print(str(i + 1) + ":" + SourceProgram[i], end="")
        one = SourceProgram[i]
        global sign
        sign = 0  # sign循环前归0
        a = True
        while a:
            m = GetToken(one, i)
            if m == 0:
                a = False


if __name__ == "__main__":
    main()
