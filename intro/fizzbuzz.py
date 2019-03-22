import sys

def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        fizz = i % 3 == 0
        buzz = i % 5 == 0
        if fizz and buzz:
            result.append('FizzBuzz')
        elif fizz:
            result.append('Fizz')
        elif buzz:
            result.append('Buzz')
        else:
            result.append(str(i))

    return result


if __name__ == '__main__':

    if len(sys.argv) < 3:
        print('Missing arguments, need 2')
    else:

        n = int(sys.argv[1])
        filename = sys.argv[2]
        result = fizzbuzz(n)
        formatted_result = '\n'.join(result)

        print(formatted_result)

        with open(filename, 'w') as file:
        
            file.write(formatted_result)




    