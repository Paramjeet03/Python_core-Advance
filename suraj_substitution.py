def substitution(giv_str,remve,replace):
    string=''
    for i in giv_str:
        if i not in remve:
            string+=i
        else:
            string+=replace
    print(string)