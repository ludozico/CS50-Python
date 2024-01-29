def main():
      # gets user input
      fruit = input('What fruit? ')
      # ignores captalization
      fruit = fruit.lower()
      # define the dictionary
      fruit_dic = {'apple':130, 'avocado':50, 'banana':110, 'cantaloupe':50,
             'grapefruit':60, 'grapes':90, 'honeydew melon':50, 'kiwifruit':90,
             'lemon':15, 'lime':20, 'nectarine':60,'orange':80, 'peach':60, 'pear':100,
             'pineapple':50, 'plums':70, 'strawberries':50, 'sweet cherries':100,
             'tangerine':50, 'watermelon':80}
      # verifies if it should ignore or reply
      if fruit in ['apple', 'avocado', 'banana', 'cantaloupe',
             'grapefruit', 'grapes', 'honeydew melon', 'kiwifruit',
             'lemon', 'lime', 'nectarine','orange', 'peach', 'pear',
             'pineapple', 'plums', 'strawberries', 'sweet cherries',
             'tangerine', 'watermelon']:
             #reply
             print(fruit, fruit_dic[fruit])

      else:
             #ignore
             None


main()



