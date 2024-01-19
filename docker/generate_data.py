from faker import Faker
import random
import csv
import pandas
import numpy as np

fake = Faker()

def generate_client_data(num_records, csv_path):
    fieldnames = [
        'client_id', 'name', 'age', 'gender', 'marital_status', 'employment_status',
        'location', 'annual_income', 'housing_condition', 'private_car', 
        'number_credits_loans', 'national_bank_reported', 'credit_score',
        'app_installed', 'email', 'phone'
    ]

    # Define parameters for the log-normal distribution
    log_mean = np.log(60000)  # Mean of the log-normal distribution
    log_std = 0.8  # Standard deviation of the log-normal distribution
    # Minimum income threshold to prevent unrealistically low incomes
    min_income_threshold = 25000  # Adjust as needed

    # Define a custom probability distribution for the number of clients reported to national bank
    reports_distribution = [0.9, 0.1]

    # Define a custom probability distribution for the number of clients reported to national bank
    housing_distribution = [0.3, 0.2, 0.5]
    

    with open(csv_path+'client_data.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(num_records):
            client_id = fake.unique.random_number()
            name = fake.name()
            age = fake.random_int(min=18, max=80)
            gender = fake.random_element(elements=('Male', 'Female'))
            marital_status = fake.random_element(elements=('Single', 'Married', 'Divorced'))
            employment_status = fake.random_element(elements=('Employed', 'Unemployed', 'Self-Employed'))
            location = fake.city()
            
            # Generate annual income using log-normal distribution
            log_income = np.random.normal(loc=log_mean, scale=log_std)
            annual_income = round(np.exp(log_income), 2)
            # Apply a minimum income threshold
            annual_income = 25000.00 if annual_income < 25000.00 else annual_income

            # Generate the number of loans using the custom distribution
            number_credits_loans = generate_number_of_loans(annual_income)

            # Generate the number of clients reported to national bank using the custom distribution
            national_bank_reported = np.random.choice([True, False], p=reports_distribution)

            # Generate the different housing conditions using the custom distribution
            housing_condition = np.random.choice(['Own', 'Rent', 'Mortgage'], p=housing_distribution)

            private_car = fake.random_element(elements=(True, False))
            credit_score = fake.random_int(min=300, max=850)
            app_installed = fake.random_element(elements=(True, False))
            email = fake.email()
            phone = fake.phone_number()

            writer.writerow({
                'client_id': client_id,
                'name': name,
                'age': age,
                'gender': gender,
                'marital_status': marital_status,
                'employment_status': employment_status,
                'location': location,
                'annual_income': annual_income,
                'housing_condition': housing_condition,
                'private_car': private_car,
                'number_credits_loans': number_credits_loans,
                'national_bank_reported': national_bank_reported,
                'credit_score': credit_score,
                'app_installed': app_installed,
                'email': email,
                'phone': phone
            })

def generate_number_of_loans(annual_income):
    # Divide income into three levels and assign probabilities accordingly
    if annual_income < 40000:
        probabilities = [0.6, 0.3, 0.08, 0.015, 0.005]  # Adjust as needed
    elif annual_income < 80000:
        probabilities = [0.36, 0.28, 0.25, 0.08, 0.03]  # Adjust as needed
    else:
        probabilities = [0.05, 0.1, 0.2, 0.3, 0.35]  # Adjust as needed

    
    return np.random.choice([1, 2, 3, 4, 5], p=probabilities)


def generate_communication_data(clients_ids):

if __name__ == "__main__":
    num_records_to_generate = 1000
    csv_path = '/home/mikemadeira_aux/Documents/Projects/Intelligent-Debt-Collection/docker/bank_debt_data/' 
    generate_client_data(num_records_to_generate, csv_path)