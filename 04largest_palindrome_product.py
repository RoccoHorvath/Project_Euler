def largest_palindrome():
    x = 999
    y = 999
    # while True:
    #     product = x * y
    #     prod_compare = product
    #     rev = 0
    #     if product % 10 != 0:
    #         while product:
    #             rev = rev * 10 + product % 10
    #             product //= 10
    #             print(rev,product,prod_compare)
    #         if rev == prod_compare:
    #             return prod_compare
        
    #     if (x-1) * y
        
    #     if x >= y:
            
    #         x -= 1
    #     else:
    #         y -= 1

    product = 998001
    prod_compare = product
    while True:
        rev = 0
        product = prod_compare
        if product % 10 != 0:
            while product:
                rev = rev * 10 + product % 10
                product //= 10
            if rev == prod_compare:
                x = 999
                while prod_compare / x <= 999:
                    if prod_compare % x == 0:
                        return prod_compare
                    x -= 1
        prod_compare -= 1        
print(largest_palindrome())