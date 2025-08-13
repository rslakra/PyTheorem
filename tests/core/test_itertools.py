#
# Author: Rohtash Lakra
#
import csv
import time
from itertools import *

# Combinatoric iterators
# These functions are used to create sequences that represent combinations, permutations, and Cartesian products.


# 1. itertools.product(iterables, repeat=1)
# Generates the Cartesian product of input iterables.

# Business Use Case: Product Configuration and Bundling in E-commerce.
# An online retailer offering customizable products (e.g., shoes with different colors, sizes, and materials) can use itertools.product() to generate all possible combinations of options to present to customers or to analyze popular configurations.

# Benefits:
# Efficiency: Generates combinations on demand, saving memory compared to creating a large list of all possible configurations, especially when dealing with many options or variants.
# Comprehensive Listing: Ensures all possible product configurations are considered without manual listing, reducing errors and saving time.

# Example 1: Cartesian product of two lists
print("Example 1: Cartesian product of two lists")
colors = ['red', 'green', 'blue']
sizes = ['S', 'M', 'L']

for combo in product(colors, sizes):
    print(combo)

print()
products = list(product(colors, sizes))
print(products)

print()
print("Example 2: Cartesian product with repetition")
# Example 2: Cartesian product with repetition
numbers = [1, 2]
for combo in product(numbers, repeat=3):
    print(combo)

# Define product options
colors = ['Red', 'Blue', 'Green']
sizes = ['S', 'M', 'L']
materials = ['Cotton', 'Polyester']

# Generate all possible product configurations
product_configurations = list(product(colors, sizes, materials))

# Print a few examples
for i, config in enumerate(product_configurations[:5]):
    print(f"Configuration {i + 1}: Color={config[0]}, Size={config[1]}, Material={config[2]}")

# Benefits:
# - Creates a comprehensive list of configurations for sales and inventory planning.
# - Helps identify popular combinations or gaps in product offerings.
# - Efficiently generates all possibilities without manually creating nested loops.

# ----------------------------------------------------------------------

print()
# 2. itertools.permutations(iterable, r=None)
# Generates all possible orderings of elements from an iterable, without repeating elements.

# Business Use Case: Route Optimization in Logistics or Delivery Services.
# A delivery company can use itertools.permutations() to find the most efficient route for a delivery driver with multiple stops, considering all possible sequences of stops.

# Benefits:
# Optimized Resource Allocation: Identifies the best route, potentially reducing fuel consumption, travel time, and operational costs.
# Improved Efficiency: Streamlines delivery operations by quickly calculating and comparing different routes.


print("Example with no specific length (r)")
input_list = [1, 2, 3]
results = list(permutations(input_list))
print(results)

print("Example with a specific length (r)")
results = list(permutations(input_list, r=2))
print(results)

# Delivery stops (e.g., coordinates or customer IDs)
stops = ['Warehouse', 'Customer A', 'Customer B', 'Customer C']

# Find all possible routes
all_routes = list(permutations(stops))

# Print the possible routes
for i, route in enumerate(all_routes):
    print(f"Route {i + 1}: {route}")

# To find the optimal route, one would typically calculate the distance or time for each route
# and then select the shortest.

# Benefits:
# - Enables calculation of the most efficient delivery routes to minimize fuel costs and delivery times.
# - Facilitates dynamic routing adjustments based on traffic or sudden changes.

# ----------------------------------------------------------------------
print()
# 3. itertools.combinations(iterable, r)
# Generates all possible combinations of a specified length from an iterable, without repetition.

# Business Use Case: Team Formation and Project Assignment in Project Management.
# When forming project teams, a manager can use itertools.combinations() to explore different combinations of team members from a pool of employees, ensuring diverse skill sets or experiences are included in each team.
#
# Benefits:
# Data-Driven Decisions: Facilitates informed team-building by systematically examining all possible combinations and identifying those that meet project requirements.
# Fairness and Inclusivity: Ensures all eligible employees are considered for teams, preventing unconscious bias and promoting balanced team structures.


players = ["John", "Daisy", "Marry", "Bob"]
for pair in combinations(players, 2):
    print(pair)

# List of employees with different skills
employees = ['Alice (Python)', 'Bob (SQL)', 'Charlie (Design)', 'David (Marketing)', 'Eve (Project Mgmt)']

# Form project teams of 3 members
team_size = 3
possible_teams = list(combinations(employees, team_size))

# Print the possible teams
for i, team in enumerate(possible_teams):
    print(f"Team {i + 1}: {', '.join(team)}")

# Benefits:
# - Allows for fair and diverse team creation based on desired criteria (e.g., skillset, experience).
# - Supports identifying the optimal team structure for project success.


# ----------------------------------------------------------------------
print()
# 4. itertools.combinations_with_replacement(iterable, r)
# Generates combinations with repetition allowed.

# Business Use Case: Portfolio Diversification and Risk Assessment in Financial Analysis.
# Financial analysts use itertools.combinations_with_replacement() to assess portfolio risk by simulating scenarios with various asset allocations, including repeated asset selections.
#
# Benefits:
# Comprehensive Risk Analysis: Evaluates the potential impact of different asset mixes, providing insights into potential losses and optimal diversification strategies.
# Strategic Decision Support: Assists in making data-driven investment decisions to mitigate risks and maximize returns.


numbers = [1, 2, 3]
for combo in combinations_with_replacement(numbers, 2):
    print(combo)

# Available asset types
assets = ['Stocks', 'Bonds', 'Real Estate']

# Create portfolios with 2 assets, allowing for repeated selections
portfolio_size = 2
portfolios = list(combinations_with_replacement(assets, portfolio_size))

# Print the possible portfolios
for i, portfolio in enumerate(portfolios):
    print(f"Portfolio {i + 1}: {', '.join(portfolio)}")

# Benefits:
# - Enables thorough risk assessment and analysis by exploring diverse asset combinations, {Link: Stack Overflow https://stackoverflow.com/questions/21224641/while-generating-all-possible-combinations-itertools-combinations-with-replaceme}.
# - Provides insights into potential losses and optimal diversification strategies, {Link: Stack Overflow https://stackoverflow.com/questions/21224641/while-generating-all-possible-combinations-itertools-combinations-with-replaceme}.

# ----------------------------------------------------------------------
print()
# Infinite iterators
# These functions generate sequences that technically never end.

# 1. itertools.count(start=0, step=1)
# Generates an infinite sequence of evenly spaced numbers.


# Business Use Case: Unique Identifier Generation in Database Systems.
# Generating consecutive order IDs or invoice numbers in a database system.
#
# Benefits:
# Scalability: Generates unique IDs on demand, avoiding the overhead of pre-generating large sequences and ensuring availability as needed.
# Data Consistency: Guarantees unique identifiers, preventing conflicts and maintaining data integrity within the system.

# Count from 10, incrementing by 1
counter = count(10)
for _ in range(5):  # Limit to 5 iterations for demonstration
    print(next(counter))

# Start generating unique IDs from a specific number
order_id_generator = count(start=1001)

# Simulate generating a few order IDs
for _ in range(5):
    order_id = next(order_id_generator)
    print(f"New Order ID: {order_id}")

# Benefits:
# - Efficiently generates unique identifiers without the need for complex database queries for each new ID.
# - Ensures data consistency by preventing duplicate IDs.


# ----------------------------------------------------------------------
print()
# 2. itertools.cycle(iterable)
# Repeats the elements of an iterable indefinitely.
# For an example, see python.plainenglish.io.

# Business Use Case: Rotating Advertisements or Promotions on a Website.
# Cycling through different advertisements or promotional banners on a website or application.
#
# Benefits:
# Dynamic Content Delivery: Presents diverse content to users, potentially increasing engagement and effectiveness of advertisements.
# Resource Efficiency: avoids repetitive ad-fetching by cycling through preloaded content, improving website performance.

# List of advertisements to display
advertisements = ['Ad 1: Product A', 'Ad 2: Service B', 'Ad 3: Discount C']

# Create an infinite cycle of advertisements
ad_cycler = cycle(advertisements)

# Simulate displaying ads on a website for a few cycles
for i in range(7):  # Display 7 ads
    current_ad = next(ad_cycler)
    print(f"Displaying: {current_ad}")
    time.sleep(1)  # Simulate a delay

# Benefits:
# - Dynamically presents diverse content to users, increasing engagement.
# - Enhances the effectiveness of advertising by cycling through different messages.

# ----------------------------------------------------------------------
print()
# 3. itertools.repeat(object, times=None)
# Repeats an object a specified number of times, or indefinitely.

# Business Use Case: Data Placeholder Generation in Data Analysis and Reporting.
# Filling in missing data points in a dataset with a placeholder value or extending a dataset for a fixed number of rows with a constant value.
#
# Benefits:
# Data Preparation Efficiency: Quickly fills gaps in data or generates placeholder rows, simplifying data preparation tasks.
# Analysis and Reporting: Allows for consistent handling of missing data or projections for future periods.


# Repeat a string 5 times
repeater = repeat("hello", 5)
for word in repeater:
    print(word)

# Existing sales data
sales_data = [12000, 15000, 13500]

# Projecting sales for the next 3 months, assuming a constant value
projected_sales_value = 14000
projected_months = 3

projected_sales = list(repeat(projected_sales_value, projected_months))

# Combine actual and projected sales
total_sales_analysis = sales_data + projected_sales
print(f"Total Sales Analysis (actual + projected): {total_sales_analysis}")

# Benefits:
# - Quickly fills in missing data points or extends datasets with constant values for analysis or projections.
# - Simplifies data preparation tasks and enables consistent handling of missing data.


# ----------------------------------------------------------------------
# Iterators terminating on the shortest input sequence
# These functions stop when the shortest input iterable is exhausted.


# 1. itertools.chain(*iterables)
# Chains multiple iterables together.

# Business Use Case: Consolidating Data from Multiple Sources in Data Processing.
# Chaining together multiple lists or data streams (e.g., from different sales regions or product lines) to process them as a single data source.
#
# Benefits:
# Streamlined Data Processing: Simplifies the handling of data from diverse sources, reducing the need for complex merge or concatenation operations.
# Memory Efficiency: Avoids creating large temporary lists in memory by processing data sequentially, which is especially useful with large datasets.


list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

for number in chain(list1, list2, list3):
    print(number)

# Sales data from different regions
region_a_sales = [100, 120, 110]
region_b_sales = [80, 95, 105]
region_c_sales = [130, 115, 140]

# Consolidate sales data for overall analysis
all_sales = list(chain(region_a_sales, region_b_sales, region_c_sales))
print(f"Consolidated Sales Data: {all_sales}")

# Benefits:
# - Streamlines data processing by combining multiple iterables into a single sequence,.
# - Efficiently handles large datasets by avoiding the creation of large intermediate lists,.

# ----------------------------------------------------------------------
# 2. itertools.chain.from_iterable(iterable)
# Alternative constructor for chain() that takes a single iterable of iterables.
list_of_lists = [['a', 'b'], ['c', 'd']]
for char in chain.from_iterable(list_of_lists):
    print(char)

# ----------------------------------------------------------------------
# 3. itertools.compress(data, selectors)
# Filters elements from data based on corresponding Boolean values in selectors.

# Business Use Case: Targeted Marketing or Customer Segmentation.
# Filtering a customer list based on marketing campaign flags (e.g., sending promotional emails only to customers opted-in for a specific category).
#
# Benefits:
# Personalized Marketing: Focuses marketing efforts on relevant customer segments, potentially improving campaign effectiveness.
# Resource Optimization: Avoids processing or sending unnecessary communications, saving time and resources.


data = [1, 2, 3, 4, 5]
selectors = [1, 0, 1, 0, 1]  # 1 means include, 0 means exclude
filtered = compress(data, selectors)
for item in filtered:
    print(item)

# Customer data (names)
customer_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

# Marketing campaign flags (True for opted-in, False for opted-out)
campaign_flags = [True, False, True, False, True]

# Filter customers for a targeted email campaign
targeted_customers = list(compress(customer_names, campaign_flags))
print(f"Customers for Targeted Campaign: {targeted_customers}")

# Benefits:
# - Focuses marketing efforts on relevant customer segments, {Link: DEV Community https://dev.to/usooldatascience/a-guide-to-pythons-itertools-module-use-cases-and-examples-59e}.
# - Optimizes resource allocation by avoiding unnecessary communications, {Link: DEV Community https://dev.to/usooldatascience/a-guide-to-pythons-itertools-module-use-cases-and-examples-59e}.


# ----------------------------------------------------------------------
# 4. itertools.dropwhile(predicate, iterable)
# Drops elements while the predicate is true, then returns the rest.

# Business Use Case: Log File Analysis and Event Monitoring.
# Skipping initial irrelevant lines in a log file until a specific event or pattern is detected, then processing the relevant log entries.
#
# Benefits:
# Efficient Log Processing: Reduces processing time by skipping irrelevant data, focusing on critical events for analysis.
# Real-time Monitoring: Enables faster detection of anomalies or critical events, improving incident response times.


numbers = [1, 4, 6, 3, 8]
result = dropwhile(lambda x: x < 5, numbers)
for num in result:
    print(num)

# Simulate a log file (lines with timestamps and messages)
log_data = [
    "INFO: System startup...",
    "DEBUG: Loading modules...",
    "WARNING: Low disk space detected!",
    "INFO: User logged in: admin",
    "ERROR: Database connection failed!",
    "INFO: Processing complete."
]

# Drop log entries until the first warning or error is encountered
relevant_logs = list(dropwhile(lambda line: not ("WARNING" in line or "ERROR" in line), log_data))

print("Relevant Log Entries:")
for entry in relevant_logs:
    print(entry)

# Benefits:
# - Quickly focuses on critical events in log files by skipping irrelevant entries,.
# - Reduces processing time and enables faster incident response,.


# ----------------------------------------------------------------------
# 5. itertools.filterfalse(predicate, iterable)
# Returns elements for which the predicate is false.

# Business Use Case: Identifying Non-Compliant Data or Outliers.
# Filtering a dataset to identify records that do not meet specific validation criteria or are considered outliers, such as filtering a list of customer orders to identify those that haven't been fulfilled.
#
# Benefits:
# Data Quality Assurance: Helps ensure data accuracy and compliance by quickly identifying invalid or unusual data points.
# Improved Business Decisions: Provides insights into potential issues or inconsistencies that need addressing, leading to better operational decisions.


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = filterfalse(lambda x: x > 4, numbers)
print(list(result))

# Sensor readings (e.g., temperature)
sensor_readings = [22.5, 23.0, 24.1, 35.0, 22.8, 23.5, 36.2, 24.0]


# Define a function to check for normal readings (e.g., between 20 and 30)
def is_normal_reading(temp):
    return 20 <= temp <= 30


# Identify outlier readings (those that are not normal)
outliers = list(filterfalse(is_normal_reading, sensor_readings))
print(f"Outlier Readings: {outliers}")

# Benefits:
# - Helps ensure data quality and identify anomalies or non-compliant data,.
# - Facilitates proactive maintenance or intervention based on outlier detection,.

# ----------------------------------------------------------------------
# 6. itertools.groupby(iterable, key=None)
# Groups consecutive items in an iterable with the same key.
# For an example, see python.plainenglish.io.

# Business Use Case: Sales Data Analysis and Reporting.
# Grouping sales transactions by product category, customer segment, or region to analyze performance and trends.
#
# Benefits:
# Granular Insights: Enables detailed analysis of sales data by categorizing transactions, providing actionable insights into performance drivers.
# Efficient Reporting: Facilitates the creation of summarized reports and dashboards for easier data visualization.


# Sample sales transactions (sorted by product category for groupby to work correctly)
sales_transactions = [
    {'category': 'Electronics', 'product': 'Laptop', 'price': 1200},
    {'category': 'Electronics', 'product': 'Monitor', 'price': 300},
    {'category': 'Clothing', 'product': 'T-Shirt', 'price': 25},
    {'category': 'Clothing', 'product': 'Jeans', 'price': 60},
    {'category': 'Electronics', 'product': 'Keyboard', 'price': 75},
]

# Sort by category for groupby to work as intended
sales_transactions.sort(key=lambda x: x['category'])

# Group transactions by product category
for category, group in groupby(sales_transactions, key=lambda x: x['category']):
    print(f"\nCategory: {category}")
    total_sales_in_category = 0
    for item in group:
        print(f"  - Product: {item['product']}, Price: ${item['price']}")
        total_sales_in_category += item['price']
    print(f"  Total sales in {category}: ${total_sales_in_category}")

# Benefits:
# - Provides granular insights into sales performance by categorizing transactions,.
# - Facilitates efficient reporting and analysis of sales trends,.

# ----------------------------------------------------------------------
# 7. itertools.islice(iterable, start, stop=None, step=1)
# Returns a slice of an iterable.

# Business Use Case: Processing Large Datasets in Chunks.
# Reading and processing a large file in smaller, manageable chunks to avoid memory exhaustion.
#
# Benefits:
# Memory Efficiency: Allows for processing large files without loading the entire dataset into memory, preventing crashes and improving performance.
# Scalability: Enables handling progressively larger datasets by processing data in manageable chunks, supporting growth and increased data volume.


text = "ABCDEFG"
# Slice from index 2 to the end
result = islice(text, 2, None)
print(list(result))

# Simulate a large CSV file (e.g., 'large_data.csv')
# For demonstration, let's create a dummy file
with open('large_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Name', 'Value'])
    for i in range(1, 10001):
        writer.writerow([i, f'Item {i}', i * 10])

# Process the file in chunks of 1000 rows
chunk_size = 1000
with open('large_data.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # Skip header
    
    chunk_num = 1
    while True:
        chunk = list(islice(reader, chunk_size))
        if not chunk:
            break
        
        print(f"\nProcessing Chunk {chunk_num} (first 5 rows):")
        for row in chunk[:5]:
            print(row)
        chunk_num += 1

# Benefits:
# - Efficiently processes large datasets without loading the entire file into memory, {Link: Stack Overflow https://stackoverflow.com/questions/74871587/improve-itertools-pairwise-function}.
# - Improves performance and prevents crashes when dealing with memory-intensive tasks,.


# ----------------------------------------------------------------------
# 8. itertools.starmap(function, iterable)
# Applies a function to the items of an iterable, treating each item as arguments to the function.

# Business Use Case: Applying Multiple Calculations to Data Records.
# Calculating metrics for each customer or product in a database, where each calculation requires multiple input values.
#
# Benefits:
# Concise and Readable Code: Simplifies the application of functions to data records, making the code more readable and maintainable.
# Functional Programming Style: Promotes a functional approach to data processing, enhancing code clarity and testability.

points = [(2, 5), (3, 2), (10, 3)]
results = starmap(pow, points)
for result in results:
    print(result)

# Customer data with purchase amounts and discount percentages
customer_data = [
    (100, 0.10),  # Purchase amount, discount %
    (50, 0.05),
    (200, 0.15),
    (75, 0.08)
]


# Function to calculate final price after discount
def calculate_final_price(amount, discount_percentage):
    return amount * (1 - discount_percentage)


# Calculate final prices for all customers using starmap
final_prices = list(starmap(calculate_final_price, customer_data))
print(f"Final Prices for Customers: {final_prices}")

# Benefits:
# - Simplifies the application of functions with multiple arguments to each item in an iterable.
# - Promotes a more concise and readable code style for data transformations.

# ----------------------------------------------------------------------
# 9. itertools.takewhile(predicate, iterable)
# Returns elements as long as the predicate is true.

# Business Use Case: Processing Data Until a Condition is Met.
# Reading and processing data from a sensor stream until a threshold value is exceeded, then stopping data collection.
#
# Benefits:
# Resource Optimization: Avoids processing unnecessary data by stopping when the desired condition is met, saving computation time and resources.
# Real-time Decision Making: Enables quick responses to changing conditions by stopping processing as soon as a critical event occurs.

numbers = [1, 4, 6, 4, 1]
result = takewhile(lambda x: x < 5, numbers)
for num in result:
    print(num)

# Stream of sensor readings (e.g., temperature)
sensor_stream = [22.0, 22.5, 23.1, 24.0, 28.5, 30.1, 31.5, 29.8]

# Process readings until the temperature exceeds 30 degrees Celsius
safe_readings = list(takewhile(lambda temp: temp <= 30.0, sensor_stream))
print(f"Safe Temperature Readings: {safe_readings}")

# Benefits:
# - Optimizes resource usage by stopping data processing once a specific condition is met, {Link: ealizadeh.com https://ealizadeh.com/blog/itertools/}.
# - Enables quick responses to changing conditions by focusing on data within a defined range,.

# ----------------------------------------------------------------------
# 10. itertools.tee(iterable, n=2)
# Returns n independent iterators from a single iterable.

# Business Use Case: Performing Multiple Analyses on the Same Data Stream.
# Branching a data stream to perform different analyses, like calculating aggregates and filtering based on different criteria, without rereading the original data.
#
# Benefits:
# Reduced Data Redundancy: Avoids rereading the same data multiple times for different analyses, improving efficiency.
# Streamlined Data Pipelines: Simplifies the creation of complex data processing pipelines by creating multiple independent branches from a single data source.


original_list = [1, 2, 3]
iter1, iter2 = tee(original_list, 2)

print(list(iter1))
print(list(iter2))

# Raw data stream (e.g., customer purchase amounts)
purchase_amounts = [150, 200, 50, 300, 120, 80]

# Create two independent iterators from the same data stream
stream1, stream2 = tee(purchase_amounts, 2)

# Calculate total sales from stream1
total_sales = sum(stream1)

# Filter for high-value purchases from stream2
high_value_purchases = [p for p in stream2 if p >= 200]

print(f"Total Sales: ${total_sales}")
print(f"High-Value Purchases: {high_value_purchases}")

# Benefits:
# - Avoids redundant data access by enabling multiple analyses on the same data stream,.
# - Supports complex data pipelines by allowing independent processing branches from a single source,.


# ----------------------------------------------------------------------
# 11. itertools.zip_longest(*iterables, fillvalue=None)
# Zips multiple iterables until the longest is exhausted, filling missing values.

# Business Use Case: Merging Data from Unequal Length Sources.
# Combining customer details with order information when some customers may not have placed orders, or vice versa.
#
# Benefits:
# Flexible Data Integration: Handles cases where data sources have different lengths, preventing data loss or errors during integration.
# Comprehensive Reporting: Ensures all available data is included in reports, even when some fields are missing, providing a complete overview.

students = ["Bob", "Ann", "John", "Marry", "Daisy", "Amy"]
grades = ["A", "A+", "D"]

for student, grade in zip_longest(students, grades, fillvalue="-"):
    print(student, grade)

# Customer data
customers = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

# Order data (some customers might not have orders)
orders = ['Order 101', 'Order 102', 'Order 103']

# Merge customer and order data, filling missing order information with 'N/A'
merged_data = list(zip_longest(customers, orders, fillvalue='N/A'))
print("Customer and Order Data:")
for customer, order in merged_data:
    print(f"Customer: {customer}, Order: {order}")

# Benefits:
# - Combines iterables of different lengths without data loss by filling in missing values.
# - Ensures comprehensive reporting by including all available data, even when some fields are incomplete.


# ----------------

# In summary, itertools functions are powerful tools for businesses to improve data processing efficiency, manage large
# datasets, and make more informed decisions by providing specialized functions for efficient and flexible iteration over
# data. They enable developers to write cleaner, more memory-efficient, and scalable code, contributing to better
# overall business performance and reduced operational costs.
