def productExceptSelf(nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n
        current_product = 1
        for i in range(n):
            answer[i] = current_product
            current_product *= nums[i]
        current_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= current_product
           
            current_product *= nums[i]
            print(answer)
        return answer
test =[2,3,4,5]
list1 = productExceptSelf(test)
print(list1)
