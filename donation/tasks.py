from donation_backend.eaacelery import app
from eaaxero import import_bank_transactions, import_trial_balance


@app.task(bind=True)
def process_bank_transactions(self):
    print("Processing bank transactions...")
    # TODO download receipt spreadsheet
    import_bank_transactions()
    # Everything else with receipts happens automatically. See donation.models.BankTransaction.save()
    import_trial_balance()
