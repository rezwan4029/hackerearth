#builds the integer number as a list by splittig its digits
def get_number(num):
    return [int(x) for x in num]

def get_reverse_sum(a,b):
    la = len(a)
    lb = len(b)

    if la > lb:
        b[lb : la] =[0] * (la - lb)
    elif lb > la:
        a[la : lb] =[0] * (lb - la)

    ans = []
    carry = 0

    while a and b :
        cur = a.pop(0) + b.pop(0) + carry
        carry = cur / 10
        cur = cur % 10
        ans.append(cur)

    if carry:
        ans.append(carry)
        
    while ans:
        cur = ans.pop(0)
        if cur != 0:
            ans.insert(0,cur)
            break
        
    final_answer = ''.join([str(x) for x in ans])
    return final_answer
        
testcases = int(input())

for testcase in range(testcases):
    first_number , second_number = [str(x) for x in raw_input().split()]
    first_number = get_number(first_number)
    second_number = get_number(second_number)
    ans = get_reverse_sum(first_number , second_number)
    print(ans)
