
from scraper import create_data_dir, fetch_reviews, save_reviews_to_csv

apps = {
    'CBE': 'com.ethiopian.cbe.mobile',
    'BOA': 'com.boa.boamobile',
    'Dashen': 'com.teklogix.amole',
}

def main():
    create_data_dir()
    all_reviews = []

    for bank, app_id in apps.items():
        bank_reviews = fetch_reviews(app_id, bank)
        all_reviews.extend(bank_reviews)

    save_reviews_to_csv(all_reviews)

if __name__ == "__main__":
    main()
