import os
from mtnmomo.collection import Collection

client = Collection({
    "COLLECTION_USER_ID": os.environ.get('COLLECTION_USER_ID'),
    "COLLECTION_API_SECRET": os.environ.get('COLLECTION_API_SECRET'),
    "COLLECTION_PRIMARY_KEY": os.environ.get('COLLECTION_PRIMARY_KEY')
})


from flask import Flask
app = Flask(__name__)

@app.route("/requestToPay")
def requestToPay():
    requestToPay = client.requestToPay(
        mobile="256772123456", amount="600", external_id="123456789", payee_note="dd", payer_message="dd", currency="EUR")
    return requestToPay

@app.route("/requestToPay/<string:transaction_ref>")
def getTransactionStatus(transaction_ref):
    
    return client.getTransactionStatus(transaction_ref)

if __name__ == "__main__":
    app.run()
