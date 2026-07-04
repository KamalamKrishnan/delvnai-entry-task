import csv

category_totals = {}

try:
    with open("transactions.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                category = row["category"]
                amount = float(row["amount"])

                if category in category_totals:
                    category_totals[category] += amount
                else:
                    category_totals[category] = amount

            except (ValueError, KeyError):
                print("Skipping invalid row:", row)

except FileNotFoundError:
    print("transactions.csv not found.")
    exit()

print("\nTotal Amount per Category (Highest to Lowest):")

sorted_totals = sorted(
    category_totals.items(),
    key=lambda item: item[1],
    reverse=True
)

for category, total in sorted_totals:
    print(f"{category}: {total}")
