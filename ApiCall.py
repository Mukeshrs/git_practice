from watson_machine_learning_client import WatsonMachineLearningAPIClient
import json
def apicall(id):
    wml_credential = {
                "apikey": "ZFx_bv7PIYgofeIUX_rRo2KBAo-CQ7dGjuSFstoYqKpu",
                "instance_id": "17c49ad1-7170-4aaf-9b56-3b17bc91419b",
                "url": "https://us-south.ml.cloud.ibm.com"
            }
    client = WatsonMachineLearningAPIClient(wml_credential)

    scoring_endpoint = "https://us-south.ml.cloud.ibm.com/v4/deployments/eecc4287-a6bc-44f6-90d7-1628e4e066bd/predictions"

    payload_scoring = {"input_data": [{"fields": ["Loan_ID", "Gender", "Married", "Dependents", "Education",
                                              "Self_Employed", "ApplicantIncome", "CoapplicantIncome", "LoanAmount",
                                              "Loan_Amount_Term", "Credit_History", "Property_Area"], "values": [id]}]}

    return client.deployments.score(scoring_endpoint, payload_scoring)

