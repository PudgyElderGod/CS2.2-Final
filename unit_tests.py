from main import prims_algorithm, pick_smallest_key

def test_prims():
  example_graph = {
    "Zero": [("One", 4), ("Seven", 8)], 
    "One": [("Seven", 11), ("Two", 8)],
    "Two": [("Three", 7), ("Eight", 2), ("Five", 4)],
    "Three": [("Two", 7), ("Five", 14), ("Four", 9)],
    "Four": [("Three", 9), ("Five", 10)],
    "Five": [("Two", 4), ("Three", 14), ("Four", 10)],
    "Six": [("Five", 2), ("Seven", 1), ("Eight", 6)],
    "Seven": [("Zero", 8), ("One", 11), ("Six", 1), ("Eight", 7)],
    "Eight": [("Two", 2), ("Six", 6), ("Seven", 7)]
    }
  result = prims_algorithm(example_graph, 'Zero')
  
  assert result == {'Zero': [('One', 4), ('Seven', 8)], 'One': [('Zero', 4)], 'Two': [('Five', 4), ('Eight', 2), ('Three', 7)], 'Three': [('Two', 7), ('Four', 9)], 'Four': [('Three', 9)], 'Five': [('Six', 2), ('Two', 4)], 'Six': [('Seven', 1), ('Five', 2)], 'Seven': [('Zero', 8), ('Six', 1)], 'Eight': [('Two', 2)]}

def test_pick_smallest():
  example_key_values = {'Zero': (0, 'Zero'), 'One': (4, 'Zero'), 'Two': (8, 'One'), 'Three': (-1, None), 'Four': (-1, None), 'Five': (-1, None), 'Six': (-1, None), 'Seven': (8, 'Zero'), 'Eight': (-1, None)}
  example_mst_set = ['Zero', 'One']
  result = pick_smallest_key(example_key_values, example_mst_set)
  assert result == 'Seven'

  example_key_values = {'Zero': (0, 'Zero'), 'One': (-1, None), 'Two': (-1, None), 'Three': (-1, None), 'Four': (-1, None), 'Five': (-1, None), 'Six': (-1, None), 'Seven': (-1, None), 'Eight': (-1, None)}
  example_mst_set = []
  result = pick_smallest_key(example_key_values, example_mst_set)
  assert result == 'Zero'