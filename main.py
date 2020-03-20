import argparse

def mapping(s1,s2):
    if len(set(s1)) < len(s1):
        print("false")
        return

    s1 = set(s1)
    s2 = set(s2)
    # print(s1,s2)
    if len(s1)<len(s2):
        print("false")
    else :
        print("true")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('value',nargs='+',help='an integer for the accumulator')

    args = parser.parse_args()
    mapping(args.value[0],args.value[1])

