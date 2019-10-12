import os
from mtnmomo.collection import Collection

client = Collection({
    "COLLECTION_USER_ID": "ff6552c6-b972-46dc-8a81-dee747192f1d",
    "COLLECTION_API_SECRET": "22a1a0745f1d41d5aeb90d0e03c409c0",
    "COLLECTION_PRIMARY_KEY": "ae71f8ac0c7e48a99020fe721b886560"
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
