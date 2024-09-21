# Base Class: Reservation
class Reservation:
    def __init__(
        self, reservationID: int, startDate: str, endDate: str, isConfirmed: bool
    ):
        self._reservationID = reservationID
        self._startDate = startDate
        self._endDate = endDate
        self._isConfirmed = isConfirmed

    # Getter and Setter for reservationID
    def get_reservationID(self) -> int:
        return self._reservationID

    def set_reservationID(self, reservationID: int):
        self._reservationID = reservationID

    # Getter and Setter for startDate
    def get_startDate(self) -> str:
        return self._startDate

    def set_startDate(self, startDate: str):
        self._startDate = startDate

    # Getter and Setter for endDate
    def get_endDate(self) -> str:
        return self._endDate

    def set_endDate(self, endDate: str):
        self._endDate = endDate

    # Getter and Setter for isConfirmed
    def is_confirmed(self) -> bool:
        return self._isConfirmed

    def set_isConfirmed(self, isConfirmed: bool):
        self._isConfirmed = isConfirmed

    # Methods
    def confirmReservation(self):
        self._isConfirmed = True
        print("Reservation confirmed.")

    def cancelReservation(self):
        self._isConfirmed = False
        print("Reservation canceled.")


# Derived Class: OnlineReservation
class OnlineReservation(Reservation):
    def __init__(
        self,
        reservationID: int,
        startDate: str,
        endDate: str,
        isConfirmed: bool,
        website: str,
        onlinePaymentSuccess: bool,
    ):
        super().__init__(reservationID, startDate, endDate, isConfirmed)
        self._website = website
        self._onlinePaymentSuccess = onlinePaymentSuccess

    # Getter and Setter for website
    def get_website(self) -> str:
        return self._website

    def set_website(self, website: str):
        self._website = website

    # Getter and Setter for onlinePaymentSuccess
    def is_onlinePaymentSuccess(self) -> bool:
        return self._onlinePaymentSuccess

    def set_onlinePaymentSuccess(self, onlinePaymentSuccess: bool):
        self._onlinePaymentSuccess = onlinePaymentSuccess

    # Method to complete online payment
    def completeOnlinePayment(self) -> bool:
        if not self._onlinePaymentSuccess:
            print("Online payment failed.")
            return False
        print("Online payment successful.")
        return True


# Derived Class: HotelReservation
class HotelReservation(Reservation):
    def __init__(
        self,
        reservationID: int,
        startDate: str,
        endDate: str,
        isConfirmed: bool,
        frontDeskAgent: str,
        paymentOnArrival: bool,
    ):
        super().__init__(reservationID, startDate, endDate, isConfirmed)
        self._frontDeskAgent = frontDeskAgent
        self._paymentOnArrival = paymentOnArrival

    # Getter and Setter for frontDeskAgent
    def get_frontDeskAgent(self) -> str:
        return self._frontDeskAgent

    def set_frontDeskAgent(self, frontDeskAgent: str):
        self._frontDeskAgent = frontDeskAgent

    # Getter and Setter for paymentOnArrival
    def is_paymentOnArrival(self) -> bool:
        return self._paymentOnArrival

    def set_paymentOnArrival(self, paymentOnArrival: bool):
        self._paymentOnArrival = paymentOnArrival

    # Method to accept cash payment
    def acceptCashPayment(self):
        print("Cash payment accepted at the hotel.")


# Class: Item
class Item:
    def __init__(self, itemID: int, description: str, price: float):
        self._itemID = itemID
        self._description = description
        self._price = price

    # Getter and Setter for itemID
    def get_itemID(self) -> int:
        return self._itemID

    def set_itemID(self, itemID: int):
        self._itemID = itemID

    # Getter and Setter for description
    def get_description(self) -> str:
        return self._description

    def set_description(self, description: str):
        self._description = description

    # Getter and Setter for price
    def get_price(self) -> float:
        return self._price

    def set_price(self, price: float):
        self._price = price


# Class: Customer
class Customer:
    def __init__(self, customerID: int, name: str, email: str):
        self._customerID = customerID
        self._name = name
        self._email = email

    # Getter and Setter for customerID
    def get_customerID(self) -> int:
        return self._customerID

    def set_customerID(self, customerID: int):
        self._customerID = customerID

    # Getter and Setter for name
    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str):
        self._name = name

    # Getter and Setter for email
    def get_email(self) -> str:
        return self._email

    def set_email(self, email: str):
        self._email = email


# Testing the classes

# Create a customer
customer1 = Customer(customerID=101, name="Ted Vera", email="tedvera@example.com")

# Create an item (e.g., room type)
room1 = Item(
    itemID=1, description="2 Queen Beds, No Smoking, Desk, Coffee Maker", price=179.90
)

# Create a reservation
reservation1 = Reservation(
    reservationID=50253687,
    startDate="2023-08-22",
    endDate="2023-08-24",
    isConfirmed=False,
)

# Confirm the reservation
reservation1.confirmReservation()

# Create an online reservation
onlineReservation = OnlineReservation(
    reservationID=50253687,
    startDate="2023-08-22",
    endDate="2023-08-24",
    isConfirmed=True,
    website="hotel.com",
    onlinePaymentSuccess=True,
)
onlineReservation.completeOnlinePayment()

# Create a hotel reservation
hotelReservation = HotelReservation(
    reservationID=50253687,
    startDate="2023-08-22",
    endDate="2023-08-24",
    isConfirmed=True,
    frontDeskAgent="John Doe",
    paymentOnArrival=True,
)
hotelReservation.acceptCashPayment()

# Display customer information
print(f"Customer: {customer1.get_name()} - Email: {customer1.get_email()}")

# Display room information
print(f"Room: {room1.get_description()} - Price: {room1.get_price()}")

# Display reservation information
print(
    f"Reservation ID: {reservation1.get_reservationID()}, Start Date: {reservation1.get_startDate()}, End Date: {reservation1.get_endDate()}, Is Confirmed: {reservation1.is_confirmed()}"
)
