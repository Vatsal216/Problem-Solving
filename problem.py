'''For a string sand an Integer k, a selection of substrings is valid if the following conditions are met:
 
 • The length of every substring is greater than or equal to k 
 • Each substring is a palindrome.
 • No two substrings overlap.
 
Determine the maximum number of valld substrings that can be formed from string

Notes:

A substring is a group of adjacent characters in a string. 
A palindrome is a string that reads the same backward as forward.

Example
a="aababaabce"
k=3

a ababa abce
a aba baab ce


Example

s = "ababaeocco"
k=4

output = 2

explanation

ababa e occo

'''





lst=[]
string=''
def substring(k,s,count,string):
    if count<len(s):
        sub=s[count]
        string=string+sub
        #palidrome check
        if len(string)>=k:
            if string==string[::-1]:
                lst.append(string)
                s=s[len(string):]
                count=0
                string=''
            else:
                count+=1
        else: count+=1
        # print(lst,s)
    elif len(s)==0:
        return lst
    else:
        s=s[1:]
        count=0
        string=''
    
    return substring(k,s,count,string)
        
s='aabbcc'
re=substring(4,s,0,string)
print(re, len(re))






