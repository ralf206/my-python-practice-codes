def inventory_level (count)
"""Prints the inventory level for items that are low."""
  for item, quantity in count:
    if quantity < 9:
      print (f"Inventory level for {item} is low")

count = [
  ("Jeans", 7),
  ("Blouse", 97),
  ("Purses", 68),
  ("Men's shoes", 34),
  ("Women's shoes", 4),
]

inventory_level (count)
