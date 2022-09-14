houses = ["Nadech's House", "Yaya's House", "Aj.Nest's House", "Mario's House"]
def deliver_product_recursively(houses):
    #Worker doing his work --> Base Case == 1
    if len(houses) == 1:
        house = houses[0]
        print("Delivering products to", house)
    #Manager doing his work --> Recursive Case
    else:
        mid = len(houses) // 2
        first_half = houses[:mid] # "[:mid]" คือตำแหน่ง "แรก" ไปจนถึงตำแหน่งที่ "mid"
        second_half = houses[mid:]  # [mid:]" คือตำแหน่งที่ "mid" ไปจนถึงตำแหน่ง "สุดท้าย"
        #Divides his work among two workers
        deliver_product_recursively(first_half)
        deliver_product_recursively(second_half)
#Call Recursive Functions
deliver_product_recursively(houses)
