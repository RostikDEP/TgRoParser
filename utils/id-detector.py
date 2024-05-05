import sys

args = sys.argv[1:]
try:
    if "--help" in args:
        help_text = ("--help - Get information\n[DETECTION MODE]\n--join - detect id when you join to group\n--message "
                     "- detect when you send detection word in group\n--id CHAT_ID - enter chat of group")
        raise Exception(help_text)
    if len(args) == 0:
        raise Exception("Syntax error. Try id-detector --help to get information")
    if ("--join" in args) + ("--message" in args) != 1:
        raise Exception("Please, chose mode of detection (--join or --message)")
    if "--id" not in args:
        raise Exception("Please enter id (--id 12345)")
    if "--join" in args:
        pass  #Chat name will be checked soon
    elif "--message" in args:
        if "--word" not in args:
            raise Exception("Please, enter detection word (--word TEST_WORD)")
        id = args[args.index("--id") + 1]
        word = args[args.index("--word") + 1]
        if ("--" in id) + ("--" in word):
            raise Exception("Arguments error")

        print(f"ID: {id}\nWORD: {word}")
except IndexError:
    print("Arguments syntax error")
except Exception as e:
    print(e)

