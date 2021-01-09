### Observations and Finding The Regularity

这学期几次作业和考试的时候遇到了一些题目，解决他们不需要特别的算法，而是需要通过观察，找到相应的规律，最终完成解题。

先看一下这道题，Count String Permutations：

![image-20210109222228363](C:\Users\Zhiwei Hu\AppData\Roaming\Typora\typora-user-images\image-20210109222228363.png)

简单来说，这道题会给定一个限定的字符串长度，要求我们用 {a, e, i, o u} 五个字符串任意组合出给定长度的字符串，但是要求：

* a 后面只能是 e
* e 后面可以是 a 或者是 i
* i 不可以和 i 放在一起
* o 后面只能是 i 或者 u
* u 后面只能是 a

**以下是对应的两个例子：**

![image-20210109222304715](C:\Users\Zhiwei Hu\AppData\Roaming\Typora\typora-user-images\image-20210109222304715.png)

![image-20210109222325707](C:\Users\Zhiwei Hu\AppData\Roaming\Typora\typora-user-images\image-20210109222325707.png)

![image-20210109222343278](C:\Users\Zhiwei Hu\AppData\Roaming\Typora\typora-user-images\image-20210109222343278.png)

这道题解题可以从右往左看，我们把所有可能的String分成五类，即分别以{a, e, i, o, u}结尾不同字符串。根据题目要求:

* 以 a 结尾的字符串，前面可以是一个以 u 结尾的字符串，或者是以 i 结尾的字符串，或者是以 e 结尾的字符串
* 以 e 结尾的字符串，前面可以是一个以 a 结尾的字符串，或者是一个以 i 结尾的字符串
* 以 i 结尾的字符串，前面可以是一个以 e 结尾的字符串，或者是一个以 o 结尾的字符串
* 以 o 结尾的字符串，前面只能是一个以 i 结尾的字符串
* 以 u 结尾的字符串，前面可以是一个以 i 结尾的字符串，或者是一个以 o 结尾的字符串

以此，我们可以根据限定字符串的长度，从右到左依照这样的规律累加字母，从而完成完整长度的String

```python
def countPerms(n):
    
    strings = dict()  # the dictionary is for book keeping
    vowels = ['a', 'e', 'i', 'o', 'u']

    MOD = 10 ** 9 + 7
    for vowel in vowels:
        strings[vowel] = 1  
        # initial substrings ['a','e','i','o','u']

    # build the string reversely, from the right to the left
    for i in range(n - 1):  # each time we add one more letter to the left
        a = strings['e'] + strings['i'] + strings['u']  
        # only ..e, ..i, ..u could be put before a
        e = strings['a'] + strings['i']  # only ..a and ..i could be put before e
        i = strings['e'] + strings['o']  # only ..e and ..o could be put before i
        o = strings['i']  # only ..i could be put before o
        u = strings['o'] + strings['i']  # only ..o and ..i could be put before u

        # now to update the values
        strings['a'] = a
        strings['e'] = e
        strings['i'] = i
        strings['o'] = o
        strings['u'] = u

    count = 0
    for values in strings.values():
        count += values # count the total number of the strings
    return count % MOD

print(countPerms(26)) #Output: 56664154
print(countPerms(764)) #Output: 888683244
```

之后还有另一道有意思的题目，叫做 Growth in 2 Dimensions。这道题会给定几个坐标，从原点开始依次按照给定的坐标为边界，对范围内的所有方格值+1，最后求拥有最大值方格的个数。

![image-20210109235835319](C:\Users\Zhiwei Hu\AppData\Roaming\Typora\typora-user-images\image-20210109235835319.png)

![image-20210109235905688](C:\Users\Zhiwei Hu\AppData\Roaming\Typora\typora-user-images\image-20210109235905688.png)

![image-20210109235925241](C:\Users\Zhiwei Hu\AppData\Roaming\Typora\typora-user-images\image-20210109235925241.png)

这道题乍看起来确实挺难的，如果严格按照题目的过程，创建二维数组之后按照给定坐标去遍历，最后返回包含最大值的方格的个数，确实最后会很麻烦。但是如果注意观察，我们每次执行growth这个步骤的时候，都是以原点出发向外延伸，也就是说最终的最大值，一定是历经了每一次的growth。那么我们只需要找出历经所有次growth的方块数量（横向growth的最小方块个数 * 纵向growth的最小方块个数），对应的也就是含有最大值的方块的数量了。对应的代码如下：

```python
def countMax(upRight):
    rows = [0] * len(upRight)
    columns = [0] * len(upRight)
    # rows / columns multiplied by the number of operations
    
    for operation in range(len(upRight)):
        ops = upRight[operation].split(" ")
        rows[operation] = int(ops[0]) # the span of every vertical growth
        columns[operation] = int(ops[1]) # the span of every horizontal growth
    
    return(min(rows) * min(columns)) 
	# the area that has gone through every growth
    # which is exactly the minimum area that was covered in every growth
    # equals to min(rows) * min(columns)
    
    '''
    Test Cases
    upRight_1 = ['18 29', '32 17', '34 9', '38 15', '36 22', '7 14', '5 100']
    Output = 45
    
    upRight_2 = ['2 3', '3 7', '4 1']
    Output = 2
    
    upright_3 = ['1 1', '1 1', '1 1', '1 1', '1 1']
    Output = 1
    '''
```

