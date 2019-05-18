import json


class RestAPI(object):

    def __init__(self, database=None):
        self.database = {}
        if database:
            users = database.get("users")
            for user in users:
                self.database[user["name"]] = {
                    "owes": user["owes"],
                    "owed_by": user["owed_by"],
                    "balance": user["balance"]
                }

    def get(self, url: str, payload=None):
        if url == "/users":
            if not payload:
                return json.dumps(
                    {
                        "users": [
                            {
                                "name": self.database[user]["name"],
                                "owes":self.database[user]["owes"],
                                "owed_by":self.database[user]["owed_by"],
                                "balance":self.database[user]["balance"]
                            } for user in self.database]
                    }
                )
            users_query = json.loads(payload).get("users")
            ans = {}
            ans["users"] = []
            if users_query:
                users_query.sort()
                for user in users_query:
                    u = self.database.get(user)
                    u["name"] = user
                    ans["users"].append(u)
            return json.dumps(ans)

    def post(self, url: str, payload=None):
        if url == "/add":
            user_string = json.loads(payload)
            user = {
                "owes": {},
                "owed_by": {},
                "balance": 0
            }
            self.database[user_string["user"]] = user
            user["name"] = user_string["user"]
            return json.dumps(user)

        elif url == "/iou":
            payload = json.loads(payload)

            l, b, amount = payload["lender"], payload[
                "borrower"], payload["amount"]

            l_b_balance = self.database[l]["owed_by"].pop(
                b, 0) - self.database[l]["owes"].pop(b, 0)
            self.database[b]["owed_by"].pop(l, 0)
            self.database[b]["owes"].pop(l, 0)
            l_b_balance += amount

            if l_b_balance > 0:
                self.database[l]["owed_by"][b] = l_b_balance
                self.database[b]["owes"][l] = l_b_balance
            elif l_b_balance < 0:
                self.database[l]["owes"][b] = -l_b_balance
                self.database[b]["owed_by"][l] = -l_b_balance

            self.database[l]["balance"] += payload["amount"]
            self.database[b]["balance"] -= payload["amount"]

            return self.get("/users", json.dumps({"users": [payload["lender"], payload["borrower"]]}))
