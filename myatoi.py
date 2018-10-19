def myAtoi(str):

        str_list = str.split()
        if len(str_list) < 1:
            return 0
        str_list = [x.encode('UTF8') for x in str_list]
        str = str_list[0]

        neg = False
        if str[0] == '-':
            neg = True
            str = str[1:]
        else:
            if str[0] == '+':
                str = str[1:]

        number = 0
        for c in str:
            if c >= '0' and c <= '9':
                number = 10 * number + ord(c) - ord('0')
            else:
                break
        if neg:
            number = number * -1
        number = (number if number <= 2147483647 else 2147483647)
        number = (number if number >= -2147483648 else -2147483648)
        return number

if __name__ == "__main__":
    print(myAtoi("1234"))
