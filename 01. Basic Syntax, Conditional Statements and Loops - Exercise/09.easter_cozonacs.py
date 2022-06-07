budget = float(input())
one_kg_floor = float(input())

current_cozonacs_count = 0
colored_eggs = 0
pack_eggs = 0.75 * one_kg_floor
one_liter_milk = (0.25 * one_kg_floor) + one_kg_floor
milk_per_cozonac = one_liter_milk / 4

cozonac_price = pack_eggs + one_kg_floor + milk_per_cozonac

while budget >= cozonac_price:
    budget -= cozonac_price
    current_cozonacs_count += 1
    colored_eggs += 3
    if current_cozonacs_count % 3 == 0:
        colored_eggs -= (current_cozonacs_count - 2)

print(f'You made {current_cozonacs_count} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')