
#2

# Weekly expenses for different categories
def category_expenses(category):
    licznik = 0
    category_total_expenses = 0
    while licznik < 4:
        category_total_expenses += monthly_expenses[licznik][category]
        licznik +=1
    return category_total_expenses
def weekly_expenses(week):
    licznik = 0
    weekly_total_expenses = 0
    while licznik < 3:
        weekly_total_expenses += monthly_expenses[week][licznik]
        licznik +=1
    return weekly_total_expenses

categories = ['Food', 'Transport', 'Utilities']
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]
food_expenses = 0

total_expenses = 0
# Calculates expenses
# Use loop statements
for weeks in monthly_expenses:
    for costs in weeks:
        total_expenses += costs


print(food_expenses)
# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', category_expenses(0))
print('Transport:', category_expenses(1))
print('Utilities:', category_expenses(2))
print('Week 1:', weekly_expenses(0))
print('Week 2:', weekly_expenses(1))
print('Week 3:', weekly_expenses(2))
print('Week 4:', weekly_expenses(3))
print('---------------')
print('TOTAL:', total_expenses)

#3

# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
]

# Returns a week day name
def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n-1]

# Returns a string with day meal names
# separated by comma
def day_meal_plan(day_number):
    return ', '.join(meal_plan[day_number])

# Prints weekly meal plan
day = 1
while day <= 7:
   print(f'{weekday(day)}: {day_meal_plan(day - 1)}')
   day += 1