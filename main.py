import argparse

def mapping(s1,s2):
    if len(set(s1)) < len(s1):
        print("false")
        return

    s1 = set(s1) #the strings are converted into a set to remove duplicates
    s2 = set(s2)
    # print(s1,s2)
    if len(s1)<len(s2): # comparing the length of sets
        print("false")
    else :
        print("true")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Passed values taken as input')
    parser.add_argument('value',nargs='+')

    args = parser.parse_args()
    mapping(args.value[0],args.value[1])

