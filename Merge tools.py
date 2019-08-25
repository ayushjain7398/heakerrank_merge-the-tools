'''Consider the following:

A string, , of length  where .
An integer, , where  is a factor of .
We can split  into  subsegments where each subsegment, , consists of a contiguous block of  characters in . Then, use each  to create string  such that:

The characters in  are a subsequence of the characters in .
Any repeat occurrence of a character is removed from the string such that each character in  occurs exactly once. In other words, if the character at some index  in  occurs at a previous index  in , then do not include the character in string .
Given  and , print  lines where each line  denotes string .

Input Format

The first line contains a single string denoting . 
The second line contains an integer, , denoting the length of each subsegment.
'''





def rmvDuplicates(stri):
    string = ''
    #len_str = len(stri)
    for ch in stri:
        if ch in string:
            continue
        else:
            string += ch
    return string
def merge_the_tools(string, k):
    str_len = len(string)
    for i in range(0,str_len,k):
        result_str = string[i:i+k]
        result_str = rmvDuplicates(result_str)
        print(result_str)

    return 0
'''L1=[]
    a=0
    d=len(s)//k
    l=list(s)
    for _ in range(k):
        L1.append(l[a:d])
        a=d
        d=d+d'''
    
    
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
