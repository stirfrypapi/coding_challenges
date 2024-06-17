
class Solution:
    def __init__(self):
        self.merchant_fraud_times = {}
        """
        {
            
        }
        """

        self.card_fraud_times = {}
        """
        {
            "4343": [
        }
        """

        self.running_amount = 0

    def perform_transaction(self, time, detail, amount, card, merchant):
        # check card fraud and merchant fraud
        if (merchant in self.merchant_fraud_times \
                and self.merchant_fraud_times[merchant] <= time):
            return "{} {} {} REJECT".format(time, detail, amount)

        if (card in self.card_fraud_times \
                and self.card_fraud_times[card] <= time):
            return "{} {} {} REJECT".format(time, detail, amount)

        if (merchant in self.merchant_fraud_times
                and self.merchant_fraud_times[merchant] > time):
            self.running_amount += float(amount)

        elif (card in self.card_fraud_times \
              and self.card_fraud_times[card] > time):
            self.running_amount += float(amount)

        return "{} {} {} APPROVE".format(time, detail, amount)

    def set_merchant_fraud_time(self, merchant_name, time):
        self.merchant_fraud_times[merchant_name] = time

    def set_card_fraud_time(self, card_num, time):
        self.card_fraud_times[card_num] = time

    def get_credit_losses(self):
        return self.running_amount

if __name__ == "__main__":
    sol = Solution()
    transactions = [
        "5,R1,5.60,4242424242424242,bobs_burgers"
        ,"10,R2,500.00,4242111111111111,a_corp"
        ,"20,card_number,4242111111111111"
        ,"21, card_number,4343111111111111"
        ,"22,R3,400.00,4343111111111111,bobs_burgers"
        ,"23,R4,100.00,4242111111111111,bobs_burgers"
        # bobs_burgers will be flagged as fraud at t=23
    ]

    for request in transactions:
        if len(request) == 5:
            reqs = request.split(",")
            time, detail, amount, card, merchant = int(reqs[0]), reqs[1], reqs[2], reqs[3], reqs[4]
            print(sol.perform_transaction(time, detail, amount, card, merchant))
        if len(request) == 3:
            rul = request.split(",")
            time, detail, detail2 = int(rul[0]), rul[1], rul[2]

            if detail == "merchant":
                sol.set_merchant_fraud_time(detail2, time)
            if detail == "card_number":
                sol.set_card_fraud_time(detail2, time)


    print(sol.get_credit_losses())
