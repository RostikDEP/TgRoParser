import sys
from modules.IdDetector import IdDetector
args = sys.argv[1:]
try:
    if "--help" in args:
        help_text = ("--help - Get information\n[DETECTION MODE]\n--join - detect id when you join to group\n--message "
                     "- detect when you send detection word in group\n")
        raise Exception(help_text)
    if len(args) == 0:
        raise Exception("Syntax error. Try id-detector --help to get information")
    if ("--join" in args) + ("--message" in args) != 1:
        raise Exception("Please, chose mode of detection (--join or --message)")
    if "--join" in args:
        pass  #Chat name will be checked soon
    elif "--message" in args:
        if "--word" not in args:
            raise Exception("Please, enter detection word (--word TEST_WORD)")
        word = args[args.index("--word") + 1]
        if "--" in word:
            raise Exception("Arguments error")
        print(f"WORD: {word}")
        detector = IdDetector()
        detector.DetectMessage(word)


except IndexError:
    print("Arguments syntax error")
except Exception as e:
    print(e)

