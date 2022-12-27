def factorial(n):
    if n<1:
        return 1
    else:
        e=n*factorial(n-1)
        return e

r=factorial(4)
def fibonacci(n):
    assert n>=0 and int(n)==n,'fibonacci no cant be negative or non integer'
    try:
        if n in [0,1]:
            return n

        else:
            return fibonacci(n-1)+fibonacci(n-2)
    except Exception as e:
        print(e)


print(fibonacci(5))
print(40%6)

def sum_digit(n):
    assert n>=0 and type(n)==int,"only integer"
    if n==0:
        return 0

    else:

        return int(n%10) + sum_digit(int(n/10))


print(sum_digit(11.2))

def power(base,exp):
    assert exp>=0 and int(exp)==exp
    if exp==0:
        return 1
    if exp==1:
        return base
    return base*power(base,exp-1)

print(power(2,-4))
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

print(gcd(48,64))


def decimaltobinary(n):
    if n==0:
        return 0

    else:
        return n%2+10*decimaltobinary(int(n/2))
print(decimaltobinary(10))

def reverse(string):
    if len(string)<=1:
        return string

    return string[len(string)-1] + reverse(string[0:len(string)-1])

print(reverse("python"))

def recursiveRange(num):
    if num <=0:
        return 0

    return num + recursiveRange(num-1)


print(recursiveRange(6))


def productofarray(arr):
    if len(arr)==0:
        return 1


    return arr[0]*productofarray(arr[1:])


print(productofarray([1,2,3]))


def power(base,exponent):
    if exponent==0:
        return 1


    return base*power(base,exponent-1)

print(power(2,0))

def ispallindrome(strng):
    if len(strng)==0:
        return True

    if strng[0] != strng[len(strng)-1]:
        return False


    return ispallindrome(strng[1:-1])


print(ispallindrome('tacocat'))


def capitalizefirst(arr):
    result=[]
    if len(arr)==0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result+capitalizefirst(arr[1:])

print(capitalizefirst(['car', 'taco', 'banana']))

def capitalizewords(arr):
    result =[]
    if len(arr)==0:
        return result

    result.append(arr[0].upper())
    return result + capitalizewords(arr[1:])

words = ['i', 'am', 'learning', 'recursion']

print(capitalizewords(words))


def stringifyNumbers(obj):
    newobj=obj
    for key in newobj:
        if type(newobj[key]) is int :
            newobj[key]=str(newobj[key])
        if type(newobj[key]) is dict:
            newobj[key]=str(newobj[key])

    return newobj

obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}

print(stringifyNumbers(obj))
