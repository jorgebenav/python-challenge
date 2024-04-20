import os
import csv
budgetpath = os.path.join('..', 'Resources', 'module_budget_data.csv')

output_path = r'C:\Users\AndBe\Desktop\ASU Data\Homework\Starter_Code\PyBank\ModuleThree\financial_analysis_results.txt'

with open(budgetpath) as budgetcsv:
    budgetread = csv.reader(budgetcsv, delimiter=',')
    next(budgetread, None)  # Skip the header

    month_count = 0
    total_sum = 0
    changes = []
    p_row = next(budgetread)
    month_count += 1
    p_amount = float(p_row[1])
    total_sum += p_amount

    increase = {'amount': -float('inf'), 'month': ''}
    decrease = {'amount': float('inf'), 'month': ''}

    for row in budgetread:
        current_month = row[0]
        c_amount = float(row[1])
        month_count += 1
        total_sum += c_amount

        change = c_amount - p_amount
        changes.append(change)

        if change > increase['amount']:
            increase = {'amount': change, 'month': current_month}
        if change < decrease['amount']:
            decrease = {'amount': change, 'month': current_month}
        p_amount = c_amount

average_change = sum(changes) / len(changes) if changes else 0

with open(output_path, 'w') as file:
    output_lines = [
        f"Total number of months: {month_count}\n",
        f"Sum: {total_sum}\n",
        f"Average Change: {average_change:.2f}\n",
        f"Greatest Increase in Profits: {increase['month']} (${increase['amount']:.2f})\n",
        f"Greatest Decrease in Profits: {decrease['month']} (${decrease['amount']:.2f})\n"
    ]

    for line in output_lines:
        print(line, end='')
        file.write(line)

print(f"Results have been written to {output_path}")
