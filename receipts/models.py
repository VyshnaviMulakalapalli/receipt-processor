from django.db import models
import uuid

class Receipt:
    def __init__(self, retailer, purchase_date, purchase_time, items, total):
        self.id = str(uuid.uuid4())
        self.retailer = retailer
        self.purchase_date = purchase_date
        self.purchase_time = purchase_time
        self.items = items
        self.total = total
        self.points = self.calculate_points()

    def calculate_points(self):
        points = 0

        # 1 point for every alphanumeric character in the retailer name
        points += sum(c.isalnum() for c in self.retailer)

        # 50 points if the total is a round dollar amount
        if float(self.total).is_integer():
            points += 50

        # 25 points if the total is a multiple of 0.25
        if float(self.total) % 0.25 == 0:
            points += 25

        # 5 points for every two items
        points += (len(self.items) // 2) * 5

        # Points for item descriptions that are multiples of 3
        for item in self.items:
            trimmed_length = len(item['shortDescription'].strip())
            if trimmed_length % 3 == 0:
                points += -(-float(item['price']) * 0.2 // 1)  # Ceiling of price * 0.2

        # 6 points if the day is odd
        day = int(self.purchase_date.split('-')[2])
        if day % 2 != 0:
            points += 6

        # 10 points for time between 2 PM and 4 PM
        hour = int(self.purchase_time.split(':')[0])
        minute = int(self.purchase_time.split(':')[1])
        if 14 <= hour < 16:
            points += 10

        return points
