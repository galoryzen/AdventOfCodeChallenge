import json

def find_pair(sum, numbers, qty):

    if qty == 2:
        for num in numbers:
            n = sum - num
            if n in numbers:
                return [num,n]
        return[]
    else:
        for num in numbers:
            new_sum = sum - num
            numbers_list = numbers.copy()
            numbers_list.remove(num)
            answer = find_pair(new_sum, numbers_list, qty-1)
            if any(answer):
                answer.append(num)
                return answer
            else:
                continue
        return[]
            
def main():
    input_file_path = './numbers.JSON'
    with open(input_file_path) as input_file:
        numbers = json.load(input_file)
        l = find_pair(2020, numbers, 3)
        c = 1
        for i in l:
            c = c*i
        print(c)
        print(find_pair(2020, numbers, 3))

main()
